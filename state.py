from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 12, "bold")


class State(Turtle):

    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.penup()
        self.hideturtle()

    def show(self):
        self.goto(self.x, self.y)
        self.write(self.name, align=ALIGN, font=FONT)
