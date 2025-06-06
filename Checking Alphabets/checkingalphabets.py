#START
char = input("Enter any character: ")

if len(char) == 1:

    if char.isalpha():
        print("Yes, it's an alphabet.")
    else:
        print("No, it's not an alphabet.")
else:
    print("Please enter only one character.")
#END