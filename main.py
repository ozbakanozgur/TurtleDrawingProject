import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("dark red")          # background Color, Renk kodu da girilir
drawing_board.title("Turtle Drawing Board")

# square
turtle_instance = turtle.Turtle()       # kaplumbaya veya imleç, çizimi yapan
'''
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)


turtle_instance.forward(100)            # 100 piksel ileri git
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)

# star
for i in range(5):
    turtle_instance.forward(200)
    turtle_instance.left(144)
'''
# polygon
num_sides = 5             # kenar
angle = 360 / num_sides   # açı
side_length = 100          # ne kadar ile gittiği
for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)


turtle.done()                           # yazmazsak ekran kapanır




