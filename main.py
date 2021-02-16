# from turtle import Turtle, Screen
import turtle
import pandas
from state import State
#
#   screen setup
#
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

#
#   data import
#
states = pandas.read_csv("50_states.csv")
print(states)
#
#   https://towardsdatascience.com/filtering-data-frames-in-pandas-b570b1f834b9
#   how does boolean filtering work
#
#
print(states['state'] == 'Texas')       # returns a data series of booleans
print(states['x'] > 200)                # returns a data series of booleans
print(states[states.state == 'Texas'])  # the data series of booleans is passed as argument


gameover = False
guesses = []
score = 0
while not gameover:
    answer = screen.textinput(title=f"{score}/{len(states)} States Correct", prompt="What's another state's name?").title()
    if answer == "Stop":
        gameover = True
        break
    print(f"answer: {answer}")
    check = states[states.state == answer]
    print(f"check: {check}")
    print(f"len check: {len(check)}")
    if len(check) != 0:
        state = State(
            check.state.values[0],
            check.x.values[0],
            check.y.values[0],
        )
        state.show()
        guesses.append(state)
        score += 1
        if score == 50:
            gameover = True




# screen.mainloop()
# screen.exitonclick()


