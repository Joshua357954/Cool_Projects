import time 
import threading
import tkinter 
import random
import time
import math
from tkinter import *

SENTENCE_FONT=('Sans serif',13,'normal')
ENTRY_FONT=('Sans serif',13,'normal')


sents=open('sentence.txt')
all_sents=sents.readlines()

class MyGUI:
	def __init__(self):

		self.window=Tk()
		self.window.title("Type Speed")
		self.window.minsize(width=550,height=400)

		self.running=False
		self.count=0

		self.frame=Frame()
		self.frame.pack(pady=10)

		self.sentence=Label(self.frame,text=random.choice(all_sents).strip(),font=SENTENCE_FONT)
		self.sentence.pack(pady=20)

		self.sent_entry=Entry(self.frame,width=50,font=ENTRY_FONT)
		self.sent_entry.pack(pady=10)
		self.sent_entry.bind('<KeyRelease>',self.start_timer)


		self.speed_label=Label(self.frame,text=' Speed : 00.0\nCPS : 00.0\nCPM : 00.0\nWPS : 00.0\nWPM : 00.0',font=SENTENCE_FONT,fg='gray')
		self.speed_label.pack(pady=10)



		self.reset_button=Button(text='Reset',command=self.reset,font=SENTENCE_FONT).pack()

		

		self.window.mainloop()

	def start_timer(self,event):
		if not self.running:
			self.running=True
			t=threading.Thread(target=self.time_thread)
			t.start()

		if self.sentence.cget('text').startswith(self.sent_entry.get()):
			self.sent_entry.config(fg='black')
		else:
			self.sent_entry.config(fg='red')

		if self.sentence.cget('text')==self.sent_entry.get():
			self.running=False
			self.sent_entry.config(fg='green')



	def time_thread(self):
		while self.running:
			time.sleep(0.1)
			self.count+=0.1
			cps=len(self.sent_entry.get())/self.count
			cpm=cps * 60
			wps=len(self.sent_entry.get().split())/self.count
			wpm=wps * 60

			self.speed_label.config(text=f' Speed : {round(self.count,2)}\nCPS : {cps:2f} \nCPM : {cpm:2f}\n WPS : {wps:2f}\nWPM : {wpm:2f}')


	def reset(self):
		self.sent_entry.delete(0,END)
		self.running=False
		self.sentence.config(text=random.choice(all_sents).strip())
		self.speed_label.config(text=' Speed : 00.00\nCPS : 00.00 \nCPM : 00.00\n WPS : 00.0\nWPM : 00.0')




MyGUI()