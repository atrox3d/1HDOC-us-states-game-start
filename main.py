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
#########################################################################################################
#   https://towardsdatascience.com/filtering-data-frames-in-pandas-b570b1f834b9
#   how does boolean filtering work
#########################################################################################################
print(states['state'] == 'Texas')       # returns a data series of booleans
print(states['x'] > 200)                # returns a data series of booleans
print(states[states.state == 'Texas'])  # the data series of booleans is passed as argument
#########################################################################################################
#
#   setup variables
#
gameover = False
all_states = states.state.to_list()
guesses = []
score = 0
try:
    with open("save") as savefile:
        lines = savefile.readlines()
        for line in lines:
            statename = line.strip()
            check = states[states.state == statename]
            print(check)
            newstate = State(
                check.state.item(),
                check.x.item(),
                check.y.item(),
            )
            newstate.show()
            #
            #   save answer/state object
            #
            guesses.append(newstate)
            #
            #   update score
            #
            score += 1
except FileNotFoundError:
    print("save file not found")
# exit()
#
#   main loop
#
while not gameover:
    #
    # get answer Title case
    #
    answer = screen.textinput(title=f"{score}/{len(states)} States Correct", prompt="What's another state's name?").title()
    #
    # failsafe
    #
    if answer == "Stop":
        gameover = True
        guessed_states = [state.name for state in guesses]
        missing_states = [
            state for state in all_states if state not in guessed_states
        ]
        print(missing_states)
        break
    print(f"answer: {answer}")
    #
    # check if answer is correct
    #
    check = states[states.state == answer]
    print(f"check: {check}")
    print(f"len check: {len(check)}")
    print(
        f"check.state.values[0]  : '{check.state.values[0]}': {type(check.state.values[0])}\n"
        f"str(check.state)       : '{str(check.state)}': {type(str(check.state))}\n"
        f"str(check.state.item()): '{check.state.item()}': {type(check.state.item())}"
    )
    print(
        f"check.x.values[0]      : {check.x.values[0]}: {type(check.x.values[0])}\n"
        f"int(check.x)           : {int(check.x)}: {type(int(check.x))}\n"
        f"check.x.item())        : {check.x.item()}: {type(check.x.item())}\n"
    )
    print(
        f"check.y.values[0]      : {check.y.values[0]}: {type(check.y.values[0])}\n"
        f"int(check.y)           : {int(check.y)}: {type(int(check.y))}\n"
        f"check.y.item())        : {check.y.item()}: {type(check.y.item())}\n"
    )
    if len(check) != 0:
        #
        #   if correct create new object to write state on map
        #
        state = State(
            check.state.item(),
            check.x.item(),
            check.y.item(),
        )
        state.show()
        #
        #   save answer/state object
        #
        guesses.append(state)
        #
        #   update score
        #
        score += 1
        if score == 50:
            #
            #   win
            #
            gameover = True


# screen.mainloop()
# screen.exitonclick()


