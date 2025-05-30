age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    if age > 0:
        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")
    else:
        print("Age must be greater than 0.")
else:
    print("Invalid input. Please enter a number.")
