import tkinter as tk
from backend import (
    button_clicked,
    calculate,
    clear,
    all_clear
)

# ==========================
# WINDOW
# ==========================

window = tk.Tk()
window.title("Calculator Version 2")
window.geometry("420x600")
window.resizable(False, False)

# ==========================
# HEADING
# ==========================

heading = tk.Label(
    window,
    text="Calculator Version 2 - Bhaskar",
    font=("Arial", 16, "bold")
)
heading.pack(pady=15, padx=4)

# ==========================
# DISPLAY
# ==========================

display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    width=18,
    bd=5
)
display.pack(pady=10, ipady=10)

# ==========================
# BUTTON FRAME
# ==========================

button_frame = tk.Frame(window)
button_frame.pack(pady=15)

# ==========================
# AC BUTTON
# ==========================

ac_button = tk.Button(
    button_frame,
    text="AC",
    font=("Arial", 16),
    width=22,
    height=2,
    command=lambda: all_clear(display)
)

ac_button.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=5
)

# ==========================
# BUTTON LAYOUT
# ==========================

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# ==========================
# CREATE BUTTONS
# ==========================

for row in range(len(buttons)):
    for col in range(len(buttons[row])):

        value = buttons[row][col]

        if value == "=":
            command = lambda: calculate(display)

        elif value == "C":
            command = lambda: clear(display)

        else:
            command = lambda value=value: button_clicked(display, value)

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 16),
            width=5,
            height=2,
            command=command
        )

        button.grid(
            row=row + 1,
            column=col,
            padx=5,
            pady=5
        )

# ==========================
# START APPLICATION
# ==========================

window.mainloop()