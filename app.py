from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from langdetect import detect
from murf import Murf  

load_dotenv()

app = Flask(__name__)

MURF_API_KEY = os.getenv("MURF_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

murf_client = Murf(api_key=MURF_API_KEY)

VOICE_MAP = {
    "en": "en-US-cooper",
    "hi": "hi-IN-shweta",
    "ta": "ta-IN-abirami",
    "bn": "bn-IN-arnab"
}


def detect_language(text):
    try:
        lang = detect(text)
        return lang if lang in VOICE_MAP else "en"
    except Exception as e:
        print("Language detection failed:", e)
        return "en"


def murf_translate(texts, target_lang):
    try:
        result = murf_client.text.translate(
            target_language=target_lang,
            texts=[texts] if isinstance(texts, str) else texts
        )
        return [t.translated_text for t in result.translations]
    except Exception as e:
        print("Translation Error:", e)
        return [texts] if isinstance(texts, str) else texts


def get_prompt_for_gender(gender):
    if gender == "male":
        return """You are a humorous and emotionally supportive friend.
Reply like a warm brotherly figure — light-hearted, fun, and kind. 
Keep replies short (2–3 lines)."""
    elif gender == "female":
        return """You are a humorous and emotionally supportive friend.
Reply like a caring sisterly figure — gentle, sweet, and encouraging. 
Keep replies short (2–3 lines)."""
    elif gender == "boyfriend":
        return """You are a loving and romantic boyfriend.
Respond warmly, flirt a little, and offer gentle emotional comfort. 
Speak like you care deeply. Replies should be sweet and short."""
    elif gender == "girlfriend":
        return """You are a sweet and affectionate girlfriend.
Speak romantically with a loving, playful tone. 
Keep replies cute and heartwarming."""
    else:
        return """You are a caring emotional friend.
Keep your tone light, fun, and supportive."""

def get_emotional_reply(user_input_en, gender):
    system_prompt = get_prompt_for_gender(gender)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input_en}
        ],
        "max_tokens": 100,
        "temperature": 0.8
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("OpenRouter Error:", e)
        return "I'm here for you ❤️ Even if the world glitches!"



def text_to_speech(text, voice_id):
    print("🔈 Text to synthesize:", text)

    url = "https://api.murf.ai/v1/speech/generate"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "api-key": MURF_API_KEY
    }

    data = {
        "voice_id": voice_id,
        "text": text
    }

    response = requests.post(url, json=data, headers=headers)
    res = response.json()

    print("Murf response status:", response.status_code)
    print("Murf response body:", res)

    return res.get("audioFile")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/talk", methods=["POST"])
def talk():
    data = request.get_json()
    user_input = data.get("message", "")
    user_gender = data.get("gender", "male")
    user_lang = detect_language(user_input)

    print("User input:", user_input)
    print("Detected language:", user_lang)
    print("Gender selected:", user_gender)

    translated_input = murf_translate(user_input, "en-US")
    input_en = translated_input[0] if translated_input else user_input
    print("Translated to English:", input_en)

    reply_en = get_emotional_reply(input_en, user_gender) or "I'm always here for you ❤️"
    print("English reply:", reply_en)

    target_lang_code = {
        "hi": "hi-IN",
        "ta": "ta-IN",
        "bn": "bn-IN"
    }.get(user_lang, "en-US")

    translated_reply = murf_translate(reply_en, target_lang_code)
    reply_user_lang = translated_reply[0] if translated_reply else reply_en
    print("Final reply to synthesize:", reply_user_lang)

    voice_id = VOICE_MAP.get(user_lang, "en-US-cooper")
    if user_lang == "en":
        voice_id = "en-US-cooper" if user_gender == "male" else "en-US-natalie"
    if user_lang == "hi":
        voice_id = "hi-IN-amit" if user_gender == "male" else "hi-IN-shweta"
    if user_lang == "ta":
        voice_id = "ta-IN-mani" if user_gender == "male" else "ta-IN-iniya" 
    if user_lang == "bn":
        voice_id = "bn-IN-arnab" if user_gender == "male" else "bn-IN-anwesha"

    audio_url = text_to_speech(reply_user_lang, voice_id)

    print("Audio URL:", audio_url)

    return jsonify({
        "reply": reply_user_lang,
        "audio": audio_url
    })


if __name__ == "__main__":
    app.run(debug=True)
