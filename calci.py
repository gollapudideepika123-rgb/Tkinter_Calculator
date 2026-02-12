import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear entry
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.configure(bg="navy blue")

expression = ""
equation = tk.StringVar()

# Entry box
entry = tk.Entry(root, textvariable=equation, font=("Arial", 18), bd=8, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, r, c) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=7, height=2, font=("Arial", 12),
                  command=equalpress, bg="orange", fg="white").grid(row=r, column=c)
    else:
        tk.Button(root, text=text, width=7, height=2, font=("Arial", 12),
                  command=lambda t=text: press(t)).grid(row=r, column=c)

# Clear button
tk.Button(root, text='C', width=30, height=2, font=("Arial", 12),
          command=clear, bg="pink", fg="white").grid(row=5, column=0, columnspan=4)

root.mainloop()
