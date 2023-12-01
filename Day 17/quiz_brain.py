class QuizBrain:
    def __init__(self, question_list):
        self.q_num = 0
        self.q_list = question_list
        self.score = 0

    def still_has_question(self):
        length = len(self.q_list)
        if self.q_num < length:
            return True
        else:
            print("You've completed the quiz!")
            print(f"Your final score is: {self.score}/{self.q_num}")

    def quest(self):
        current_q = self.q_list[self.q_num]
        self.q_num +=1
        answer = input(f"Q.{self.q_num} {current_q.text} True or False? ")
        self.check_answer(answer, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is {self.score}/{self.q_num}")
        print("\n")