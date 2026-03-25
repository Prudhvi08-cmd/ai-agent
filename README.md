# 🤖 Autonomous Multi-Step AI Agent

---

## 📌 Overview

This project implements an **Autonomous Multi-Step Agent** that can:

* Understand user tasks
* Break them into steps
* Execute them using tools

It simulates real-world workflow automation such as:

* Scheduling meetings
* Checking availability
* Cancelling meetings
* Sending notifications

---

## 🚀 Features

* Multi-step task execution
* Tool-based architecture
* Dynamic time slots (10AM–5PM)
* Conflict detection and suggestions
* Multi-task handling
* Input validation
* Continuous execution (loop-based system)

---

## 🧠 Architecture

```
User Input
   ↓
Interpreter
   ↓
Planner
   ↓
Executor
   ↓
Tools (Calendar / Notification)
   ↓
Output
```

---

## ⚙️ Tech Stack

* Python
* Modular architecture
* Git & GitHub

---

## 📁 Project Structure

```
ai-agent/
│
├── core/
│   ├── interpreter.py
│   ├── planner.py
│   ├── executor.py
│
├── tools/
│   ├── calendar_tool.py
│   ├── notification_tool.py
│
├── utils/
│   ├── logger.py
│
├── main.py
└── README.md
```

---

## 🧪 Example Usage

### Input

```
Schedule meeting at 10AM and notify team
```

### Output

```
[Step] Checking availability...
[Step] Booking meeting...
Booked 10AM
[NOTIFICATION] schedule completed at 10AM
```

---

## ⚠️ Conflict Case

### Input

```
Schedule meeting at 10AM
Schedule meeting at 10AM
```

### Output

```
10AM not available
Try 11AM
```

---

## 🔄 Supported Tasks

* Schedule meeting
* Cancel meeting
* Check availability
* Send notification
* Reschedule meeting

---

## ⚠️ Note

This project currently uses a **rule-based interpreter** for reliability.
It is designed to integrate **AI models (LLMs)** for advanced understanding.

---

## 🎯 Future Improvements

* Add AI (Gemini / OpenAI)
* Real email integration
* Database support
* UI dashboard

---

## 👨‍💻 Author

Prudhvi
