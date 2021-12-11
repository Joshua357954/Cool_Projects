
from turtle import *
import random
import threading
import time

colors=['pink','yellow','green','cyan','gray','brown','orange']

class PBullet:

	def __init__(self):
		

		self.bullet_list=[]
		self.used_bullet=0
		self.make_bullets()
		
		
	def make_bullets(self):
		for _ in range(20):
			new_bullet=Turtle()
			new_bullet.color(random.choice(colors))
			new_bullet.shape('circle')
			new_bullet.penup()
			new_bullet.speed('fastest')
			new_bullet.goto(500,500)

			self.bullet_list.append(new_bullet)

	def shoot_bullet(self,loc):
		threading.Thread(target=lambda : self.real_shoot(loc)).start()

	def real_shoot(self,loc):
		for index in range(0,600,40):

			if self.used_bullet	>len(self.bullet_list):
				time.sleep(0.0001)
				new_y=loc[1]+index
				self.bullet_list[self.used_bullet].goto(loc[0],new_y)
			print(self.used_bullet)
			self.used_bullet+=1




