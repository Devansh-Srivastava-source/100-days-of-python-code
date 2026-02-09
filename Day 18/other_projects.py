import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    """This will give three components of making a color, ie, (r,g,b)"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tim.speed("fastest")
for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading+5)





screen = t.Screen()
screen.exitonclick()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("goldenrod1")
# for _ in range(7):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# colors_list = ["green", "DodgerBlue", "firebrick2", "khaki", "MidnightBlue", "hotpink", "orange", "purple"]
# for i in range(3,11):
#     for _ in range(i):
#         tim.color(colors_list[i-3])
#         tim.forward(100)
#         tim.right(360/i)

# for _ in range(200):
#     angle = [90,180,270,360]
#     colors_list = ["green", "DodgerBlue", "firebrick2", "khaki"]
#     ran_num1 = random.randint(0,3)
#     ran_num2 = random.randint(0,3)
#     tim.color(random_color())
#     tim.forward(30)
#     tim.right(angle[ran_num1])