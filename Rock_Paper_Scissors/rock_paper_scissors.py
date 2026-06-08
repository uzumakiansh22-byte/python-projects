import random
import tkinter as tk


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("420x330")
        self.root.resizable(False, False)

        self.user_score = 0
        self.computer_score = 0
        self.tie_count = 0
        self.choices = ["Rock", "Paper", "Scissors"]

        tk.Label(root, text="Rock Paper Scissors", font=("Arial", 15, "bold")).pack(pady=12)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=8)

        for choice in self.choices:
            tk.Button(button_frame, text=choice, width=11, command=lambda selected=choice: self.play_round(selected)).pack(side=tk.LEFT, padx=5)

        self.user_choice_label = tk.Label(root, text="Your choice: ", font=("Arial", 11))
        self.user_choice_label.pack(pady=5)

        self.computer_choice_label = tk.Label(root, text="Computer choice: ", font=("Arial", 11))
        self.computer_choice_label.pack(pady=5)

        self.winner_label = tk.Label(root, text="Winner: ", font=("Arial", 12, "bold"))
        self.winner_label.pack(pady=8)

        self.score_label = tk.Label(root, text="", font=("Arial", 11))
        self.score_label.pack(pady=8)

        tk.Button(root, text="Reset Score", width=14, command=self.reset_score).pack(pady=8)

        self.update_score_label()

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)
        winner = self.find_winner(user_choice, computer_choice)

        if winner == "You win":
            self.user_score += 1
        elif winner == "Computer wins":
            self.computer_score += 1
        else:
            self.tie_count += 1

        self.user_choice_label.config(text=f"Your choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer choice: {computer_choice}")
        self.winner_label.config(text=f"Winner: {winner}")
        self.update_score_label()

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"

        if (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            return "You win"

        return "Computer wins"

    def update_score_label(self):
        self.score_label.config(
            text=f"Your Score: {self.user_score}    Computer Score: {self.computer_score}    Ties: {self.tie_count}"
        )

    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.tie_count = 0
        self.user_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer choice: ")
        self.winner_label.config(text="Winner: ")
        self.update_score_label()


if __name__ == "__main__":
    window = tk.Tk()
    app = RockPaperScissors(window)
    window.mainloop()
