
---

# WhatsApp AI Chatbot

## Overview
The WhatsApp AI Chatbot integrates OpenAI's API to provide automated responses to messages sent through WhatsApp. This project includes webhook handling, database storage of chat history, token management, and utilizes Flask as a backend server. Key functionalities include verifying webhook requests, processing incoming messages, and interacting with OpenAI to generate AI-powered responses sent via WhatsApp.

## Skills Demonstrated
This project showcases the following skills and technologies:
- **Python Development**: Backend logic with Flask, using modular file structure and clear error handling.
- **API Integration**: Working with OpenAI's API and WhatsApp's API to handle messaging and AI response generation.
- **Database Management**: Using SQLite to store chat history, manage message logs, and ensure data integrity.
- **Environment Management**: Securely storing and loading configuration variables using `.env` files.
- **JSON Processing**: Handling and parsing JSON data for webhook verification and message handling.
- **Error Handling**: Implementing structured error handling for API interactions and database operations.

## Prerequisites
- Python 3.7+
- Flask
- OpenAI Python client
- WhatsApp Business API (or equivalent test setup)

## Setup Instructions
Follow these steps to set up and run the project locally.

### 1. Clone the Repository
Clone the project from the repository:
```bash
git clone https://github.com/federico2102/WhatsApp-AI-Chatbot.git
cd WhatsApp-AI-Chatbot
```

### 2. Install Dependencies
Create a virtual environment and install the necessary dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # For Windows, use: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory to store sensitive information:
```plaintext
OPENAI_API_KEY=your_openai_api_key
WHATSAPP_TOKEN=your_whatsapp_token
VERIFY_TOKEN=your_verification_token
PORT=3000  # Or any other available port
MAX_TOKENS=4000
```

### 4. Database Setup
The app uses SQLite for storing messages. No additional setup is required, as the database file will be created automatically on the first run.

### 5. Run the Flask Server
To start the server, run:
```bash
python server.py
```
The server will be running on `http://127.0.0.1:3000/` by default.

### 6. Test Webhook Endpoint
Use a tool like Postman to test the webhook endpoint. Send a POST request to `http://127.0.0.1:3000/webhook` with a JSON payload like:
```json
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "changes": [
        {
          "value": {
            "metadata": {
              "phone_number_id": "YOUR_PHONE_NUMBER_ID"
            },
            "messages": [
              {
                "from": "YOUR_PHONE_NUMBER",
                "text": {
                  "body": "Hello AI!"
                }
              }
            ]
          }
        }
      ]
    }
  ]
}
```

### 7. Check Responses
If configured correctly, the server will process incoming messages and respond using OpenAI’s API via WhatsApp. Responses will also be logged in the `chat_history.db` SQLite database.

## Directory Structure
- `server.py`: Entry point to start the Flask server.
- `routes.py`: Contains the webhook route for handling incoming messages.
- `openai_handler.py`: Handles communication with OpenAI's API.
- `database.py`: Manages database interactions to store and retrieve chat history.
- `whatsapp.py`: Contains functions to send messages via the WhatsApp API.
- `utils.py`: Includes utility functions for token management and chat history formatting.
- `.env`: Contains environment variables for sensitive data.

## Testing
To verify that the chatbot works as expected, you can simulate incoming messages via the webhook endpoint or directly through WhatsApp if integrated with a real number. Use Postman to confirm that each request is processed and logged in the database, with the AI's response being sent back through the WhatsApp API.

## Future Enhancements
- **Error Handling Improvements**: Add more detailed error logging for each API interaction.
- **UI Dashboard**: Create a dashboard to visualize chat history and logs.
- **Enhanced NLP**: Utilize more advanced features from OpenAI's models, like fine-tuning for a custom chatbot personality.

---
