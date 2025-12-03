import tkinter as tk

def main():

    root = tk.Tk()
    root.title("Password Strength Checker")
    root.geometry("400x400")
    
    root.mainloop()

if __name__ == "__main__":
    main()

def check_password_strength(password):
    length = len(password)
    if length <= 5:
        return "Weak", "red"
    elif 6 <= length <= 8:
        return "Medium", "yellow"
    elif length > 12:
        return "Very Strong", "dark green"
    elif length > 8:
        return "Strong", "light green"
    else:
        return "Unknown", "black"



import tkinter as tk

def check_strength():
    password = entry.get()
    strength, color = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}", foreground=color)

def check_password_strength(password):
    length = len(password)
    if length <= 5:
        return "Weak", "red"
    elif 6 <= length <= 8:
        return "Medium", "yellow"
    elif length > 12:
        return "Very Strong", "dark green"
    elif length > 8:
        return "Strong", "light green"
    else:
        return "Unknown", "black"

def main():
    global entry, result_label
    root = tk.Tk()
    root.title("Length Converter App")
    root.geometry("400x400")

    label = tk.Label(root, text="Enter Password:")
    label.pack(pady=10)

    entry = tk.Entry(root, show="*")
    entry.pack(pady=5)

    button = tk.Button(root, text="Check Strength", command=check_strength)
    button.pack(pady=10)

    result_label = tk.Label(root, text="Strength: N/A", font=("Helvetica", 12, "bold"))
    result_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()