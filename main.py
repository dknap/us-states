import turtle
import pandas
from state import State

DATA_FILE = "50_states.csv"
MAX_POINTS = 50
points = 0
correct_guesses = []

screen = turtle.Screen()
screen.screensize(canvwidth=400, canvheight=400)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(DATA_FILE)
states = data["state"].to_list()
print(states)

while len(correct_guesses) < 50:
    user_guess = screen.textinput(title=f"{points}/{MAX_POINTS} States Correct", prompt="What's another state's name? ")
    print(user_guess)
    for state in range(len(states)):
        if user_guess.title() == states[state]:
            show_state = State(states[state], data["x"][state], data["y"][state])
            if user_guess.title() not in correct_guesses:
                correct_guesses.append(states[state])
                points += 1
            print(correct_guesses)
    if user_guess == "exit" or user_guess == "Exit":
        missing_list = []
        for state in states:
            if state not in correct_guesses:
                missing_list.append(state)

        to_learn = pandas.DataFrame(missing_list)
        # print(to_learn)
        to_learn.to_csv("to_learn.csv")
        break





