import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from functools import partial

# Function to determine winner
def determine_winner(user_choice):
    """
    Determine the winner of the game based on the user's and computer's choices.
    Display the images of the choices and the result.
    Args:
        user_choice (str): The user's choice.
    """

    choices = ['sang', 'kagaz', 'ghychi']
    computer_choice = random.choice(choices)

    # Load images
    user_img = Image.open(f"{user_choice}.png")
    computer_img = Image.open(f"{computer_choice}.png")
    user_img = user_img.resize((100, 100))
    computer_img = computer_img.resize((100, 100))
    user_img = ImageTk.PhotoImage(user_img)
    computer_img = ImageTk.PhotoImage(computer_img)

    user_label.configure(image=user_img)
    user_label.image = user_img
    computer_label.configure(image=computer_img)
    computer_label.image = computer_img

    # Determine winner
    if user_choice == computer_choice:
        messagebox.showinfo("Result", "mosavi!")
    elif (user_choice == 'sang' and computer_choice == 'ghychi') or \
         (user_choice == 'kagaz' and computer_choice == 'sang') or \
         (user_choice == 'ghychi' and computer_choice == 'kagaz'):
        messagebox.showinfo("Result", f"shoma bordi! {user_choice} mizand {computer_choice}")
    else:
        messagebox.showinfo("Result", f"shoma bkhti! {computer_choice} mizand {user_choice}")

    result_text = f"You chose {user_choice}, computer chose {computer_choice} {result_label}"
    result_label.config(text=result_text)
# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors GUI Images")

# Load images
rock_img = Image.open("sang.png")
paper_img = Image.open("kagaz.png")
scissors_img = Image.open("ghychi.png")
rock_img = rock_img.resize((100, 100))
paper_img = paper_img.resize((100, 100))
scissors_img = scissors_img.resize((100, 100))
rock_img = ImageTk.PhotoImage(rock_img)
paper_img = ImageTk.PhotoImage(paper_img)
scissors_img = ImageTk.PhotoImage(scissors_img)

# Labels for images
user_label = tk.Label(root, image=rock_img)
computer_label = tk.Label(root, image=rock_img)
user_label.grid(row=0, column=0)
computer_label.grid(row=0, column=1)

# Buttons for user choice
rock_button = tk.Button(root, image=rock_img, command=lambda: determine_winner('sang'))
paper_button = tk.Button(root, image=paper_img, command=lambda: determine_winner('kagaz'))
scissors_button = tk.Button(root, image=scissors_img, command=lambda: determine_winner('ghychi'))
rock_button.grid(row=1, column=0)
paper_button.grid(row=1, column=1)
scissors_button.grid(row=1, column=2)

# Result label
result_text = "..."
result_label = tk.Label(root, text=result_text)
result_label.grid(row=2, column=0, columnspan=3)

# Quit button
quit_button = tk.Button(root, text="QUIT", command=root.quit)
quit_button.grid(row=3, column=0, columnspan=3)
# Start the application

root.mainloop()
