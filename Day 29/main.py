from tkinter import *
from tkinter import messagebox
import random
import pyperclip
EMAIL = "luki@email.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for n in range(nr_letters)]
    password_symbols = [random.choice(symbols) for n in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for n in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("C:/Python/Day 29/data.txt",'a') as f:
                f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(column=1, row=0)
logo_img = PhotoImage(file="C:/Python/Day 29/logo.png")
canvas.create_image(100,100, image=logo_img)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, EMAIL)
password_label = Label(text="Password")
password_label.grid(column=0,row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1,row=3,columnspan=2)

password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(column=3,row=3)

add_button = Button(text="Add", width=30,command=save_to_file)
add_button.grid(column=1,row=4, columnspan=2)


window.mainloop()