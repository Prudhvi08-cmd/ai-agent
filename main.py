from core.interpreter import interpret
from core.planner import plan
from core.executor import execute

def main():
    print("AI Agent Ready (type 'exit')")

    while True:
        user_input = input("\nEnter task: ")

        if user_input.lower() == "exit":
            break

        task = interpret(user_input)

        if task.get("action") == "unknown":
            print("Invalid input. Try again.")
            continue

        steps = plan(task)
        execute(task, steps)

if __name__ == "__main__":
    main()
