import re

def extract_time(text):
    match = re.search(r'(\d{1,2})(am|pm)', text.lower())
    if match:
        return f"{int(match.group(1))}{match.group(2).upper()}"
    return None

def interpret(user_input):
    text = user_input.lower()
    time = extract_time(text) or "10AM"

    if "cancel" in text:
        return {"action": "cancel", "time": time}

    if "reschedule" in text or "move" in text:
        return {"action": "reschedule", "old": "10AM", "new": "11AM"}

    if "free" in text or "availability" in text:
        return {"action": "check", "time": time}

    if "notify" in text:
        return {"action": "notify", "message": "Team update"}

    if "schedule" in text or "meeting" in text:
        return {"action": "schedule", "time": time}

    return {"action": "unknown"}
