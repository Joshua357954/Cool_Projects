
from tkinter import *
from random import choice ,shuffle
from tkinter import messagebox

# flip pairs game
# using a for loop create  4 rows with two items each 

# make a function that populate the lists with random items

# create a re-render function to check the list
# and render the cards based on the properties

# create a flip card mechanism once a card is fliped
# will change the image of the card to the image specified in that index
# append that index item to pairs list

# crete a function to check if the pairs are same after two flips
# if pairs are same . we will increase the score and re-render our cards
# if the pairs are complete we will use a message box  to say game over 

import time

SCORE_FONT=("Sans serif",12,"bold")

BUTTON_FONT=("Sans serif",15,"bold")

BGC='lightgreen'

class FlipPairs:

	def __init__(self):
		# Basic screen setup
		self.root=Tk()
		self.root.minsize(300,450)
		self.root.title("FlipPairs-Game")
		self.root.config(bg=BGC)

		# Globals
		self.score=0
		self.pairs=[]
		self.clicked_b=[]
		self.card_list=[[{'img':'1.png','closed':True},{'img':'3.png','closed':True}],
						[{'img':'3.png','closed':True},{'img':'2.png','closed':True}],
						[{'img':'2.png','closed':True},{'img':'4.png','closed':True}],
						[{'img':'4.png','closed':True},{'img':'3.png','closed':True}]]
		self.num=[1,1,2,2,3,3,4,4]

		self.flip_count=0

		self.frame=Frame(bg=BGC)
		self.frame.pack(pady=10)

		self.b0=Button(self.frame,text=" "*7,font=BUTTON_FONT,command=lambda: self.flip_me(self.b0,0))
		self.b1=Button(self.frame,text=" "*7,font=BUTTON_FONT,command=lambda: self.flip_me(self.b1,1))
		self.b2=Button(self.frame,text=" "*7,font=BUTTON_FONT,command=lambda: self.flip_me(self.b2,2))
		self.b3=Button(self.frame,text=" "*7,font=BUTTON_FONT,command=lambda: self.flip_me(self.b3,3))

		self.b4=Button(self.frame,text=" "*7,font=BUTTON_FONT,command=lambda: self.flip_me(self.b4,4))
		self.b5=Button(self.frame,text=" "*7,font=BUTTON_FONT,command=lambda: self.flip_me(self.b5,5))
		self.b6=Button(self.frame,text=" "*7,font=BUTTON_FONT,command=lambda: self.flip_me(self.b6,6))
		self.b7=Button(self.frame,text=" "*7,font=BUTTON_FONT,command=lambda: self.flip_me(self.b7,7))

		self.reset_btn=Button(self.root,text="Reset",font=BUTTON_FONT,command=self.refresh)
		self.reset_btn.pack()
		self.b0.grid(row=0,column=0,padx=10,pady=10)
		self.b1.grid(row=0,column=1,padx=10,pady=10)

		self.b2.grid(row=1,column=0,padx=10,pady=10)
		self.b3.grid(row=1,column=1,padx=10,pady=10)

		self.b4.grid(row=2,column=0,padx=10,pady=10)
		self.b5.grid(row=2,column=1,padx=10,pady=10)

		self.b6.grid(row=3,column=0,padx=10,pady=10)
		self.b7.grid(row=3,column=1,padx=10,pady=10)

		self.scoreLabel=Label(bg=BGC,text=f"Score {self.score}/{4}",font=SCORE_FONT)
		self.scoreLabel.pack()
		self.make_random_cards()
		self.make_buttons()


		self.root.mainloop()

	def make_random_cards(self):
		shuffle(self.num)

	# def render_cards(self):
	# 	for index , row in enumerate(self.card_list):
			
	# 		for i , column in enumerate(row) :

	# 			tex=f"row - {index} ,column {i}"

	# 			self.label=Button(self.frame ,text=tex , command=lambda:self.flip_me('kicc'))
	# 			self.label.grid(row=index,column=i,padx=10,pady=20)



	def make_buttons(self):
		pass

	def reset_buttons(self):
		messagebox.showinfo("Hey","Incorrect Move")
		for btnk in self.clicked_b:
			btnk['state']='normal'
			btnk['text']=" "*7

					
	def flip_me(self,*d_item):

		if self.flip_count <3:
			self.flip_count+=1
			btn,index=d_item[0],d_item[1]
			number=self.num[index]

			btn['text']=f'  {number}   '
			btn['state']='disabled'
			self.pairs.append(number)
			self.clicked_b.append(btn)

			


			if len(self.pairs)==2  :
				print(self.pairs)

				if self.pairs[0]==self.pairs[1]:
					print('match')
					self.score+=1

					for ind ,btns in enumerate(self.clicked_b):
						btns['text']=f"   {self.pairs[ind]}   "
					self.scoreLabel.config(text=f"Score {self.score}/4")

					self.pairs=[]
					self.clicked_b=[]
					self.flip_count=0

				else:
					self.flip_count=0
					self.pairs=[]
					print(self.clicked_b)

					self.reset_buttons()

					self.clicked_b=[]
					

		if self.score==4:
			messagebox.showinfo("Nice Job","You Win...")
			all_btn=[self.b0,self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7]
			for _all in all_btn:
				_all.config(bg="lightgray",relief='groove')


			
	def refresh(self):
		all_btn=[self.b0,self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7]

		for bts in all_btn:
			bts.config(text=" "*7,state='active',bg='SystemButtonFace')
			self.pairs=[]
			self.score=0
			self.clicked_b=[]
			self.scoreLabel.config(text=f"Score {self.score}/4")



	
				


FlipPairs()






































