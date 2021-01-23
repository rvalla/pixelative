import sys
import math
import numpy as np
from attractor import Attractor

class MetaAttractor(Attractor):
	"A meta strange attractor"

	def __init__(self, lsize, attractor, parameters, subdivisions, colors):
		self.psize = attractor.size
		self.size = attractor.size * 2 #size is double of input attractor
		self.success = True #we save a success boolean variable
		self.loopsize = lsize #size of step in nested building loop
		self.getColorCount = 0 #saving how many times the color was returned
		self.sub = subdivisions #indexes where the attractors change
		self.acolor = 0 #the actual active color
		self.colors = colors #the meta attractor colors list
		self.x = attractor.data[0][0] #actual value for x
		self.limX = attractor.limX #storing maximum and minimum for x
		self.y = attractor.data[0][1] #actual value for y
		self.limY = attractor.limY #storing maximum and minimum for y
		self.xc = parameters[0] #attractor coeficients for x
		self.yc = parameters[1] #attractor coeficients for y
		self.data = MetaAttractor.buildInitialData(attractor.data, self.size) #the meta attractor points
		print("-- MetaAttractor construction started!", end="\n")
		MetaAttractor.buildPoints(self)
		print(self)

	def buildPoints(self):
		loops = divmod(self.psize, self.loopsize) #dividing iterations in steps
		for i in range(loops[0]):
			print("-- " + str(i * self.loopsize) + " points built...               ", end="\r")
			for e in range(self.loopsize):
				origin = e + i * self.loopsize
				destiny = origin + self.psize
				try:
					self.x = self.getNewCoordinate(self.data[origin][0], self.data[origin][1], self.xc)
					self.y = self.getNewCoordinate(self.data[origin][0], self.data[origin][1], self.yc)
				except:
					print("-- the attractor is so strange...", end="\n")
					print("-- the program is interrupted!", end="\n")
					self.success = False
					break
				if math.isfinite(self.x) and math.isfinite(self.y):
					self.data[destiny][0] = self.x #saving new point
					self.data[destiny][1] = self.y
					self.checkLimits(self.x, self.limX)
					self.checkLimits(self.y, self.limY)
				else:
					print("-- the attractor went to infinity...", end="\n")
					print("-- the program is interrupted!", end="\n")
					self.success = False
					break
			else:
				continue
			break
		print("-- all points were saved!                                         ", end="\n")

	def getColor(self):
		#here we return different colors for points from different attractors
		if self.getColorCount > self.sub[self.acolor]:
			self.acolor += 1
		self.getColorCount += 1
		return self.colors[self.acolor]

	def buildInitialData(data, newsize):
		#we need to double the data size saving the original one in the first half of the array
		newdata = np.zeros((newsize, 2), dtype="float64")
		newdata[0:data.shape[0]] = data
		return newdata

	def __str__(self):
		#the class meta attractor shows this if you print it
		return "-- MetaAttractor\n" + \
				"-- Points: " + str(self.size) + "\n" + \
				"-- x parameters: " + str(self.xc) + "\n" + \
				"-- y parameters: " + str(self.yc) + "\n" + \
				"-- Limits: " + str(self.limX) + ", " + str(self.limY)
