#imports
import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./")
import globalsettings
# import button handler class
from buttonClass import *
# import menu handler classes
from menuHandlerClass import *

#extended button class with button handler functions
class myButton(Button):
	def __init__(self, pin, lable, action):
		Button.__init__(self, pin, lable, action)
	#user defined button handlers here
	def button3Handler(self, menu=None, menufunc=None):
		globalsettings.SECOND_SCREEN
		if (globalsettings.DEBUGFLAG >= 1):
			print("Button 3 handler ") 
		if (menu.selected < (menu.length )):
			menu.selected -= 1
		if (menu.selected == 0 ):
			if (globalsettings.DEBUGFLAG >= 1):
				print("selected has overflowed ", menu.selected)
			globalsettings.SECOND_SCREEN = False
			menu.selected = menu.length

# List of buttons and associated handlers
myButtonsList = [myButton(22,"Button1", myButton.button1Handler),myButton(27, "Button2", myButton.button2Handler),myButton(17, "Button3", myButton.button3Handler)]


#extentions to MenuFunc class go here
# function handlers
class MyMenuFunc(MenuFunc):
	def __init__(self, folder):
		#self.functionHandlersDictionary = functionHandlersDictionary
		#print("init my menu func")
		MenuFunc.__init__(self, folder)
