from flask import Flask, request, jsonify

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Load data
loader = TextLoader("data/data.md")

# Use this line if you need to load a directory of files as source
# loader = DirectoryLoader("data/")

# Create vector store index without persistence
index = VectorstoreIndexCreator().from_loaders([loader])

# Set up Conversational Retrieval Chain with OpenAI GPT-3.5 Turbo
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = []


@app.route('/v1/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the JSON payload
        data = request.get_json()
        user_input = data.get('input')
        query = user_input

        # Query the Conversational Retrieval Chain and get the chatbot's answer
        result = chain({"question": query, "chat_history": chat_history})
        answer = result['answer']

        # Update chat history with the user's input and the chatbot's answer
        chat_history.append((query, answer))

        # Return the chatbot's answer in the response
        return jsonify({"answer": answer})

    except Exception as e:
        # Handle errors and return an error message in the response
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(port=5000)
