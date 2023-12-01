from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    text = i['text']
    ans = i['answer']
    q = Question(text, ans)
    question_bank.append(q)

q = QuizBrain(question_bank)
while q.still_has_question() == True:
    q.quest()
