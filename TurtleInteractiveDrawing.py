import turtle
from tkinter import mainloop

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Drawing Board")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.right(100)

def rotate_angle_left():
    turtle_instance.left(100)

def clear_screen():
     turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()


drawing_board.listen()                                 # "(dinle) Klavye tuşlarına basılıp basılmadığını takip et"
drawing_board.onkey(fun=turtle_forward, key="space")   # onkey, bir tuşa basıldığında ne yapılacağını belirler.
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")

mainloop()
