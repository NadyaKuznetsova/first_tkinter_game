from tkinter import *

root = Tk()
root.geometry("300x200")

def test():
    btn1.config(text="new text")

lbl1 = Label(root, text= "| | | | | | | | | | | | | | |", bg="blue", font=("Arial", 20,"bold"))
lbl1.place(x=40, y=100)
btn1 = Button(root, text="1", command= test, font=("Arial", 10), bg="white")
btn1.place(x=100, y=60)
btn2 = Button(root, text="2", command= test, font=("Arial", 10), bg="white")
btn2.place(x=140, y=60)
btn3 = Button(root, text="3", command= test, font=("Arial", 10), bg="white")
btn3.place(x=180, y=60)

root.mainloop()