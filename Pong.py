import turtle
import os

# Global Variables
is_paused = False

wn = turtle.Screen()
wn.title("Pong by VJ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A : 0  Player B : 0", align="center", font=("Courier", 24, "normal"))

# List of ball colors
ball_colors = ["blue", "red", "green", "yellow", "orange"]
current_color_index = 0

# Functions
def toggle_pause():
    global is_paused
    is_paused = not is_paused

def reset_positions():
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    ball.goto(0, 0)

# Add a function to reset the game
def reset_game():
    global score_a, score_b
    score_a = 0
    score_b = 0
    reset_positions()
    pen.clear()
    pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

def paddle_a_up():
    if (paddle_a.ycor() > 239):
        return
    else:
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
    if (paddle_b.ycor() > 239):
        return
    else:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if (paddle_b.ycor() < -239):
        return
    else:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(reset_game, "r")

# Call reset_game function to initialize the game
reset_game()

# Main game loop
while True:
    wn.update()

    if not is_paused:
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            current_color_index = (current_color_index + 1) % len(ball_colors)
            ball.color(ball_colors[current_color_index])

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            current_color_index = (current_color_index + 1) % len(ball_colors)
            ball.color(ball_colors[current_color_index])

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            current_color_index = (current_color_index + 1) % len(ball_colors)
            ball.color(ball_colors[current_color_index])

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            current_color_index = (current_color_index + 1) % len(ball_colors)
            ball.color(ball_colors[current_color_index])

        # Paddle and ball collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            current_color_index = (current_color_index + 1) % len(ball_colors)
            ball.color(ball_colors[current_color_index])

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            current_color_index = (current_color_index + 1) % len(ball_colors)
            ball.color(ball_colors[current_color_index])
