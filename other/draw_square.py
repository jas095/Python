import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(0,3):
        some_turtle.forward(100)
        some_turtle.left(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("FIGURAS")
    #Create the turtle goku - Draws a square and create an circle with this
    goku = turtle.Turtle()
    #Create the turtle gohan - Draws a triangle
    gohan = turtle.Turtle()
    #Create the turtle vegeta - Draws a circle
    vegeta = turtle.Turtle()
    goku.shape("triangle")
    goku.color("#2196F3")
    vegeta.shape("square")
    vegeta.color("#E91E63")
    gohan.shape("circle")
    gohan.color("#AA00FF")
    goku.speed(100)
    gohan.speed(100)
    vegeta.speed(100)
    goku.pu()
    goku.setpos(-200,0)
    gohan.pu()
    gohan.setpos(200,0)

    for i in range(36):#it would be 360 degrees
        #goku - Draws a square
        goku.pd()
        draw_square(goku)
        goku.right(10)
        #Vegeta - Draws a circle
        vegeta.circle(90)
        vegeta.right(10)
        #Gohan - Draws a triangle
        gohan.pd()
        draw_triangle(gohan)
        gohan.right(10)
    gohan.right(90)
    gohan.fd(400)
    vegeta.right(90)
    vegeta.fd(400)
    goku.right(90)
    goku.fd(400)

    # for i in range(3):
    #     for i in range(4):
    #         draw_triangle(gohan)
    #         gohan.fd(30)
    #     gohan.left(120)




    window.exitonclick()

draw_art()
