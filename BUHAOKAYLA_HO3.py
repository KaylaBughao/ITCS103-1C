import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x200")
window.configure(bg="#a8c6cf")

def calculate(operator):
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    if operator == "+":
        result = num1 + num2
        text = f"The sum is of {num1} + {num2} is {result}."
    elif operator == "-":
        result = num1 - num2
        text = f"The difference of {num1} - {num2} is {result}."
    elif operator == "*":
        result = num1 * num2
        text = f"The product of {num1} * {num2} is {result}."
    elif operator == "/":
        result = num1 / num2
        text = f"The division of {num1} / {num2} is {result}."

    result_label.config(text=text)

result_label = tk.Label(window, text="Result will appear here", bg="#a8c6cf", font=("Arial", 10))
result_label.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(window, text="Enter 1st Number:", bg="#a8c6cf").grid(row=1, column=0, padx=10, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=1, column=1)

tk.Label(window, text="Enter 2nd Number:", bg="#a8c6cf").grid(row=2, column=0, padx=10, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=2, column=1)

tk.Button(window, text="Add", width=10, command=lambda: calculate("+")).grid(row=3, column=0, pady=5)
tk.Button(window, text="Subtract", width=10, command=lambda: calculate("-")).grid(row=3, column=1)

tk.Button(window, text="Multiply", width=10, command=lambda: calculate("*")).grid(row=4, column=0, pady=5)
tk.Button(window, text="Division", width=10, command=lambda: calculate("/")).grid(row=4, column=1)

window.mainloop()