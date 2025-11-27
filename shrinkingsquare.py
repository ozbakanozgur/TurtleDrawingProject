import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def shrinking_square(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5


shrinking_square(200)
shrinking_square(180)
shrinking_square(160)
shrinking_square(140)
shrinking_square(120)
shrinking_square(100)
shrinking_square(80)
shrinking_square(60)
shrinking_square(40)
shrinking_square(20)


turtle.done()
