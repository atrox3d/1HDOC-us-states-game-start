# from turtle import Turtle, Screen
import turtle
import pandas
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
    answer = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if answer == "Stop":
        gameover = True
        break
    print(f"answer: {answer}")
    check = states[states.state == answer]
    print(f"check: {check}")
    print(f"len check: {len(check)}")
    if len(check) != 0:
        guesses.append(answer)
        score += 0
        print("#TODO write state on screen")
        # print(type(check.state.values))
        print(check.state.values[0])
        print(check.x.values[0])
        print(check.y.values[0])




# screen.mainloop()
# screen.exitonclick()


