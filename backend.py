


def button_clicked(display, value):
    display.insert("end", value)

def all_clear(display):
    display.delete("0", "end")

def clear(display):
    current = display.get()

    if len(current) > 0:
        display.delete(len(current)-1, "end")

def calculate(display):
    expression = display.get()

    try:
        result = eval(expression)

        display.delete(0, "end")
        display.insert(0, result)

    except:
        display.delete(0, "end")
        display.insert(0, "Error")




