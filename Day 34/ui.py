from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0",bg=THEME_COLOR, fg="white", font=("Arial", 12))
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,125,width=280,text="Question", fill=THEME_COLOR,font=FONT)
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

        correct_answer = PhotoImage(file="C:\Python\Day 34\images/true.png")
        self.correct_button = Button(image=correct_answer,highlightthickness=0, command=self.correct_pressed)
        self.correct_button.grid(column=0,row=2)

        wrong_answer = PhotoImage(file="C:/Python/Day 34/images/false.png")
        self.wrong_button = Button(image=wrong_answer,highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(column=1,row=2)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The end.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def red(self):
        self.canvas
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)