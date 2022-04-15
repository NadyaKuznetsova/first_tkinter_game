from tkinter import *
import random
root = Tk()


f = Canvas(root, width=500, height=300, bg='grey')
f.pack()

p = 15

def i1():
  global p
  y = 1
  p = p - y
  if p <= 0:
    f.delete("all")
    lbl1.config(text = "Компьютер победил")
    lbl1.place(x=140, y=150)
  else:
    lbl1.config(text = " ".join([" |"] * p))

def i2():
  global p
  y = 2
  p = p - y
  if p <= 0:
    f.delete("all")
    lbl1.config(text = "Компьютер победил")
    lbl1.place(x=140, y=150)
  else:
    lbl1.config(text = " ".join([" |"] * p))

def i3():
  global p
  y = 3
  p = p - y
  if p <= 0:
    f.delete("all")
    lbl1.config(text = "Компьютер победил")
    lbl1.place(x=140, y=150)
  else:
    lbl1.config(text = " ".join([" |"] * p))

def r():
  global p
  y1 = random.randint(1, 3)
  p = p - int(y1)
  if p <= 0:
    f.delete("all")
    lbl1.config(text = "Игрок победил")
    lbl1.place(x=165, y=150)
  else:
    lbl1.config(text = " ".join([" |"] * p))

lbl1 = Label(root, text= "".join([" |"] * p), bg="blue", font=("Arial", 20,"bold"))
lbl1.place(x=150, y=150)
btn1 = Button(root, text="1", command= i1, font=("Arial", 10), bg="white")
btn1.place(x=220, y=100)
btn2 = Button(root, text="2", command= i2, font=("Arial", 10), bg="white")
btn2.place(x=260, y=100)
btn3 = Button(root, text="3", command= i3, font=("Arial", 10), bg="white")
btn3.place(x=300, y=100)
btn4 = Button(root, text ="ход компьютера", command = r, font = ("Forte", 15), bg='white',)
btn4.place(x=180, y=200)


root.mainloop()