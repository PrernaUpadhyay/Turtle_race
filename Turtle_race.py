from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create turtles and position them at the starting line
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start the race
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Move each turtle a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        # Check if a turtle has reached the finish line
        if turtle.xcor() > 230:  # Turtle has crossed the finish line
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! The {winning_color} turtle won the race, and you guessed correctly!")
            else:
                print(f"Sorry, the {winning_color} turtle won the race. Better luck next time!")

screen.exitonclick()
