age = str(input("Are you a cigarette addict older than 75 years old? (Yes/No): ")) 

chronic = str(input("Do you have a severe chronic disease? (Yes/No): "))

immune = str(input("Is your immune system too weak? (Yes/No):"))

if (age and chronic and immune).title().strip() == "Yes":
    print("You are in risky group")
else:
    print("You are not in risky group")