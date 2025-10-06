# 🌦️ Agentic Weather Reminder  
> An intelligent AI agent that checks your forecast and reminds you when to grab your umbrella ☂️  

---

![Python](https://img.shields.io/badge/Python-3.13-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-orange)
![Google-Calendar](https://img.shields.io/badge/Google-Calendar%20API-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 💡 Why I Built This
This project started as an exploration of **Agentic AI** — building systems that can *act* on data instead of just analyzing it.  
I wanted to make something practical, simple, and relatable — so I built an agent that helps you **avoid getting caught in the rain** 🌧️.  

---

## ✨ Features
- 🗣️ Natural language input — *“Check tomorrow’s weather in Seattle and remind me if I need an umbrella”*  
- 🧠 Uses **OpenAI** to extract intent (city, date, and action)  
- 🪄 Fallback parser for offline or quota-limited scenarios  
- 🌤️ Fetches live weather data via OpenWeatherMap API  
- 📅 Creates calendar reminders through Google Calendar API  

---

## 🧠 Tech Stack
- 🐍 **Python 3.13**
- 🧠 **OpenAI GPT-4o**
- 🌦️ **OpenWeatherMap API**
- 📅 **Google Calendar API (OAuth 2.0)**
- 🔐 **python-dotenv** for managing environment variables
- ☁️ **Requests / Google API Client**

---

## 🧩 How It Works
```text
User Input ─► OpenAI (Intent Parsing)
             │
             ├──► Weather API (Get Forecast)
             │
             ├──► Decision Engine (Check for Rain)
             │
             └──► Google Calendar (Create Reminder)

⚙️ Setup Instructions

1. Clone the repo

git clone https://github.com/SharathReddyKottam/agent-weather-reminder.git
cd agent-weather-reminder

2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Environment variables

Copy .env.example → .env and add your keys:
OPENAI_API_KEY=your_openai_api_key_here
SIMULATE_RAIN=false

5. Google Calendar API setup

Go to Google Cloud Console → APIs & Services → Library and enable Google Calendar API.
Create OAuth 2.0 Web Client ID credentials.
Download the JSON and save it as credentials.json in your project folder.
Add your Gmail under OAuth Consent Screen → Test Users.
When you first run, a browser window will open for authentication.
(The repo includes credentials.json.example for reference — don’t share your real one!)

🚀 Usage

Run the agent:

-python agent.py

Example input:

-check tomorrow's weather in London and remind me if I need an umbrella

Example output:

[Intent Extraction]
{"city": "London", "date": "tomorrow", "action": "check weather"}

[Weather API] London → Rain (17.2°C)
[Agent Decision] It's rainy! Creating Google Calendar event...
Event created: https://calendar.google.com/calendar/event?eid=xxxx


📂 Project Structure:

agent-weather-reminder/
│── agent.py
│── weather_api.py
│── calendar_service.py
│── reminder.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example
│── credentials.json.example

⚠️ Notes

Don’t upload your real .env or credentials.json to GitHub.

If Google shows “App not verified”, that’s normal in Testing mode.
Just click Advanced → Continue for personal use.

📰 Read the Full Story

I’ve documented the full build process, challenges, and alternate LLM integrations in my Medium article:
👉 Building an Agentic AI: The Weather Reminder Project


📝 License

This project is licensed under the MIT License