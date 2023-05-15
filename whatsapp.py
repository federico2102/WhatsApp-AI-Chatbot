import json
import requests

import config


def send_whatsapp_message(phone_number_id,
                          modified_phone_number,
                          generated_text):
    url = (
        "https://graph.facebook.com/v12.0/"
        + phone_number_id
        + "/messages?access_token="
        + config.token
    )

    data = {
        'messaging_product': 'whatsapp',
        'to': modified_phone_number,
        'type': 'text',
        'text': json.dumps({'body': generated_text}),
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=data, headers=headers)
    print("WhatsApp API Response:", response.status_code)
    print("WhatsApp API Response Content:", response.json())
