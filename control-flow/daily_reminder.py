task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        print(" is a high priority task") 
    case "medium":
        print(" is a medium priority task") 
    case "low":
        print(" is a low priority task") 
    case _:
        print("has unknown priority") 

if time_bound == "yes":
    print (" that requires immediate attention today!")
else:
    print(" Consider completing it when you have free time.")


