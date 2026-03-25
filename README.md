🤖 Autonomous Multi-Step AI Agent
📌 Overview

This project implements an Autonomous Multi-Step Agent capable of interpreting user tasks, breaking them into multiple steps, and executing them using tool-based architecture.

The system simulates real-world workflow automation such as scheduling meetings, checking availability, cancelling, and sending notifications.

🚀 Features
✅ Multi-step task execution
✅ Tool-based architecture (Calendar & Notification)
✅ Dynamic time slot management (10AM–5PM)
✅ Conflict detection and alternative suggestions
✅ Multi-task handling (e.g., "schedule meeting and notify team")
✅ Input validation and error handling
✅ Continuous interaction (loop-based execution)
🧠 How It Works

The system follows a modular pipeline:

User Input → Interpreter → Planner → Executor → Tools → Output

Components:
Interpreter: Extracts intent and entities (time, action)
Planner: Converts task into executable steps
Executor: Executes steps sequentially
Tools:
Calendar Tool (check, book, cancel)
Notification Tool (mock email)
⚙️ Tech Stack
Python
Modular architecture (core, tools, utils)
Git & GitHub
📁 Project Structure
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
🧪 Example Usage
Input:
Schedule meeting at 10AM and notify team
Output:
[Step] Checking availability...
[Step] Booking meeting...
Booked 10AM
[NOTIFICATION] schedule completed at 10AM
Conflict Case:
Schedule meeting at 10AM
Schedule meeting at 10AM

Output:

10AM not available
Try 11AM
🔄 Supported Tasks
Schedule meeting
Cancel meeting
Check availability
Send notification
Reschedule meeting
⚠️ Note

This project uses a rule-based interpreter for reliability.
The architecture is designed to integrate AI models (LLMs) for enhanced natural language understanding.

🎯 Future Improvements
Integration with LLMs (Gemini / OpenAI)
Real email API integration
Database for persistent storage
UI Dashboard
👨‍💻 Author

Prudhvi
