import sys
import math
import numpy as np

class Attractor():
	"A strange attractor"

	def __init__(self, size, lsize, origin, parameters, color):
		self.size = size #number of iterations
		self.success = True
		self.loopsize = lsize #size of step in nested building loop
		self.color = color #the attractor color
		self.x = origin[0] #actual value for x
		self.px = self.x #previous value for x
		self.limX = [0.0, 0.0] #storing maximum and minimum for x
		self.y = origin[1] #actual value for y
		self.py = self.y #previous value for y
		self.limY = [0.0, 0.0] #storing maximum and minimum for y
		self.xc = parameters[0] #attractor coeficients for x
		self.yc = parameters[1] #attractor coeficients for y
		self.data = np.zeros((size, 2), dtype="float64") #the attractor points
		print("-- Attractor construction started!", end="\n")
		Attractor.buildPoints(self)

	def buildPoints(self):
		loops = divmod(self.size, self.loopsize) #dividing iterations in steps
		for i in range(loops[0]):
			print("-- " + str(i * self.loopsize) + " points built...               ", end="\r")
			for e in range(self.loopsize):
				try:
					self.x = Attractor.getNewCoordinate(self.px, self.py, self.xc) #get a new x coordinate
					self.y = Attractor.getNewCoordinate(self.px, self.py, self.yc) #get a new y coordinate
				except:
					print("-- the attractor is so strange...", end="\n")
					print("-- the program is interrupted!", end="\n")
					self.success = False
					break
				self.px = self.x #updating previous values
				self.py = self.y
				self.data[i*self.loopsize + e][0] = self.x #saving new point
				self.data[i*self.loopsize + e][1] = self.y
				Attractor.checkLimits(self.x, self.limX)
				Attractor.checkLimits(self.y, self.limY)
			else:
				continue
			break
		print("-- all points were saved!                                         ", end="\n")

	def getNewCoordinate(px, py, c):
		#taking previous x and y and calculating new value for coeficients store in c
		f = c[0] + px * c[1] + math.pow(px, 2) * c[2] + math.pow(px, 3) * c[3] + \
			math.pow(px, 2) * py * c[4] + px * py * c[5] + px * math.pow(py, 2) * c[6] + \
			py * c[7] + math.pow(py, 2) * c[8] + math.pow(py, 3) * c[9]
		return f

	def checkLimits(f, limits):
		#we save minimum and maximum coordinates to know the attractor's area
		if f < limits[0]:
			limits[0] = f
		elif f > limits[1]:
			limits[1] = f

	def __str__(self):
		#the class attractor shows this if you print it
		return "-- pixelative --\n" + \
				"-- Attractor\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- The chaos in the plane...\n" + \
				"-- Points: " + str(self.size) + "\n" + \
				"-- Limits: " + str(self.limX) + ", " + str(self.limY)
