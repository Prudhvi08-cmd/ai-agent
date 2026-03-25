from tools.calendar_tool import check_slot, book_slot, cancel_slot, next_available
from tools.notification_tool import notify

def execute(task, steps):
    action = task["action"]
    time = task.get("time", "10AM")

    for step in steps:

        if step == "check":
            if check_slot(time) == "booked":
                print(f"{time} not available")
                alt = next_available()
                if alt:
                    print(f"Try {alt}")
                return

            elif check_slot(time) == "invalid":
                print("Invalid time")
                return

        elif step == "book":
            if not book_slot(time):
                print("Booking failed")
                return

        elif step == "cancel":
            if not cancel_slot(time):
                print("Nothing to cancel")
                return

        elif step == "notify":
            notify(f"{action} completed at {time}")

    print("Task completed")
