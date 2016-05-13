# p2GUI.py

import time as time
import PIL as pil
import Tkinter as tkinter
import math as math
import threading as threading
import random as random
import stream_data
random.seed()

X = 0
Y = 1

def convertCor(x, y, maxheight):
	return (x, maxheight-y)

class Bar:
	def __init__(self, parentCanvas, bottomCenter, maximumHeight, width, color):
		self.parentCanvas = parentCanvas
		self.bottomCenter = bottomCenter
		self.maximumHeight = maximumHeight
		self.currentHeight = 0
		self.width = width
		self.color = color
		self.percent = 0.0

		# junk rectangle, reference used to delete old rectange before
		# drawing again
		self.rectangle = parentCanvas.create_rectangle(0,0,1,1, fill=self.color)

	# return the height that would represent the current percent
	def heightOfPercent(self):
		return int(float(self.maximumHeight) * self.percent)

	# redraw the bar to the specified height
	def drawNewHeight(self, newHeight):
		if newHeight > self.maximumHeight:
			newHeight = self.maximumHeight

		x1, y1 = convertCor(
			self.bottomCenter[X] - self.width/2,
			self.bottomCenter[Y] + newHeight,
			self.parentCanvas.winfo_height()
		)
		x2, y2 = convertCor(
			self.bottomCenter[X] + self.width/2,
			self.bottomCenter[Y],
			self.parentCanvas.winfo_height()
		)
		self.currentHeight = newHeight
		self.parentCanvas.delete(self.rectangle)
		self.rectangle = self.parentCanvas.create_rectangle(x1, y1, x2, y2, fill=self.color)


	# draw option to immediatly represent the percent
	def drawAtpercent(self):
		self.drawNewHeight(self.heightOfPercent())

	# draw option to smoothly approach percent
	# this method increments the height towards the
	# height of the percent value this bar contains.
	# returns true if the current height is equal
	# to the height of the percent, and false if it is
	# still catching up
	def incrementTowardsPercent(self, increment):
		if math.fabs(self.heightOfPercent()-self.currentHeight) <= increment:
			return True
		oldHeight = self.currentHeight
		if self.heightOfPercent() > self.currentHeight:
			self.drawNewHeight(oldHeight+increment)
			return False
		if self.heightOfPercent() < self.currentHeight:
			self.drawNewHeight(oldHeight-increment)
			return False


class Graph(tkinter.Canvas):
	def __init__(self, parent, height, numberOfBars, colorsOfBars):
		# this little chunk aranges the bars based on
		# the following hardcoded parameters, and produces
		# a width that is recomended for the canvas
		# based on them. The height of the canvas is still
		# chosed by whoever constructs the Graph object
		self.verticalBumbers = 100
		self.horizontalBumbers = 75
		self.spaceBetweenBars = 50
		self.barWidth = 100
		self.recomendedWidth = 0

		# determines what x values the bottom centers
		# of the bars aught to have to be nicely spaced
		# based on the parameters defined above.
		# the y value of the centers will just be the
		# self.verticalBumbers member
		XsOfCenters = self.setRecomendedWidthAndReturnXsOfCenters(
				numberOfBars
			)

		# call the super constructor for the canvas
		tkinter.Canvas.__init__(
			self,
			parent,
			width=self.recomendedWidth,
			height=height
		)
		# keep a reference to the parent window
		# pack this widget into the parent window
		# update this widget so that its dimensions
		# assume their proper values. UPDATE BEFOR
		# ADDING BARS
		self.parent = parent
		self.pack()
		self.background = 'white'
		self.update()

		# add the bars
		self.bars = []
		for i in range(0, numberOfBars):
			self.bars.append(
				Bar(
					self,
					(XsOfCenters[i], self.verticalBumbers),
					self.winfo_height()-2*self.verticalBumbers,
					self.barWidth,
					colorsOfBars[i]
				)
			)


	# based on the number of bars defined in construction,
	# and the horizontalBumbers and widthBeetweenBars members,
	# this method determines how the bars should be space out,
	# and recomends a width for the width of the canvas based
	# on that spacing
	def setRecomendedWidthAndReturnXsOfCenters(self, numberOfBars):
		width = 0
		width += self.horizontalBumbers
		XsOfCenters = []
		for i in range(0, numberOfBars):
			width += self.barWidth/2
			XsOfCenters.append(width)
			width += self.barWidth/2
			if i == numberOfBars -1:
				break
			width += self.spaceBetweenBars
		self.recomendedWidth = width + self.horizontalBumbers
		return XsOfCenters


	# changes the percent members of each of the bars.
	# this is the best way to change what direction the
	# bars grow in.
	def setPercents(self, percentsArray):
		for i in range(0, len(self.bars)):
			self.bars[i].percent = percentsArray[i]

	# drawing option for smoothly approaching
	# heights that match percents
	def incrementTowardsPercents(self, increment):
		allBarsAreCurrent = True
		for bar in self.bars:
			if not bar.incrementTowardsPercent(increment):
				allBarsAreCurrent = False
		return allBarsAreCurrent


	# drawing option for immediatly drawing
	# bars such that they reflect their percents
	def drawAllBarsAtPercentHeight(self):
		for bar in self.bars:
			bar.drawAtpercent()



class GUI(tkinter.Tk):
	def __init__(self, height, numberOfBars, colorsOfBars):
		tkinter.Tk.__init__(self)
		self.barGraph = Graph(self, height, numberOfBars, colorsOfBars)
		startButton = tkinter.Button(self, text="start", command = stream_data.startStream)
		startButton.pack()
		stopButton = tkinter.Button(self, text="stop", command = stream_data.stopStream)
		stopButton.pack()

	def setPercents(self, percentsArray):
		self.barGraph.setPercents(percentsArray)

	def startMainloop(self):
		self.mainloop()

	def firstDraw(self):
		self.barGraph.drawAllBarsAtPercentHeight()





colorsOfBars = [ 'red', 'green', 'blue' ]
height = 600
numberOfBars = 3
gui = GUI(height, numberOfBars, colorsOfBars)

oneHundredPercent = float(gui.barGraph.bars[0].maximumHeight)
# gui.setPercents(
# 	[
# 		float(random.randrange(oneHundredPercent)/oneHundredPercent),
# 		float(random.randrange(oneHundredPercent)/oneHundredPercent),
# 		float(random.randrange(oneHundredPercent)/oneHundredPercent)
# 	]
# )
def runInMainLoop():
	gui.barGraph.incrementTowardsPercents(2)
	gui.after(1, runInMainLoop)

def updatePercents():
	oneHundredPercent = float(gui.barGraph.bars[0].maximumHeight)
	gui.setPercents(stream_data.ratioList)
	gui.after(1000, updatePercents)

gui.after(1, runInMainLoop)
gui.after(50, updatePercents)
gui.startMainloop()
