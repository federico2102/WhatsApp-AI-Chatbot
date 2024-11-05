import tiktoken
import json
from database import delete_oldest_messages, retrieve_chat_history
from config import MAX_TOKENS, AI_ROLE


def format_chat_for_api(phone_number):
    chat_history = retrieve_chat_history(phone_number)
    formatted_chat = []

    # Combine all messages into one prompt
    for message in chat_history:
        formatted_chat.append(f"{message[2]}: {message[4]}")

    # Join into a single prompt for the new API call
    prompt = "\n".join(formatted_chat)
    return prompt

def count_tokens_array(formatted_chat_history):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return sum(len(encoding.encode(json.dumps(text))) for text in formatted_chat_history)

def adjust_tokens_amount(phone_number):
    formatted_chat_history = format_chat_for_api(phone_number)
    total_tokens = count_tokens_array(formatted_chat_history)
    while total_tokens > MAX_TOKENS:
        delete_oldest_messages(phone_number)
        formatted_chat_history = formatted_chat_history[2:]
        total_tokens = count_tokens_array(formatted_chat_history)
    return formatted_chat_history
