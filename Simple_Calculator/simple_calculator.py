import tkinter as tk
from tkinter import messagebox


class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("360x300")
        self.root.resizable(False, False)

        tk.Label(root, text="Simple Calculator", font=("Arial", 15, "bold")).pack(pady=12)

        tk.Label(root, text="First Number").pack()
        self.first_entry = tk.Entry(root, font=("Arial", 11), justify="center")
        self.first_entry.pack(pady=4)

        tk.Label(root, text="Second Number").pack()
        self.second_entry = tk.Entry(root, font=("Arial", 11), justify="center")
        self.second_entry.pack(pady=4)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=12)

        tk.Button(button_frame, text="Add", width=10, command=lambda: self.calculate("add")).grid(row=0, column=0, padx=4, pady=4)
        tk.Button(button_frame, text="Subtract", width=10, command=lambda: self.calculate("subtract")).grid(row=0, column=1, padx=4, pady=4)
        tk.Button(button_frame, text="Multiply", width=10, command=lambda: self.calculate("multiply")).grid(row=1, column=0, padx=4, pady=4)
        tk.Button(button_frame, text="Divide", width=10, command=lambda: self.calculate("divide")).grid(row=1, column=1, padx=4, pady=4)

        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=8)

        tk.Button(root, text="Clear", width=12, command=self.clear_fields).pack()

    def get_numbers(self):
        """Read and validate both number fields."""
        try:
            first_number = float(self.first_entry.get())
            second_number = float(self.second_entry.get())
            return first_number, second_number
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")
            return None, None

    def calculate(self, operation):
        first_number, second_number = self.get_numbers()
        if first_number is None or second_number is None:
            return

        if operation == "add":
            result = first_number + second_number
        elif operation == "subtract":
            result = first_number - second_number
        elif operation == "multiply":
            result = first_number * second_number
        elif operation == "divide":
            if second_number == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
                return
            result = first_number / second_number
        else:
            messagebox.showerror("Error", "Unknown operation.")
            return

        self.result_label.config(text=f"Result: {result}")

    def clear_fields(self):
        self.first_entry.delete(0, tk.END)
        self.second_entry.delete(0, tk.END)
        self.result_label.config(text="Result: ")


if __name__ == "__main__":
    window = tk.Tk()
    app = SimpleCalculator(window)
    window.mainloop()
