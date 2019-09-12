import turtle

isaiah = turtle.Turtle()
paige = turtle.Turtle()
dyson = turtle.Turtle()
jarrett = turtle.Turtle()
isaiah.color("dark slate blue")
dyson.color("aquamarine")
isaiah.speed(100)
dyson.speed(100)
paige.speed(100)
jarrett.speed(100)

isaiah.forward(100)
jarrett.right(90)
jarrett.forward(100)
paige.right(180)
paige.forward(100)
dyson.left(90)
dyson.forward(100)
turtle.left(90)
def quartercircle():
     for i in range (1,5):
         turtle.circle(100)
         turtle.left(90)
quartercircle()
def square():
    for i in range (1,60):
        isaiah.forward(100)
        isaiah.right(90)
        isaiah.right(5)
square()
def square2():
    for i in range (1,60):
        dyson.forward(100)
        dyson.right(90)
        dyson.right(5)

square2()
def square3():
    for i in range (1,60):
        paige.forward(100)
        paige.right(90)
        paige.right(5)
square3()
def square4():
    for i in range (1,60):
        jarrett.forward(100)
        jarrett.right(90)
        jarrett.right(5)
square4()




turtle.exitonclick()