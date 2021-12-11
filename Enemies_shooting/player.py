

import turtle 
from turtle import *



class Player(Turtle):
	def __init__(self):
		super().__init__()

		# setup turtle
		self.xmove=0
		self.ymove=0
		self.color('red')
		self.speed(10)
		self.shapesize(2,2)
		self.shape('square')
		self.penup()
		self.goto(0,-220)

	def move_right(self):
		
		self.goto(self.xcor()+10,-220)


	def move_left(self):
		self.goto(self.xcor()-10,-220)
