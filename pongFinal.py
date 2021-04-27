import turtle

wn = turtle.Screen()
wn.title("Extreme Pong")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

score_a = 0
score_b = 0
score_c = 0
score_d = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.dy = .01

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("white")
paddle_c.shapesize(stretch_wid=1, stretch_len=5)
paddle_c.penup()
paddle_c.goto(0,350)

paddle_d = turtle.Turtle()
paddle_d.speed(0)
paddle_d.shape("square")
paddle_d.color("white")
paddle_d.shapesize(stretch_wid=1, stretch_len=5)
paddle_d.penup()
paddle_d.goto(0,-350)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1.5
ball.dy = 1

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0 Player C: 0  Player D: 0", align ="center", font=("Courier", 18, "normal"))

def paddle_a_up():

    y = paddle_a.ycor()
    y += 1
    paddle_a.sety(y)

def paddle_a_down():
    
    y = paddle_a.ycor()
    y -= 1
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

def paddle_c_up():

    x = paddle_c.xcor()
    x += 1
    paddle_c.setx(x)

def paddle_c_down():
    
    x = paddle_c.xcor()
    x -= 1
    paddle_c.setx(x)

def paddle_d_up():
    x = paddle_d.xcor()
    x += 1
    paddle_d.setx(x)

def paddle_d_down():
    x = paddle_d.xcor()
    x -= 1
    paddle_d.setx(x)
    
wn.listen()
#wn.onkeypress(paddle_a_up, "w")
#wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    paddle_a.sety(paddle_a.ycor() + paddle_a.dy)

    if ball.ycor() > paddle_a.ycor():
        paddle_a_up()  
    if ball.ycor() < paddle_a.ycor():
        paddle_a_down()

    if ball.xcor() > paddle_c.xcor():
        paddle_c_up()  
    if ball.xcor() < paddle_c.xcor():
        paddle_c_down()

    if ball.xcor() > paddle_d.xcor():
        paddle_d_up()  
    if ball.xcor() < paddle_d.xcor():
        paddle_d_down()

    """
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    """
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=-1
        pen.clear()
        pen.write("Player A: {}  Player B: {}  Player C: {}  Player D: {}".format(score_a, score_b, score_c, score_d), align ="center", font=("Courier", 18, "normal"))
    

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=-1
        pen.clear()
        pen.write("Player A: {}  Player B: {}  Player C: {}  Player D: {}".format(score_a, score_b, score_c, score_d), align ="center", font=("Courier", 18, "normal"))


    if ball.ycor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_c +=-1
        pen.clear()
        pen.write("Player A: {}  Player B: {}  Player C: {}  Player D: {}".format(score_a, score_b, score_c, score_d), align ="center", font=("Courier", 18, "normal"))
    

    if ball.ycor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_d +=-1
        pen.clear()
        pen.write("Player A: {}  Player B: {}  Player C: {}  Player D: {}".format(score_a, score_b, score_c, score_d), align ="center", font=("Courier", 18, "normal"))

    

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() < -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1  

    if ball.ycor() > 340 and ball.ycor() < 350 and (ball.xcor() < paddle_c.xcor() + 40 and ball.xcor() > paddle_c.xcor() - 40):
        ball.sety(340)
        ball.dy *= -1

    if ball.ycor() < -340 and ball.ycor() < -350 and (ball.xcor() < paddle_d.xcor() + 40 and ball.xcor() > paddle_d.xcor() - 40):
        ball.sety(-340)
        ball.dy *= -1  
        
    

