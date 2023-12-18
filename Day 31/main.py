from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
data = {}

try:
    df = pandas.read_csv("C:/Python/Day 31/data/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("C:/Python/Day 31/data/french_words.csv")
    data = original.to_dict(orient="records")
else:
    data = df.to_dict(orient="records")


def next_card():
    global random_card, flip_timer 
    try:
        window.after_cancel(flip_timer)
        random_card = random.choice(data)
        canvas.itemconfig(language, text="French", fill = "black")
        canvas.itemconfig(word, text=random_card["French"], fill="black")
        canvas.itemconfig(image, image=card_front)
        flip_timer = window.after(3000,flip_card)     
    except IndexError:
        canvas.itemconfig(word, text="No more words.", fill="black")


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_card["English"],fill="white")
    canvas.itemconfig(image, image=card_back)

def is_known():
    data.remove(random_card)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("C:/Python/Day 31/data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)

card_front = PhotoImage(file = "C:/Python/Day 31/images/card_front.png")
card_back = PhotoImage(file = "C:/Python/Day 31/images/card_back.png")
right = PhotoImage(file = "C:/Python/Day 31/images/right.png")
wrong = PhotoImage(file = "C:/Python/Day 31/images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400,263, image= card_front)
language = canvas.create_text(400, 150,text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0,row=0,columnspan=2)

x_button = Button(image=wrong, highlightthickness=0, command=next_card)
x_button.grid(column=0,row=1)

tick_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
tick_button.grid(column=1,row=1)

next_card()

window.mainloop()
