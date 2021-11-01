# Space Invaders
# Set up screenn

import turtle
import os

# Set up the Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

# Create the player turle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.pen()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)


# Create Player Speed
player_speed = 15

# Move the player left and right


def move_left():
    x = player.xcor()
    x -= player_speed
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    player.setx(x)

# Create keyboard binding


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_left, "Right")





delay = raw_input("Press Enter to Finish.")


