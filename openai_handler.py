import openai
from utils import adjust_tokens_amount, format_chat_for_api
from config import OPENAI_API_KEY

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_openai_answer(phone_number):
    formatted_chat_history = format_chat_for_api(phone_number)

    try:
        # Make the API call using the correct OpenAI API function
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=formatted_chat_history,
            max_tokens=150  # Adjust max_tokens as needed
        )
        return response
    except Exception as e:  # Catch any unexpected errors
        print("Error occurred while making OpenAI API call:", e)
        adjust_tokens_amount(phone_number)
        # Return an error message as a fallback
        return {"error": "An error occurred while processing the request"}
