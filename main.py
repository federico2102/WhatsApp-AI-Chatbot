"use strict";


from dotenv import load_dotenv
#import openai
import os
import requests
from flask import Flask, request, jsonify


load_dotenv()
#openai.api_key = os.getenv("OPENAI_KEY")

app = Flask(__name__)

print("ESTOY LEYENDO")

# Access token for your app
# Save it as an environment variable
token = os.getenv("WHATSAPP_TOKEN")



# Sets server port and logs message on success
@app.route("/webhook", methods=["POST"])
def webhook():
    # Parse the request body from the POST
    body = request.json

    print("LLEGO UN MENSAJEEEEE")

    # Check the Incoming webhook message
    print(jsonify(body))

    # info on WhatsApp text message payload:
    # https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/payload-examples#text-messages
    if "object" in body:
        if (
            "entry" in body
            and body["entry"][0]["changes"]
            and body["entry"][0]["changes"][0]["value"]["messages"]
        ):
            phone_number_id = body["entry"][0]["changes"][0]["value"]["metadata"][
                "phone_number_id"
            ]
            from_number = body["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
            msg_body = body["entry"][0]["changes"][0]["value"]["messages"][0]["text"][
                "body"
            ]

            url = "https://graph.facebook.com/v12.0/" + phone_number_id + "/messages?access_token=" + token

            data = {
                "messaging_product": "whatsapp",
                "to": from_number,
                "text": {"body": "Ack: " + msg_body},
            }
            headers = {"Content-Type": "application/json"}

            response = requests.post(url, json=data, headers=headers)

    return jsonify({"status": "success"}), 200


# Accepts GET requests at the /webhook endpoint. You need
#  this URL to setup webhook initially.
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    verify_token = os.getenv("VERIFY_TOKEN")
    print("LLEGO UN MENSAJEEEEE")

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == verify_token:
            print("WEBHOOK_VERIFIED")
            return challenge, 200

    return "Invalid Request", 403


if __name__ == "__main__":
  app.run(port=os.getenv("PORT", 3000))
# response = openai.Completion.create(
#     engine="davinci", prompt="Once upon a time", max_tokens=50
# )

# generated_text = response["choices"][0]["text"]
# print(generated_text)
