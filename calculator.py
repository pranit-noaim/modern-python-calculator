import tkinter as tk

# ---------------- Window ---------------- #

root = tk.Tk()
root.title("Modern Python Calculator")
root.geometry("360x550")
root.resizable(False, False)
root.configure(bg="#1f1f1f")

expression = ""


# ---------------- Functions ---------------- #

def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""


# ---------------- Display ---------------- #

equation = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=equation,
    font=("Segoe UI", 24),
    justify="right",
    bd=0,
    bg="#2d2d2d",
    fg="white"
)

display.pack(fill="both", padx=15, pady=20, ipady=20)


# ---------------- Buttons ---------------- #

frame = tk.Frame(root, bg="#1f1f1f")
frame.pack(expand=True, fill="both")

buttons = [
    ["C", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "":
            continue

        if text == "=":
            command = equal
        elif text == "C":
            command = clear
        elif text == "⌫":
            command = delete
        else:
            command = lambda x=text: press(x)

        button = tk.Button(
            frame,
            text=text,
            font=("Segoe UI", 18),
            bg="#3b3b3b",
            fg="white",
            bd=0,
            activebackground="#505050",
            activeforeground="white",
            command=command
        )

        button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

for i in range(5):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

root.mainloop()
