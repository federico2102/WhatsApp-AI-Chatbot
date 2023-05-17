from flask import Flask, request, jsonify
from datetime import datetime
from database import create_table, insert_message
from openai_chat import get_openai_answer
from whatsapp import send_whatsapp_message
from utils import adjust_tokens_amount

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
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

                            # Insert the received message into the database
                            # with the current timestamp
                            create_table()
                            timestamp = datetime.now()
                            insert_message(
                                modified_phone_number,
                                'User',
                                timestamp,
                                msg_body)

                            # Get the response from the OpenAI API
                            openai_answer = get_openai_answer(
                                modified_phone_number)
                            generated_text = openai_answer.choices[
                                0].message.content

                            # Send the generated response via WhatsApp
                            send_whatsapp_message(
                                phone_number_id,
                                modified_phone_number,
                                generated_text)

                            # Save IA answer in messages table
                            timestamp = datetime.now()
                            insert_message(
                                modified_phone_number,
                                'AI',
                                timestamp,
                                generated_text)

                            # Adjust amount of tokens in chat history
                            adjust_tokens_amount(modified_phone_number)
                        else:
                            print("Received a non-text message:", msg)

    return jsonify({"status": "success"}), 200
