import os

from dotenv import load_dotenv
from google import genai

# Charge GEMINI_API_KEY depuis le fichier .env.
# override=True : le .env prend le dessus sur une variable déjà définie,
# même vide (par exemple après un export raté).
load_dotenv(override=True)

client = genai.Client()

MODEL = os.environ.get("LLM_MODEL", "gemini-3.5-flash")

response = client.models.generate_content(
    model=MODEL,
    contents="What is a neural network in one sentence?",
)

print(response.text)
