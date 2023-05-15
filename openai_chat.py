import openai
from openai import ChatCompletion

import config

openai.api_key = config.openai.api_key


def get_openai_answer(msg_body):
    return ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg_body},
        ],
    )
