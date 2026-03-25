calendar = {}

def init_calendar():
    for h in range(10, 18):
        if h < 12:
            t = f"{h}AM"
        elif h == 12:
            t = "12PM"
        else:
            t = f"{h-12}PM"
        calendar[t] = "free"

init_calendar()

def check_slot(time):
    return calendar.get(time, "invalid")

def book_slot(time):
    if calendar.get(time) == "free":
        calendar[time] = "booked"
        print(f"Booked {time}")
        return True
    return False

def cancel_slot(time):
    if calendar.get(time) == "booked":
        calendar[time] = "free"
        print(f"Cancelled {time}")
        return True
    return False

def next_available():
    for t, s in calendar.items():
        if s == "free":
            return t
    return None
