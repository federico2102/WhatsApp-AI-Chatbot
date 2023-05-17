import tiktoken
import json
from database import delete_oldest_messages, retrieve_chat_history
from config import MAX_TOKENS
from config import AI_ROLE


def format_chat_for_api(phone_number):
    chat_history = retrieve_chat_history(phone_number)
    formatted_chat = []
    for message in chat_history:
        formatted_message = f"{message[2]}: {message[4]}"
        formatted_chat.append(formatted_message)

    formatted_chat_history = [
        {"role": "system", "content": AI_ROLE},
    ]
    for message in formatted_chat:
        formatted_chat_history.append({"role": "user", "content": message})

    return formatted_chat_history


def count_tokens_array(formatted_chat_history):
    total_tokens = 0
    for text in formatted_chat_history:
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        token_count = len(encoding.encode(json.dumps(text)))
        total_tokens += token_count
    return total_tokens


def adjust_tokens_amount(phone_number):
    formatted_chat_history = format_chat_for_api(phone_number)
    total_tokens = count_tokens_array(formatted_chat_history)

    while total_tokens > int(MAX_TOKENS):
        delete_oldest_messages(phone_number)
        formatted_chat_history = formatted_chat_history[2:]
        total_tokens = count_tokens_array(formatted_chat_history)

    return formatted_chat_history
