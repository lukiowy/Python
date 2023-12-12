import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States")
image = "C:/Python/Day 25/States/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("C:/Python/Day 25/States/50_states.csv")
correct_guesses = []
state_list = data.state.to_list()
score = 0
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title = f"{score}/50Guess the State", prompt="What's another name?").title()
    if answer_state == "Exit":
        for i in correct_guesses:
            state_list.remove(i)
        new_data = pandas.DataFrame(state_list)
        new_data.to_csv("C:/Python/Day 25/States/states_to_learn.csv")
        break
    for states in data["state"]:
        if answer_state == states:
            answer = turtle.Turtle()
            answer.hideturtle()
            answer.up()
            correct = data[data["state"] == answer_state]
            answer.goto(int(correct['x']),int(correct['y']))
            answer.write(answer_state)
            correct_guesses.append(answer_state)
            score +=1