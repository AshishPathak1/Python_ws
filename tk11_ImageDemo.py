import tkinter as tk
from tkinter import PhotoImage

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.operand1_var = tk.StringVar()
        self.operand2_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.entry_operand1 = tk.Entry(root, textvariable=self.operand1_var, width=10, font=("Helvetica", 16))
        self.entry_operand2 = tk.Entry(root, textvariable=self.operand2_var, width=10, font=("Helvetica", 16))
        self.entry_result = tk.Entry(root, textvariable=self.result_var, width=10, font=("Helvetica", 16))

        self.entry_operand1.grid(row=0, column=0, padx=5, pady=5)
        self.entry_operand2.grid(row=0, column=1, padx=5, pady=5)
        self.entry_result.grid(row=0, column=2, padx=5, pady=5)

        self.img_add = PhotoImage(file="add.png")
        self.img_subtract = PhotoImage(file="subtract.png")
        self.img_multiply = PhotoImage(file="multiply.png")
        self.img_divide = PhotoImage(file="divide.png")

        tk.Button(root, image=self.img_add, command=self.add, padx=20, pady=20).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(root, image=self.img_subtract, command=self.subtract, padx=20, pady=20).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(root, image=self.img_multiply, command=self.multiply, padx=20, pady=20).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(root, image=self.img_divide, command=self.divide, padx=20, pady=20).grid(row=1, column=3, padx=5, pady=5)

    def add(self):
        self.perform_operation('+')

    def subtract(self):
        self.perform_operation('-')

    def multiply(self):
        self.perform_operation('*')

    def divide(self):
        self.perform_operation('/')

    def perform_operation(self, operator):
        try:
            operand1 = float(self.operand1_var.get())
            operand2 = float(self.operand2_var.get())
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                if operand2 != 0:
                    result = operand1 / operand2
                else:
                    result = "Error (Divide by zero)"
            else:
                result = "Error (Invalid operator)"

            self.result_var = (str(result))
        except Exception as e:
            print(f"Exception: {type(e).__name__}: {str(e)}")
            self.result_var = ("Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
