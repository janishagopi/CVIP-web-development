import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Calculator")
window.geometry("570x600+100+200")
window.resizable(False, False)
window.configure(bg="black")

# Setting the initial values 
var = ""
A = 0
operator = ""

def number_1():
    global var
    var = var + "1"
    the_data.set(var)

def number_2():
    global var
    var = var + "2"
    the_data.set(var)

def number_3():
    global var
    var = var + "3"
    the_data.set(var)

def number_4():
    global var
    var = var + "4"
    the_data.set(var)

def number_5():
    global var
    var = var + "5"
    the_data.set(var)

def number_6():
    global var
    var = var + "6"
    the_data.set(var)

def number_7():
    global var
    var = var + "7"
    the_data.set(var)

def number_8():
    global var
    var = var + "8"
    the_data.set(var)

def number_9():
    global var
    var = var + "9"
    the_data.set(var)

def number_0():
    global var
    var = var + "0"
    the_data.set(var)

def add():
    global A, var, operator
    A = float(var)
    operator = "+"
    var = var + "+"
    the_data.set(var)

def sub():
    global A, var, operator
    A = float(var)
    operator = "-"
    var = var + "-"
    the_data.set(var)

def mul():
    global A, var, operator
    A = float(var)
    operator = "*"
    var = var + "*"
    the_data.set(var)

def div():
    global A, var, operator
    A = float(var)
    operator = "/"
    var = var + "/"
    the_data.set(var)

def percent():
    global A, var, operator
    A = float(var)
    operator = "%"
    var = var + "%"
    the_data.set(var)

def dot():
    global var
    var = var + "."
    the_data.set(var)

def equal():
    global A, operator, var
    var2 = var
    if operator == "+":
        a = float((var2.split("+")[1]))
        x = A + a
        the_data.set(x)
        var = str(x)
    elif operator == "-":
        a = float((var2.split("-")[1]))
        x = A - a
        the_data.set(x)
        var = str(x)
    elif operator == "*":
        a = float((var2.split("*")[1]))
        x = A * a
        the_data.set(x)
        var = str(x)
    elif operator=="%":
        a=float((var2.split("%")[1]))
        x=A%a
        the_data.set(x)
        var=str(x)
    elif operator == "/":
        a = float((var2.split("/")[1]))
        if a == 0:
            messagebox.showerror("Division by 0 Not Allowed.")
            A == ""
            var = ""
            the_data.set(var)
        else:
            x = float(A / a)
            the_data.set(x)
            var = str(x)

def buttonC():
    global A, var, operator
    var = ""
    A = 0
    operator = ""
    the_data.set(var)

# creating the label for the window
the_data = StringVar()
gui_label = Label(window, width=25, height=2, text="", font=("consolas", 30), textvariable=the_data, bg="black", fg="#fff")
gui_label.pack()

# ... Other button configurations ...

Button(window, text="C", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=buttonC).place(x=10, y=100)
Button(window, text="/", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=div).place(x=150, y=100)
Button(window, text="%", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=percent).place(x=290, y=100)
Button(window, text="*", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=mul).place(x=430, y=100)

Button(window, text="7", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_7).place(x=10,y=200)
Button(window, text="8", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_8).place(x=150,y=200)
Button(window, text="9", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_9).place(x=290,y=200)
Button(window, text="-", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=sub).place(x=430,y=200)

Button(window, text="4", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_4).place(x=10,y=300)
Button(window, text="5", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_5).place(x=150,y=300)
Button(window, text="6", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_6).place(x=290,y=300)
Button(window, text="+", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=add).place(x=430, y=300)

Button(window, text="1", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_1).place(x=10,y=400)
Button(window, text="2", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_2).place(x=150,y=400)
Button(window, text="3", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_3).place(x=290,y=400)
Button(window, text="0", width=11, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=number_0).place(x=10,y=500)

Button(window, text=".", width=5, height=1, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=dot).place(x=290,y=500)
Button(window, text="=", width=5, height=3, font=("consolas", 30, "bold"), bd=1, fg="black", bg="white",command=equal).place(x=430, y=400)

window.mainloop()
