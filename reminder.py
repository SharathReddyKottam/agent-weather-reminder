def save_reminder(text: str):
    with open("reminders.txt", "a") as f:
        f.write(text + "\n")
    return f"Reminder saved: {text}"
