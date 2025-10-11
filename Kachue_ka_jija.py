import random
from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Kachua Programmer")

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
sym = "[]()*;@#/,_-!&"

all = lower + upper + num + sym

frame = Frame(root)

Label(frame, text="Enter length for password: ", font=("Arial 16 bold")).pack(side=LEFT)
word = Entry(frame, font=("Arial 15 bold"))
word.pack()
frame.pack(pady=10)

length = int(input("Enter length for password: "))
password  = " ".join(random.sample(all, word))

frame1 = Frame(root)
password = Label(frame1, text="", font=("Arial 12"))
password.pack()

print(password)
