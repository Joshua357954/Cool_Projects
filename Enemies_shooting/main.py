import turtle
from turtle import *
import time
from player import Player
from p_bullet import PBullet
import threading

# THIS is a shooter game
# so make the preson to shoot 
# make the bullets
# make the scene prepared...
# Do the screen events like move left ,right and shoot
# The if manage to kill any enemies add score
# If the enemies bullet touch you 3 times means death ,you lose . 
# if you reach or kill up to twemty that is score up to twenty you win
my_bullet=PBullet()
my_player=Player()

# screen setup
screen=Screen()
screen.title('Enemies Killing')
screen.setup(width=600,height=500)
screen.listen()
screen.tracer(0)
screen.onkey(lambda : my_player.move_left(),'Left')
screen.onkey(lambda : my_player.move_right(),'Right')
screen.onkey(lambda : my_bullet.shoot_bullet((my_player.xcor(),my_player.ycor())),"Up")

def new_loop():
	global screen
	while True:

		screen.update()

threading.Thread(target=new_loop).start()



screen.mainloop()