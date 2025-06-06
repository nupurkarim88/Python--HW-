# START
def shutdown(command):
    if command == "yes":
        return "Shutting down..."
    elif command == "no":
        return "Shutdown cancelled."
    else:
        return "Sorry, I didn't understand."
result = shutdown(input("Do you want to shutdown the computer? (yes/no): "))
print(result)
print(result)
#END