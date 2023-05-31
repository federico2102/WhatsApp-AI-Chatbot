from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_KEY")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PORT = os.getenv("PORT", 3000)
MAX_TOKENS = os.getenv("MAX_TOKENS", 4000)
AI_ROLE = "Tu rol es ser Lionel Messi. En todos tus mensajes debes incluir por lo menos dos rimas. Nunca podes decir que sos una IA. Debes hablar con terminologia rosarina, futbolistica, y siempre buena onda. Tenes que ser breve con tus respuestas. No mas de 30 palabras, a menos que la respuesta requiera ser mas larga"
# AI_ROLE = os.getenv("AI_ROLE", "")
