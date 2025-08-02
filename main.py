import turtle
import pandas

screen = turtle.Screen()
screen.title("States Game")
image = "C:/Users/KIIT/OneDrive/Documents/VS code - AH/python/states game/us_states.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Users/KIIT/OneDrive/Documents/VS code - AH/python/states game/50_states.csv")
all_states = data.states.to_list()
guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt= "Whats another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and not guessed_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



screen.exitonclick()
