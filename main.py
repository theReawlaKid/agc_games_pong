import turtle
import winsound


def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
        paddle_b.sety(y)


def write_score():
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


def sound_wall():
    winsound.PlaySound("sounds\\wall.wav", winsound.SND_ASYNC)


def sound_paddle():
    winsound.PlaySound("sounds\\paddle.wav", winsound.SND_ASYNC)


def sound_score():
    winsound.PlaySound("sounds\\score.wav", winsound.SND_ASYNC)


wn = turtle.Screen()
wn.title("Pong by @ReawlaCode")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)
# score trackers
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
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3
# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
write_score()
# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "d")
wn.onkeypress(paddle_b_up, "p")
wn.onkeypress(paddle_b_down, "l")


# main game loop
while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # border checking
    if ball.ycor() > 290:
        sound_wall()
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -280:
        sound_wall()
        ball.sety(-280)
        ball.dy *= -1
    if ball.xcor() > 410:
        sound_score()
        ball.goto(100, 0)
        ball.dx *= -1
        score_a += 1
        write_score()
    if ball.xcor() < -410:
        sound_score()
        ball.goto(-100, 0)
        ball.dx *= -1
        score_b += 1
        write_score()
    # paddle and ball collisions
    if ball.xcor() > 330 and (paddle_b.ycor() + 50) > ball.ycor() > (paddle_b.ycor() - 50):
        sound_paddle()
        ball.dx *= -1
    if ball.xcor() < -330 and (paddle_a.ycor() + 50) > ball.ycor() > (paddle_a.ycor() - 50):
        ball.dx *= -1
        sound_paddle()


