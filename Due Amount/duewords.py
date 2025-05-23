def check_age():
    age_input = input("Please enter your age: ")

    if not age_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

    age = int(age_input)

    if age < 0 or age > 120:
        print("The age entered seems incorrect. Please enter a valid age between 0 and 120.")
        return

    if age % 2 == 0:
        print(f"The age {age} is even.")
    else:
        print(f"The age {age} is odd.")

check_age()
