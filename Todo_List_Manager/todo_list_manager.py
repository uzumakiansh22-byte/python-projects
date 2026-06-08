import json
import os
import tkinter as tk
from tkinter import messagebox


TASKS_FILE = "tasks.json"


class TodoListManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List Manager")
        self.root.geometry("420x360")
        self.root.resizable(False, False)

        self.tasks = []

        tk.Label(root, text="Todo List Manager", font=("Arial", 15, "bold")).pack(pady=10)

        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)

        self.task_entry = tk.Entry(input_frame, width=32, font=("Arial", 11))
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(input_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 10))
        self.task_listbox.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        self.complete_button = tk.Button(button_frame, text="Mark Complete", width=15, command=self.mark_complete)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete Task", width=15, command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.load_tasks()
        self.refresh_listbox()

    def get_tasks_path(self):
        """Use the tasks.json file stored beside this Python file."""
        return os.path.join(os.path.dirname(__file__), TASKS_FILE)

    def load_tasks(self):
        """Load saved tasks when the app starts."""
        try:
            with open(self.get_tasks_path(), "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
            self.save_tasks()
        except json.JSONDecodeError:
            messagebox.showerror("File Error", "tasks.json is not valid JSON. Starting with an empty list.")
            self.tasks = []

    def save_tasks(self):
        """Save tasks automatically after each change."""
        try:
            with open(self.get_tasks_path(), "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=4)
        except OSError:
            messagebox.showerror("Save Error", "Could not save tasks.json.")

    def refresh_listbox(self):
        """Show all tasks in the Listbox."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Pending"
            self.task_listbox.insert(tk.END, f"[{status}] {task['text']}")

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showerror("Invalid Task", "Please type a task before adding it.")
            return

        self.tasks.append({"text": task_text, "completed": False})
        self.task_entry.delete(0, tk.END)
        self.save_tasks()
        self.refresh_listbox()

    def get_selected_index(self):
        """Return the selected Listbox index, or None if nothing is selected."""
        try:
            return self.task_listbox.curselection()[0]
        except IndexError:
            messagebox.showerror("No Selection", "Please select a task first.")
            return None

    def mark_complete(self):
        selected_index = self.get_selected_index()
        if selected_index is None:
            return

        self.tasks[selected_index]["completed"] = True
        self.save_tasks()
        self.refresh_listbox()

    def delete_task(self):
        selected_index = self.get_selected_index()
        if selected_index is None:
            return

        del self.tasks[selected_index]
        self.save_tasks()
        self.refresh_listbox()


if __name__ == "__main__":
    window = tk.Tk()
    app = TodoListManager(window)
    window.mainloop()
