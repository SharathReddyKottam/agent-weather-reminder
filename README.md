🌦️ Agentic Weather Reminder

An AI-powered weather assistant that checks the forecast and creates reminders in Google Calendar when you need to carry an umbrella.
Built with Python, OpenAI, and Google Calendar API.

✨ Features

Natural language input → “Check tomorrow’s weather in Seattle and remind me if I need an umbrella”

Uses OpenAI to parse intent (city, date, action)

Fallback parser (works without AI)

Fetches live weather data

Creates reminders in your Google Calendar

🛠️ Setup

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
5. Google Calendar setup

In Google Cloud Console, enable Calendar API.

Create OAuth Web client ID credentials.

Download the JSON and save as credentials.json (your own, don’t share).

Add your Gmail as a Test user in the OAuth consent screen.

For repo safety, this project includes credentials.json.example as a template.

🚀 Usage

Run the agent:
python agent.py

Example input:
check tomorrow's weather in London and remind me if I need an umbrella

If it’s rainy, you’ll see:
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

📝 License

MIT License. Free to use and modify.