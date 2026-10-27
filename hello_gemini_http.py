import json
import os
import urllib.error
import urllib.request

from dotenv import load_dotenv

# Charge GEMINI_API_KEY depuis le fichier .env.
load_dotenv(override=True)

MODEL = os.environ.get("LLM_MODEL", "gemini-3.5-flash")
url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": os.environ["GEMINI_API_KEY"],
}
body = json.dumps({
    "contents": [
        {"parts": [{"text": "What is a neural network in one sentence?"}]}
    ],
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
except urllib.error.HTTPError as e:
    # Affiche le détail de l'erreur renvoyé par l'API (404, 429, clé refusée...).
    print(f"HTTP {e.code}: {e.read().decode()}")
    raise SystemExit(1)

parts = result["candidates"][0]["content"]["parts"]
print("".join(p.get("text", "") for p in parts))
