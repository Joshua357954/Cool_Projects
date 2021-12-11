# This is the 2048 game project

# First create the gui (Frame,Label,ScoreLabel)
# make a reload gui method
# create a random tile function to add everytime you make a new move
# add key bindings to make new moves
# make the moves functionality

# configure the score board and row or column is merged 
#with the compiled merged value 

import tkinter 
from tkinter import *
import random

MAIN_BG='orange'
FRAME_BG='lightblue'
LABEL_FONT=("Sans serif",17,"normal")
BTN_FONT=("Sans serif",30,"bold")
RE="groove"

class Game:
	def __init__(self):
		self.score=0
		self.matrix=[]

		# Initialize the master Tk class
		self.root=Tk()
		self.root.minsize(300,370)
		self.root.maxsize(300,370)
		self.root.config(bg=MAIN_BG)

		# Score label 
		self.scoreLabel=Label(text=f'   Score \n   {self.score}',font=LABEL_FONT,bg=MAIN_BG)
		self.scoreLabel.pack(pady=10)

		# Buttons Frame
		self.frame=Frame(bg=FRAME_BG)
		self.frame.pack()

		# Add Key-Bindings 
		self.root.bind("<Up>",self.move_Up)
		self.root.bind("<Down>",self.move_Down)
		self.root.bind("<Left>",self.move_Left)
		self.root.bind("<Right>",self.move_Right)

		# Start Game Method

		self.start_game()
		self.add_tile()
		self.reload_gui()
		self.run_functions()
		
		self.root.mainloop()

	def start_game(self):
		self.matrix=[[0]*4 for _ in range(4)]
		print("The gmae has started ...")
		print(self.matrix)

		for i in range(4):
			for j in range(4):
				LAB=Label(self.frame,text=" " ,font=LABEL_FONT,relief=RE,width=4,height=2)
				LAB.grid(row=i,column=j,padx=5,pady=5)

	def add_tile(self):
		# for _ in range(2):		
		row=random.randint(0,3)
		column=random.randint(0,3)
		if self.matrix[row][column] ==0:
			self.matrix[row][column]=random.choice([2,4])
		else:
			row=random.randint(0,3)
			column=random.randint(0,3)
			self.matrix[row][column]=random.choice([2,4])

		print(self.matrix)

	def run_functions(self):
		self.stack()

	def reload_gui(self):

		for i in range(4):
			for j in range(4):
				new_val=self.matrix[i][j]
				if new_val != 0:
					LAB=Label(self.frame,text=self.matrix[i][j] ,font=LABEL_FONT,relief=RE,width=4,height=2)
					LAB.grid(row=i,column=j,padx=5,pady=5)
				else:
					LAB=Label(self.frame,text="",font=LABEL_FONT,relief=RE,width=4,height=2)
					LAB.grid(row=i,column=j,padx=5,pady=5)
		self.scoreLabel.config(text=f'   Score \n   {self.score}')
	# Keys----
	def stack(self):
		new_matrix=[[0]*4 for _ in range(4)]
		for i in range(4):
			fill_pos=0
			for j in range(4):
				if self.matrix[i][j] !=0:
					new_matrix[i][fill_pos]=self.matrix[i][j]
				fill_pos+=1
		self.matrix=new_matrix

	def combine(self):
		for i in range(4):
			for j in range(3):
				if self.matrix[i][j]!=0 and self.matrix[i][j]==self.matrix[i][j+1]:
					# self.matrix[i][j]=0
					self.matrix[i][j]*=2
					# self.matrix[i][j]=0
					self.score+=self.matrix[i][j]
					self.matrix[i][j]=0

		print(self.score)

	def reverse(self):
		new_matrix=[]
		for i in range(4):
			new_matrix.append([])
			for j in range(4):
				new_matrix[i].append(self.matrix[i][3-j])

		self.matrix=new_matrix

	def transpose(self):
		new_matrix=[[0]*4 for _ in range(4)]
		for i in range(4):
			for j in range(4):
				new_matrix[i][j]=self.matrix[i][j]

		self.matrix=new_matrix




	def move_Left(self,event):
		self.stack()
		self.combine()
		self.stack()
		self.add_tile()
		self.reload_gui()
	
	def move_Right(self,event):
		self.reverse()
		self.stack()
		self.combine()
		self.stack()
		self.reverse()
		self.add_tile()
		self.reload_gui()

	def move_Up(self,event):
		self.transpose()
		self.stack()
		self.combine()
		self.stack()
		self.transpose()
		self.add_tile()
		self.reload_gui()
	
	def move_Down(self,event):
		print("Moving Down")
		self.transpose()
		self.reverse()
		self.stack()
		self.combine()
		self.stack()
		self.reverse()
		self.transpose()
		self.add_tile()
		self.transpose()

Game()