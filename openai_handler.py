import openai
from utils import adjust_tokens_amount, format_chat_for_api
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_openai_answer(phone_number):
    formatted_chat_history = format_chat_for_api(phone_number)
    try:
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=formatted_chat_history,
        )
    except openai.error.InvalidRequestError:
        adjust_tokens_amount(phone_number)
        return get_openai_answer(phone_number)
