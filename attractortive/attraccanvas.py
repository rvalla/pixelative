import math
import numpy as np
from PIL import Image as im

class AttracCanvas():
	"The canvas where attractors are print"

	def __init__(self, w, h, margin, background, attractor):
		self.w = w #the result image width
		self.h = h #the result image height
		self.m = margin #rows and columns of blank pixels for border
		self.aw = abs(attractor.limX[1] - attractor.limX[0]) #here we store the attractor width
		self.ah = abs(attractor.limY[1] - attractor.limY[0]) #here we store the attractor height
		self.background = background
		self.pstate = np.zeros((h, w), dtype="int") #we save the pixel's state
		self.canvas = np.full((h, w, 3), self.background) #image color data
		self.overflowpixels = 0
		print("-- Canvas is ready!", end="\n")
		AttracCanvas.paintPoints(self, attractor)

	def paintPoints(self, attractor):
		print("-- painting " + str(attractor.size) + " attractor points...", end="\r")
		for p in range(attractor.data.shape[0]):
			x = AttracCanvas.getPixel(attractor.data[p][0], attractor.limX[0], self.aw, self.w, self.m)
			y = AttracCanvas.getPixel(attractor.data[p][1], attractor.limY[0], self.ah, self.h, self.m)
			if self.pstate[y][x] > 0:
				try:
					self.canvas[y][x] += attractor.color / math.pow(2, self.pstate[y][x]) #adding the color
					self.pstate[y][x] += 1 #saving how many points were painted in this pixel
				except:
					self.overflowpixels += 1
			else:
				self.canvas[y][x] = np.absolute(attractor.color)
				self.pstate[y][x] += 1
		print("-- " + str(self.overflowpixels) + " pixels were saturated...           ", end="\n")
		print("-- attractor points painted!", end="\n")

	def getPixel(f, amin, asize, isize, margin):
		ad = abs(f - amin) / asize #measuring the distance between coordinate and minimum
		pd = round((isize - 2 * margin) * ad) #mapping the distance to the actual image size
		return pd + margin

	def save(self, filepath, filename):
		data = np.array(np.round(self.canvas), dtype="uint8")
		image = im.fromarray(data)
		image.save(filepath + filename + ".jpg")
		print("-- Canvas was saved!", end="\n")

	def __str__(self):
		return "-- pixelative --\n" + \
				"-- AttracCanvas\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Looking for strange attractors...\n"
