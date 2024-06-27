# promt for a single task
task = input("Enter your task: ")

# prompt for the task's priority
priority = input("priority (high/medium/low): ").lower()

# Prompt for time insensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# process the task based on priority and time sensitivity
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task."
    case 'medium':
        reminder = f"'{task}' is a medium priority task."
    case 'low':
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' unknown priority level."
# Mosify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += " consider completing it when you have free time."

# provide the customized reminder
print("Reminder:", reminder)


