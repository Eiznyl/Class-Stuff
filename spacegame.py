import turtle
import os
import math

screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Space Game')

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('green')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for edge in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

icon = turtle.Turtle()
icon.color('green')
icon.shape('triangle')
icon.penup()
icon.speed(0)
icon.setposition(0,-200)
icon.setheading(90)

iconspeed = 15

def move_left():
	x = icon.xcor()
	x -= iconspeed
	if x < -280:
		x = - 280
	icon.setx(x)

turtle.listen()
turtle.onkey(move_left, 'Left')

def move_right():
	x = icon.xcor()
	x += iconspeed
	if x > 280:
		x = 280
	icon.setx(x)

turtle.listen()
turtle.onkey(move_right, 'Right') 

def fire_gun():
	global gunstate
	if gunstate == "ready":
		gunstate = "fire"	
		x = icon.xcor()
		y = icon.ycor() +10
		gun.setposition(x, y)
		gun.showturtle()
	
turtle.listen()
turtle.onkey(fire_gun, 'space')

def collision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(), 2))
	if distance < 15:
		return True
	else: 
		return False

bad = turtle.Turtle()
bad.color('red')
bad.shape('square')
bad.penup()
bad.speed(0)
bad.setposition(-200, 250)

badspeed = 2

gun = turtle.Turtle()
gun.color('white')
gun.shape('circle')
gun.penup()
gun.speed(0)
gun.shapesize(0.5, 0.5)
gun.hideturtle()

gunspeed = 20

gunstate = "ready"

while True:
	x = bad.xcor()
	x += badspeed
	bad.setx(x) 

	if bad.xcor() > 280:
		y = bad.ycor()
		y -= 40
		badspeed *= -1
		bad.sety(y)
	if bad.xcor() < -280:
		y = bad.ycor()
		y -= 40
		badspeed *= -1
		bad.sety(y)
	if gunstate == "fire":
		y = gun.ycor()
		y += gunspeed
		gun.sety(y)

	if gun.ycor() > 275:
		gun.hideturtle()
		gunstate = "ready"
	
	if collision(gun, bad):
		gun.hideturtle()
		gunstate = "ready"
		gun.setposition(0, -400)
		bad.setposition(-200, 250)
delay = input('Press enter to finish')
