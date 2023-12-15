from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_s = WORK_MIN * 60
    short_break_s = SHORT_BREAK_MIN * 60
    long_break_s = LONG_BREAK_MIN * 60
    print(reps)
    if reps%2 != 0:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
    elif reps%8 == 0:
        label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps%2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    minutes = math.floor(count/60)
    seconds = count%60  
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 50))
label.grid(column=1, row=0)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="C:/Python/Day 28/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,  35,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark = Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)
window.mainloop()