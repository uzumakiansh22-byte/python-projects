import random
import tkinter as tk
from tkinter import messagebox


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("360x260")
        self.root.resizable(False, False)

        self.secret_number = 0
        self.attempts = 0

        self.title_label = tk.Label(root, text="Guess a number from 1 to 100", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=15)

        self.guess_entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.guess_entry.pack(pady=5)

        self.check_button = tk.Button(root, text="Check Guess", width=16, command=self.check_guess)
        self.check_button.pack(pady=8)

        self.result_label = tk.Label(root, text="Enter your first guess.", font=("Arial", 12))
        self.result_label.pack(pady=5)

        self.attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 11))
        self.attempts_label.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset / New Game", width=16, command=self.new_game)
        self.reset_button.pack(pady=10)

        self.new_game()

    def new_game(self):
        """Start a fresh game with a new random number."""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="Enter your first guess.")
        self.attempts_label.config(text="Attempts: 0")
        self.check_button.config(state=tk.NORMAL)

    def check_guess(self):
        """Validate the guess and compare it with the secret number."""
        try:
            guess = int(self.guess_entry.get())
            if guess < 1 or guess > 100:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a whole number from 1 to 100.")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            self.result_label.config(text="Too Low")
        elif guess > self.secret_number:
            self.result_label.config(text="Too High")
        else:
            self.result_label.config(text="Correct")
            messagebox.showinfo("You Won", f"Correct! You guessed it in {self.attempts} attempts.")
            self.check_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    window = tk.Tk()
    app = NumberGuessingGame(window)
    window.mainloop()
