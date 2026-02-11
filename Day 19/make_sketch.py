from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_counter_clock():
    tim.left(10)
def move_clockwise():
    tim.right(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen() #Its an event listener used to do things based on keypresses or other things.
screen.onkey(move_forward,"w")
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_counter_clock)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=clear_screen)

screen.exitonclick()
