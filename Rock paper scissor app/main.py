import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

def get_computer_choice():
    """Randomly select 'rock', 'paper', or 'scissors' for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    """Main game function called by buttons."""
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
    result_label.config(text=f"Result: {result}")

user_choice_label = tk.Label(root, text="Your choice: None", font=("Helvetica", 12))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer's choice: None", font=("Helvetica", 12))
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Result: Make a choice to play!", font=("Helvetica", 14, "bold"), fg="blue")
result_label.pack(pady=20)


button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play_game('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play_game('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play_game('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

root.mainloop()