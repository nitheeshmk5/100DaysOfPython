from turtle import Turtle, Screen
import pandas,turtle

my_screen = Screen()
my_screen.title('Guess Any 10 States in India')

my_screen.addshape("india_outline.gif")
turtle.shape("india_outline.gif")

data = pandas.read_csv('states.csv')
all_states = data['state'].to_list()

guess_states = []

while len(guess_states) < 10:
    
    answer_state = my_screen.textinput(
        title=f"Guess {len(guess_states)}/10 States",
        prompt="Enter a state name (or 'exit' to quit): "
        ).title()

    if answer_state.lower() == "exit":
        break

    if answer_state in all_states:
        tur = Turtle()
        tur.hideturtle()
        tur.penup()
        tur.color("red1")
        state_data = data[data['state'] == answer_state]
        x_coord = int(state_data['x'].iloc[0])
        y_coord = int(state_data['y'].iloc[0])
    
        tur.goto(x_coord, y_coord)
        tur.write(answer_state, align="center", font=('Arial', 6, 'normal'))
        
        guess_states.append(answer_state)
    else:
        my_screen.textinput("Invalid State", "Please enter a valid state name.")

if len(guess_states) == 10:
    tur = Turtle()
    tur.hideturtle()
    tur.penup()
    tur.goto(0, 225)
    tur.color("red")
    tur.write("Congratulations!\nYou guessed all 10 states!", align="center", font=('Courier', 24, 'bold'))

my_screen.exitonclick()
