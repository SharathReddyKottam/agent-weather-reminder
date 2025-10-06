import os
import json
import datetime
from dotenv import load_dotenv
from openai import OpenAI
from weather_api import get_weather
from calendar_service import create_reminder_event

# Load environment variables
load_dotenv()

# Initialize OpenAI client (reads OPENAI_API_KEY from .env automatically)
client = OpenAI()


def parse_intent(user_input: str):
    """
    Try OpenAI for intent parsing.
    If OpenAI fails, fall back to a simple keyword-based parser.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # you can change to gpt-4o / gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "Extract city, date, and action as JSON."},
                {"role": "user", "content": user_input}
            ]
        )
        text = response.choices[0].message.content.strip()
        return json.loads(text)

    except Exception as e:
        print(f"[Warning] OpenAI failed, falling back to backup parser: {e}")

        # --- Extended backup parser (simple keyword matching) ---
        text = user_input.lower()
        if "virginia" in text:
            return {"city": "Virginia", "date": "tomorrow", "action": "check weather"}
        elif "new york" in text:
            return {"city": "New York", "date": "tomorrow", "action": "check weather"}
        elif "seattle" in text:
            return {"city": "Seattle", "date": "tomorrow", "action": "check weather"}
        elif "london" in text:
            return {"city": "London", "date": "tomorrow", "action": "check weather"}
        elif "mumbai" in text:
            return {"city": "Mumbai", "date": "tomorrow", "action": "check weather"}
        else:
            # Default fallback
            return {"city": "New York", "date": "tomorrow", "action": "check weather"}


def main():
    # Step 1: Take input
    user_input = input("Enter your request: ")

    # Step 2: Parse intent
    intent = parse_intent(user_input)
    print("\n[Intent Extraction]")
    print(intent)

    city = intent.get("city", "New York")
    date_requested = intent.get("date", "tomorrow")

    # Step 3: Get weather
    try:
        weather = get_weather(city)
        print(f"\n[Weather API] {city} → {weather['condition']} ({weather['temp']}°C)")
    except Exception as e:
        print(f"[Error] Could not fetch weather: {e}")
        return

    # Step 4: Reason & act
    if "Rain" in weather["condition"]:
        reminder_text = f"Carry umbrella {date_requested} in {city}."
        print("[Agent Decision] It's rainy! Creating Google Calendar event...")

        # Convert "tomorrow" into a date string
        if date_requested.lower() == "tomorrow":
            event_date = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
        else:
            # fallback = today
            event_date = datetime.date.today().isoformat()

        print(create_reminder_event(reminder_text, event_date, city))
    else:
        print(f"[Agent Decision] Weather looks {weather['condition']}. No reminder needed.")


if __name__ == "__main__":
    main()
