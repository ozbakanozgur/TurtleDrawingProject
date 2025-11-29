import turtle
from tkinter import mainloop

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("dark red")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("yellow")
turtle.speed(0)

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(10):                                 #Her turda "i" değer atlar.
    turtle_instance.color(turtle_colors[i % 6])     # 6'ya böler ve kalanı yazdırır, 6 renk var.
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)


#turtle.done()
mainloop()                 #aynı görevi yaparlar
