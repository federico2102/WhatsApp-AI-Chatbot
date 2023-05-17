from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_KEY")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PORT = os.getenv("PORT", 3000)
MAX_TOKENS = os.getenv("MAX_TOKENS", 4000)
AI_ROLE = os.getenv("AI_ROLE", "")
