from tkinter import *

def conversion():
    miles = int(entry.get())
    km = miles * 1.6
    label4["text"] = km

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)
label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

label2 = Label(text="Miles")
label2.grid(column=2, row=0)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

label4 = Label(text="0")
label4.grid(column=1, row=1)

button = Button(text="Calculate",command=conversion)
button.grid(column = 1, row = 2)

entry = Entry(text="0",width=10)
entry.grid(column=1, row=0)


window.mainloop()