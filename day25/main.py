import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('States Game')

bg_path = 'blank_states_img.gif'
screen.addshape(bg_path)
turtle.shape(bg_path)

data = pd.read_csv('50_states.csv')

correctly_guessed_states = []
states = data.state.to_list()
number_of_states_to_guess = len(states)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.speed('fastest')

while len(correctly_guessed_states) < number_of_states_to_guess:
    guess = screen.textinput(f'{len(correctly_guessed_states)}/{number_of_states_to_guess} States Correct', 'Guess another state:').title()
    if guess in states and guess not in correctly_guessed_states:
        correctly_guessed_states.append(guess)
        state_row = data[data.state == guess]
        writer.goto(int(state_row.x), int(state_row.y))
        writer.write(guess)
    elif guess == 'exit'.title():
        break

missed_states = data[~data.state.isin(correctly_guessed_states)]
missed_states.to_csv('missed_states.csv')