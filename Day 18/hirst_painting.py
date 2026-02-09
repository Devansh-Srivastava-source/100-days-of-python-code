import turtle as t
import random
# The below two lines are used for extraction of colors from image.
# import colorgram
# colors = colorgram.extract('image2.jpg',30)
t.colormode(255)
colors = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (0, 255, 255),    # Cyan
    (255, 192, 203),  # Pink
    (165, 42, 42),    # Brown
    (128, 128, 128),  # Gray
    (0, 0, 0),        # Black
    (143, 255, 200), 
    (0, 128, 128),    # Teal
    (75, 0, 130),     # Indigo
    (255, 20, 147)    # Deep Pink
]
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setx(-300)
timmy.sety(-150)
for j in range(1,11):
    for i in range(1,11):
        timmy.pendown()
        timmy.dot(30,random.choice(colors))
        timmy.penup()
        timmy.forward(50)
        
    timmy.home()
    timmy.setx(-300)
    timmy.sety(-150+(j*40))
#We dont need pen down for dot operation.
screen = t.Screen()
screen.exitonclick()