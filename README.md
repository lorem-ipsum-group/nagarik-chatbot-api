# Nagarik Chatbot API
This Chatbot API powers the [Nagarik frontend](https://github.com/lorem-ipsum-group/nagarik) for enhanced user interactions.

## Getting Started

### Prerequisites
- [Python](https://www.python.org/downloads/)
- OpenAI API key

### Installation

1. Clone the repository:

```
git clone git@github.com:lorem-ipsum-group/nagarik-chatbot-api.git
```

2. Navigate to the repository 📂:

```
cd nagarik-chatbot-api
```

3. Create a virtual environment and activate it.<br>
For Unix-like systems,
```
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies

```
pip3 install -r requirements.txt
```

4. Create a `.env` file inside the root directory

```
touch .env
```

5. Set the following credentials inside the `.env` file

```
#.env
OPENAI_API_KEY=
```

### Usage

1. Run the development server:
```
flask run
```
By default, the API runs on http://localhost:5000/.

2. For getting a response from the Chatbot, send a `POST` request to the API endpoint
```
POST http://localhost:5000/v1/chat HTTP/1.1
Content-Type: application/json

{
    "input": "<insert your question here>"
}
```

## Contributing

We welcome contributions to **Nagarik Chatbot API**! If you find bugs or have ideas for new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
