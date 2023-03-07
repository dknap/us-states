from turtle import Turtle

FONT = ("Arial", 8, "normal")
ALIGN = "center"


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.color = "white"
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(state, align=ALIGN, font=FONT)