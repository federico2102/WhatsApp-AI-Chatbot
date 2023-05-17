import json
import requests
from config import WHATSAPP_TOKEN


def send_whatsapp_message(
        phone_number_id,
        modified_phone_number,
        generated_text):
    url = (
        "https://graph.facebook.com/v12.0/"
        + phone_number_id
        + "/messages?access_token="
        + WHATSAPP_TOKEN
    )

    data = {
        'messaging_product': 'whatsapp',
        'to': modified_phone_number,
        'type': 'text',
        'text': json.dumps({'body': generated_text}),
    }

    headers = {"Content-Type": "application/json"}

    requests.post(url, json=data, headers=headers)
