from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
is_race_on = False
# This below method is used to pop up a prompt window.
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will " \
"win the race? Enter a color: ")
print(user_bet)

colors = ['red','orange','yellow','green','blue','purple']
y_coor = [-70,-40,-10,20,50,80]
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape = "turtle") #See this shape changing.
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_coor[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won!")
            else:
                print(f"You lost. The {winning_color} turtle won.")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



# A turtle object is 40x40
# The color returns two values, one for pencolor and other for fill color.
screen.exitonclick()