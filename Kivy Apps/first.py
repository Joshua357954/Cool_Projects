from kivy.app import App 
from kivymd.app import MDApp 
from kivy.lang import Builder
from kivy.core.window import Window 

Window.size=(320,540)
kv="""
ScreenManager:
	Screen:
		MDFloatLayout:
			md_bg_color:app.theme_cls.primary_light



"""

def FirstApp(MDApp):
	
	pass

FirstApp().run()