from turtle import Turtle, Screen
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state # Series (Column...)
states_list = states.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?")
    guess = answer_state.title()

    if guess == "Exit":
        # missing_states = []
        # for state in states_list:
        #     if state not in correct_guesses:
        #         missing_states.append(state)

        # List Comprehension...
        missing_states = [state for state in states_list if state not in correct_guesses]

        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if guess in states_list:
        x = data[data.state == guess].x
        y = data[data.state == guess].y

        new_state = Turtle()
        new_state.pu()
        new_state.hideturtle()
        new_state.goto(x.iloc[0], y.iloc[0])
        new_state.write(f"{guess}")
        correct_guesses.append(guess)








