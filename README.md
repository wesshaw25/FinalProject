# FinalProject
# creating a pong game with 4 paddles and 1< balls
# Proposal

## What will (likely) be the title of your project?

Extreme Pong

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

I will be taking the well known simple game of pong and elevating it to include multiple balls and four sides.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

My software will take the original design and simplistic code of pong and enhance it slightly. By adding new components to the game there will be a big more complex coding. The code will create multiple balls, a user paddle, and three computer paddles to play the game. It will be executed through a series of function and loops.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

TODO, if applicable

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

TODO, if applicable

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

I am hoping at the very least I am able to get the simple pong game down with the extra components aside. 

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

I think I should be able to accomplish (on top of the pong game) the addition of multiple balls and more paddles.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

I hope to accomplish the above. I would like to expect the addition of more balls and paddles.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

My next steps are going to be important and I am going to need to execute them thoroughly. I am going to need to refine and review many skills as well as extend my knowledge beyond what I know already to solidify my project. I am going to need to figure out how to program the computer users to play an effective game against the human user. 

FINAL CODE

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
        
    


