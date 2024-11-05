from flask import request, jsonify
from datetime import datetime
from database import create_table, insert_message
from openai_handler import get_openai_answer
from whatsapp_handler import send_whatsapp_message
from config import VERIFY_TOKEN

def setup_routes(app):
    @app.route("/webhook", methods=["GET", "POST"])
    def webhook():
        if request.method == "GET":
            verify_token = request.args.get("hub.verify_token")
            if verify_token == VERIFY_TOKEN:
                return request.args.get("hub.challenge"), 200
            else:
                return "Invalid verification token", 403

        elif request.method == "POST":
            body = request.json
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
                                msg = messages[0]

                                if "text" in msg:
                                    msg_body = msg["text"]["body"]
                                    create_table()
                                    timestamp = datetime.now()
                                    insert_message(modified_phone_number, 'User', timestamp, msg_body)

                                    openai_answer = get_openai_answer(modified_phone_number)
                                    generated_text = openai_answer.choices[0].message.content

                                    send_whatsapp_message(phone_number_id, modified_phone_number, generated_text)

                                    timestamp = datetime.now()
                                    insert_message(modified_phone_number, 'AI', timestamp, generated_text)
                                else:
                                    print("Received a non-text message:", msg)
            return jsonify({"status": "success"}), 200
