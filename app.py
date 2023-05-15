from flask import Flask, request, jsonify

import config
import openai_chat
import whatsapp

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.json

    print(jsonify(body))

    if "object" in body and "entry" in body:
        entry = body["entry"]
        if entry and "changes" in entry[0]:
            changes = entry[0]["changes"]
            if changes and "value" in changes[0]:
                value = changes[0]["value"]
                if "messages" in value:
                    messages = value["messages"]
                    if messages:
                        phone_number_id = value["metadata"]["phone_number_id"]
                        from_number = messages[0]["from"]
                        modified_phone_number = "541115" + from_number[5:]
                        msg_body = messages[0]["text"]["body"]

                        print("EL NUMERO:", modified_phone_number)

                        openai_answer = openai_chat.get_openai_answer(msg_body)
                        generated_text = openai_answer.choices[
                            0].message.content
                        print(generated_text)

                        whatsapp.send_whatsapp_message(phone_number_id,
                                                       modified_phone_number,
                                                       generated_text)

    return jsonify({"status": "success"}), 200


@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == config.verify_token:
            print("WEBHOOK_VERIFIED")
            return challenge, 200
