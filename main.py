# from turtle import Turtle, Screen
import turtle

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgpic(IMAGE)

# screen.addshape(IMAGE)
# turtle.shape(IMAGE)
# def getxy(x, y):
#     print(x, y)
# screen.onscreenclick(getxy)


answer = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
print(answer)


# screen.mainloop()
# screen.exitonclick()


