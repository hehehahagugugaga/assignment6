import tkinter as tk

window = tk.Tk()
window.minsize(width=300, height=300)

e = tk.Entry(window, width=54, borderwidth=5)
e.place(x=0, y=0)

def click(num):
    result=e.get()
    e.delete(0,tk.END)
    e.insert(0,str(result)+str(num))


button = tk.Button(text="1",width=12, command=lambda :click(1))
button.place(x=2, y=40)

button = tk.Button(text="2",width=12, command=lambda :click(2))
button.place(x=102, y=40)

button = tk.Button(text="3",width=12, command=lambda :click(3))
button.place(x=202, y=40)

button = tk.Button(text="4",width=12, command=lambda :click(4))
button.place(x=2, y=80)

button = tk.Button(text="5",width=12, command=lambda :click(5))
button.place(x=102, y=80)

button = tk.Button(text="6",width=12, command=lambda :click(6))
button.place(x=202, y=80)

button = tk.Button(text="7",width=12, command=lambda :click(7))
button.place(x=2, y=120)

button = tk.Button(text="8",width=12, command=lambda :click(8))
button.place(x=102, y=120)

button = tk.Button(text="9",width=12, command=lambda :click(9))
button.place(x=202, y=120)

button = tk.Button(text="0",width=12, command=lambda :click(0))
button.place(x=102, y=160)

def add():
    n1=e.get()
    global math
    math= "addition"
    global i
    i = int(n1)
    e.delete(0,tk.END)

def sub():
    n1=e.get()
    global math
    math= "subtraction"
    global i
    i = int(n1)
    e.delete(0,tk.END)

def div():
    n1=e.get()
    global math
    math= "division"
    global i
    i = int(n1)
    e.delete(0,tk.END)

def mul():
    n1=e.get()
    global math
    math= "multiplication"
    global i
    i = int(n1)
    e.delete(0,tk.END)

def equal():
    n2=e.get()
    e.delete(0,tk.END)
    if math== "addition":
        e.insert(0,i+int(n2))
    elif math== "subtraction":
        e.insert(0,i-int(n2))
    elif math== "division":
        e.insert(0,i/int(n2))
    elif math== "multiplication":
        e.insert(0,i*int(n2))

def clear():
    e.delete(0,tk.END)

button = tk.Button(text="+",width=12, command=add)
button.place(x=2, y=160)

button = tk.Button(text="-",width=12, command=sub)
button.place(x=102, y=160)

button = tk.Button(text="/",width=12, command=div)
button.place(x=202, y=160)

button = tk.Button(text="*",width=12, command=mul)
button.place(x=102, y=160)

button = tk.Button(text="=",width=12, command=equal)
button.place(x=202, y=160)

button = tk.Button(text="CLEAR",width=12, command=mul)
button.place(x=102, y=200)

window.mainloop()
