# manualClasifierSkeleton

from Tkinter import *

# main window
master = Tk()

# make and pack the display widget
displayTweetLabel = Label(
	master, 
	text='test test', 
	anchor=W, 
	justify=LEFT
)
displayTweetLabel.pack(
	side=TOP
)
 
# changes the text of the display label
def updateDisplayLabel(newText):
	displayTweetLabel.config(text=newText)

# Use this to write tweet to display
def displayTweet(newTweet):
	updateDisplayLabel(newTweet)

"""
Below are all the functions that are called
when a button is clicked. I don't know if
passing them arguments will work/be easy,
however they can use global variables without
needing them to be passed. I suggest using
only global variables.
The event argument in each of the functions
is there to make it compatible with hotkeys
"""

def onPositiveClick(event=None):
	updateDisplayLabel('Positive')

def onFunnyClick(event=None):
	updateDisplayLabel('Funny')

def onAdvertisementClick(event=None):
	updateDisplayLabel('advertisement')

def onSadDisapointedClick(event=None):
	updateDisplayLabel('sadDisapointed')

def onAngryClick(event=None):
	print event.char
	updateDisplayLabel('angry')

def onSkipClick(event=None):
	updateDisplayLabel('Skip')

def onExitClick(event=None):
	updateDisplayLabel('Exit')

def onRemoveClick(event=None):
	updateDisplayLabel('remove')


# Button definitions
positive = Button(
	master, 
	text="Positive", 
	command=onPositiveClick
)

funny = Button(
	master, 
	text="Funny", 
	command=onFunnyClick
)

advertisement = Button(
	master, 
	text="Advertisement", 
	command=onAdvertisementClick
)

sadDisapointed = Button(
	master, 
	text="Sad/Disapointed", 
	command=onSadDisapointedClick
)

angry = Button(
	master, 
	text="Angry", 
	command=onAngryClick
)

Skip = Button(
	master, 
	text="Skip", 
	command=onSkipClick
)

Exit = Button(
	master, 
	text="Exit", 
	command=onExitClick
)

remove = Button(
	master, 
	text='Remove', 
	command=onRemoveClick
)

# putting buttons on screen

positive.pack(
	side=LEFT
)
funny.pack(
	side=LEFT
)
advertisement.pack(
	side=LEFT
)
sadDisapointed.pack(
	side=LEFT
)
angry.pack(
	side=LEFT
)
Skip.pack(
	side=LEFT
)
remove.pack(
	side=LEFT
)
Exit.pack(
	side=LEFT
)

# Hot keys
master.bind("1", onPositiveClick)
master.bind("2", onFunnyClick)
master.bind("3", onAdvertisementClick)
master.bind("4", onSadDisapointedClick)
master.bind("5", onAngryClick)
master.bind("6", onSkipClick)
master.bind("7", onRemoveClick)
master.bind("8", onExitClick)



master.mainloop()