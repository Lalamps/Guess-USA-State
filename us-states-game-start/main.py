import turtle
import pandas

screen = turtle.Screen()
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")
screen.title("Guess all States Game")
screen.tracer(0)

data = pandas.read_csv("50_states.csv")





def add_names(guess):
    guess_row = data.loc[data["state"] == guess, :].values.flatten().tolist()
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(guess_row[1], guess_row[2])
    new_turtle.write(guess, align='center', font=('Arial', 8, 'normal'))


def check_answer(guess):
    for state in data["state"]:
        if state == guess:
            add_names(guess)
            guessed_states.append(guess)




guessed_states = []

while True:
    screen.update()
    guess = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Type a State name: ").title()
    if guess in guessed_states:
        pass
    elif guess == "Exit":
        break
    else:
        check_answer(guess)

missed_states = [state for state in data["state"] if state not in guessed_states]


new_data = pandas.DataFrame(missed_states)
new_data.to_csv("missed_states")


print(missed_states)
print(len(missed_states))

screen.exitonclick()