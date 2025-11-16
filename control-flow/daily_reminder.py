while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ("high", "medium", "low"):
        break
    print("Invalid priority. Please enter high, medium, or low.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ("yes", "no"):
        break
    print("Please answer yes or no.")

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unspecified priority"

if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = "Note: " + message + ". Consider completing it when you have free time."

print("\nReminder:", message)
