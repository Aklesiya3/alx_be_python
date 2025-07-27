<<<<<<< HEAD
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = f"'{task}' has an unknown priority"
=======
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip()
time_bound = input("Is it time-bound? (yes/no): ").strip()

>>>>>>> ad98482c0c0062416a708129fda106cf45f21329
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
        else:
            print("please enter either (yes/no)!")
    case "low":
<<<<<<< HEAD
        reminder = f"'{task}' is a low priority task"
    case _:
        pass

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("\nReminder:", reminder)
=======
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("please enter either (yes/no)!")
>>>>>>> ad98482c0c0062416a708129fda106cf45f21329
