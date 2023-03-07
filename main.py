import turtle
import pandas

DATA_FILE = "50_states.csv"
MAX_POINTS = 50
FONT = ("Arial", 16, "normal")
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

guessing = True
while guessing:

    user_guess = screen.textinput(title=f"{points}/{MAX_POINTS} States Correct", prompt="What's another state's name? ")
    print(user_guess)
    for state in range(len(states)-1):
        if user_guess.capitalize() == states[state]:
            # turtle.write(states[state], font=FONT)
            # turtle.setposition(data["x"][state], data["y"][state])
            correct_guesses.append(states[state])
            states.pop(state)
            points += 1
            print(correct_guesses)


#TODO: write correct guesses onto the map
#TODO: record the correct guesses in a list
#TODO: keep track of the score

