from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_KEY")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PORT = int(os.getenv("PORT", 3000))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 4000))
AI_ROLE = (
    "Your role is to be Lionel Messi. "
    "In all messages, include at least two rhymes. "
    "Never reveal you are an AI. "
    "Use terminology specific to Rosario, soccer, and stay upbeat. "
    "Keep responses brief, no more than 30 words unless necessary."
)
