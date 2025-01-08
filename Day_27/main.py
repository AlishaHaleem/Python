import tkinter

from Python.Day_27.playground import my_car

print("aws")

import tkinter as tk

window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


#import turtle as t
#tim = t.Turtle()
#tim.write("Some text")
#tim.shape("turtle")
#tim.color("red")
#tim.forward(100)








window.mainloop()