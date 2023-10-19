import turtle
import os

wn = turtle.Screen()
wn.title("Pong by VJ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # This line stops the window from updating. If we want to update the window we'll have to do it manually

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # This is the speed of animation. This line sets the speed to the maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2
# Lines 34 and 35 are such that it makes the ball move 2 pixels whenever it moves

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A : 0  Player B : 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    if (paddle_a.ycor() > 239):
        return
    else :
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if (paddle_a.ycor() < -239):
        return
    else:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if (paddle_a.ycor() > 239):
        return
    else: 
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if (paddle_a.ycor() < -239):
        return
    else :
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # This line reverses the direction of the ball
        # os.system("aplay Hehe.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1