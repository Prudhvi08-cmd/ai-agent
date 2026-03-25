def plan(task):
    action = task["action"]

    plans = {
        "schedule": ["check", "book", "notify"],
        "cancel": ["cancel", "notify"],
        "check": ["check"],
        "notify": ["notify"],
        "reschedule": ["cancel", "check", "book", "notify"]
    }

    return plans.get(action, [])
