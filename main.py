from turtle import Turtle
import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
file = pd.read_csv("50_states.csv")
all_states = file.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = file[file["state"] == answer_state]
        x = state_data["x"].iloc[0]
        y = state_data["y"].iloc[0]

        state_name = Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(x, y)
        state_name.write(answer_state)


