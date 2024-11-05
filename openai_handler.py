import openai
from utils import adjust_tokens_amount, format_chat_for_api
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_openai_answer(phone_number):
    formatted_chat_history = format_chat_for_api(phone_number)

    try:
        # Use the latest OpenAI function for chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": formatted_chat_history}],
            max_tokens=150,  # Adjust max_tokens as needed for response length
        )
        return response
    except Exception as e:  # Use a general Exception for compatibility
        print("Error occurred:", e)
        adjust_tokens_amount(phone_number)
        return get_openai_answer(phone_number)
