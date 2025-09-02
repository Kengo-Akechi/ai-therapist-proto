# Flask Cohere Chatbot

This project is a **Flask-based chatbot** that integrates Cohere's API to handle user queries dynamically. The application provides a simple web interface using Flask-WTF forms for user input and processes responses through Cohere's **chat endpoint**.

## Features

- **Flask Web Interface**: Uses Flask-WTF forms for structured user input.
- **Cohere Chat API**: Enables real-time interactions using Cohere's `chat` method.
- **Secure Configuration**: Includes a secret key for handling form validation securely.
- **Dynamic Response Generation**: Captures user queries and generates relevant responses.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask (`pip install flask`)
- Flask-WTF (`pip install flask-wtf`)
- Cohere SDK (`pip install cohere`)

## Installation

1. Clone the repository or copy the script.
2. Install required dependencies:

   ```bash
   pip install -r requirements.txt