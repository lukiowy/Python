from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label",font=("Arial",24,"bold"))
my_label.grid(column=0, row= 0)

my_label["text"] = "New Text"
my_label.config(text = "New Text")

def button_click():
    asd = input.get()
    my_label["text"] = asd

button = Button(text="Click me", command = button_click)
button.grid(column=1, row =1)

input = Entry(width=10)
input.grid(column=3, row=2)

button2= Button(text="Button2")
button2.grid(column=2,row=0)


window.mainloop()

# def add(*args):
#     all = 0
#     for n in args:
#         all += n
#     print(all)

# add(1,2,3,4)