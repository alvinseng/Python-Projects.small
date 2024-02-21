import turtle
import pandas
from state_name import StateName

FONT = ('Courier', 10, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name = turtle

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

# print(answer_state)

data = pandas.read_csv("50_states.csv")
state_data = data["state"].to_list()


states_list = []

while len(states_list) < 50:
    answer_state = screen.textinput(title=f"{len(states_list)}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    state_coord = data[data.state == answer_state]

    if answer_state == "Exit":
        missed_states = [states for states in state_data if states not in states_list]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in state_data:
        states_list.append(answer_state)
        name_turtle = turtle.Turtle()
        name_turtle.hideturtle()
        name_turtle.speed("fastest")
        name_turtle.pu()
        name_turtle.goto(int(state_coord.x), int(state_coord.y))
        name_turtle.write(answer_state, align="center", font=FONT)
    else:
        continue


turtle.mainloop()