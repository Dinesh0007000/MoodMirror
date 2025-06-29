# 🎙️ MoodMirror – Talk to Your AI Friend in Any Mood & Language

MoodMirror is a multilingual, emotionally intelligent AI chatbot built using **Murf's Text-to-Speech API** and **OpenRouter's LLM**. You can talk to it in your preferred language and choose the personality of your virtual companion — from a supportive sister to a flirty boyfriend. It listens, responds emotionally, and speaks back to you in a realistic voice!

---

## 🔥 Live Demo

👉 [Click here to try the app](https://moodmirror-z5uq.onrender.com/)

---

## 💡 Features
```plaintext
- 🧑‍🤝‍🧑 **Choose Your Friend Type**: Brotherly friend, Sisterly friend, Boyfriend, or Girlfriend.
- 🗣️ **Multilingual Support**: English, Hindi, Tamil, and Bengali.
- 🎤 **Voice Output**: Powered by Murf AI's realistic TTS voices.
- ❤️ **Emotionally Intelligent**: Replies generated using OpenRouter LLM with context-based emotional tones.
- 🔁 **Real-time Interaction**: Dynamic voice playback and natural conversation flow.
```
---

## 🛠️ Tech Stack
```plaintext
| Layer       | Technology           |
|-------------|----------------------|
| Backend     | Python (Flask)       |
| AI Model    | OpenRouter (Mistral 7B) |
| TTS         | Murf AI              |
| Frontend    | HTML, CSS, JavaScript |
| Deployment  | [Render/Heroku/etc.] |
```
---

## 📸 Screenshots
![main_page_ui](main_page.png)
![user_request_page_ui](user_request_page.png)
![chatbot_response_page_ui](ui_response_page.png)

---

## 🚀 How to Run Locally
```plaintext
1. **Clone the repo**
   git clone https://github.com/yourusername/MoodMirror.git
   cd MoodMirror
Create a .env file
MURF_API_KEY=your_murf_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
Install dependencies

pip install -r requirements.txt
Run the app

python app.py
🧠 API Usage
Murf AI – used for real-time voice generation based on reply.

OpenRouter AI – used to create emotional replies based on user input and selected character type.
```

📂 Project Structure
```plaintext
MoodMirror/
│
├── static/
│   ├── avatars/
│   └── css/
├── templates/
│   ├── index.html
│   └── chat.html
├── app.py
├── requirements.txt
└── README.md
```

📎 License
MIT License. Feel free to fork, remix, and improve.

🙌 Credits
Built by Gavireddy Dinesh Karthik

Special thanks to Murf AI for the amazing APIs and opportunity 💙
 
## Tech Stack Badges
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Murf AI](https://img.shields.io/badge/Murf%20AI-TTS-blueviolet)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-informational)

