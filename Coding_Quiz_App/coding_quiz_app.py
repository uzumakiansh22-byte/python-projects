import json
import os
import random
import tkinter as tk
from tkinter import messagebox


QUESTIONS_FILE = "questions.json"
QUESTION_LIMIT = 10
TIME_PER_QUESTION = 15


class CodingQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coding Quiz App")
        self.root.geometry("640x430")
        self.root.resizable(False, False)

        self.all_questions = self.load_questions()
        self.selected_language = ""
        self.quiz_questions = []
        self.current_index = 0
        self.score = 0
        self.time_left = TIME_PER_QUESTION
        self.timer_id = None

        self.show_language_screen()

    def get_questions_path(self):
        return os.path.join(os.path.dirname(__file__), QUESTIONS_FILE)

    def load_questions(self):
        """Read static questions from questions.json."""
        try:
            with open(self.get_questions_path(), "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            messagebox.showerror("File Missing", "questions.json was not found.")
        except json.JSONDecodeError:
            messagebox.showerror("File Error", "questions.json is not valid JSON.")
        return {}

    def clear_window(self):
        """Remove all widgets before drawing a new screen."""
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        for widget in self.root.winfo_children():
            widget.destroy()

    def show_language_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Choose a Coding Language", font=("Arial", 17, "bold")).pack(pady=20)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        languages = ["Python", "C", "C++", "Java", "JavaScript", "HTML"]
        for index, language in enumerate(languages):
            button = tk.Button(
                button_frame,
                text=language,
                width=16,
                height=2,
                command=lambda selected=language: self.start_quiz(selected),
            )
            button.grid(row=index // 2, column=index % 2, padx=10, pady=8)

    def start_quiz(self, language):
        available_questions = self.all_questions.get(language, [])

        if len(available_questions) < QUESTION_LIMIT:
            messagebox.showerror("Not Enough Questions", "Not enough questions available for this language.")
            return

        self.selected_language = language
        self.quiz_questions = random.sample(available_questions, QUESTION_LIMIT)
        self.current_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_window()

        if self.current_index >= len(self.quiz_questions):
            self.show_end_screen()
            return

        self.time_left = TIME_PER_QUESTION
        question_data = self.quiz_questions[self.current_index]

        top_frame = tk.Frame(self.root)
        top_frame.pack(fill="x", padx=20, pady=10)

        self.progress_label = tk.Label(top_frame, text=f"{self.current_index + 1}/{QUESTION_LIMIT}", font=("Arial", 11, "bold"))
        self.progress_label.pack(side=tk.LEFT)

        self.score_label = tk.Label(top_frame, text=f"Score: {self.score}", font=("Arial", 11, "bold"))
        self.score_label.pack(side=tk.LEFT, padx=190)

        self.timer_label = tk.Label(top_frame, text=f"Time: {self.time_left}", font=("Arial", 11, "bold"))
        self.timer_label.pack(side=tk.RIGHT)

        tk.Label(self.root, text=self.selected_language, font=("Arial", 13, "bold")).pack(pady=5)

        question_label = tk.Label(
            self.root,
            text=question_data["question"],
            font=("Arial", 13),
            wraplength=560,
            justify="center",
        )
        question_label.pack(pady=20)

        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=8)

        for option in question_data["options"]:
            button = tk.Button(
                options_frame,
                text=option,
                width=45,
                command=lambda selected=option: self.check_answer(selected),
            )
            button.pack(pady=5)

        self.update_timer()

    def update_timer(self):
        """Count down without freezing the Tkinter window."""
        self.timer_label.config(text=f"Time: {self.time_left}")

        if self.time_left <= 0:
            self.current_index += 1
            self.show_question()
            return

        self.time_left -= 1
        self.timer_id = self.root.after(1000, self.update_timer)

    def check_answer(self, selected_answer):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        correct_answer = self.quiz_questions[self.current_index]["answer"]
        if selected_answer == correct_answer:
            self.score += 1

        self.current_index += 1
        self.show_question()

    def show_end_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Quiz Complete", font=("Arial", 18, "bold")).pack(pady=35)
        tk.Label(self.root, text=f"Final Score: {self.score} out of {QUESTION_LIMIT}", font=("Arial", 15)).pack(pady=20)
        tk.Button(self.root, text="Restart Quiz", width=16, command=self.show_language_screen).pack(pady=15)


if __name__ == "__main__":
    window = tk.Tk()
    app = CodingQuizApp(window)
    window.mainloop()
