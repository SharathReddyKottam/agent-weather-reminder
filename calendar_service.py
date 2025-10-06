from __future__ import print_function
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying SCOPES, delete the token.json file
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

def get_calendar_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service

def create_reminder_event(summary: str, date: str, city: str):
    """
    Creates a calendar event reminder.
    date should be in format YYYY-MM-DD
    """
    service = get_calendar_service()

    event = {
        "summary": summary,
        "location": city,
        "description": "Agentic AI Weather Reminder",
        "start": {
            "dateTime": f"{date}T09:00:00",
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": f"{date}T10:00:00",
            "timeZone": "America/New_York",
        },
    }

    event = service.events().insert(calendarId="primary", body=event).execute()
    return f"Event created: {event.get('htmlLink')}"
