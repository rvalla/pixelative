import time as tm
import numpy as np
from attractor import Attractor
from attraccanvas import AttracCanvas

class Attractortive():
	"Building and saving strange attractors"

	#the constructor
	def __init__(self, config, charcode):
		self.config = config
		self.starttime = tm.time()
		self.outPath = None
		self.outFile = None
		self.points = None
		self.loop = None
		self.origin = []
		self.param = []
		self.width = None
		self.height = None
		self.margin = None
		self.cmode = None
		self.color = None
		self.background = None
		Attractortive.setConfig(self, self.config, charcode)
		print(self)
		self.theattractor = Attractor(self.points, self.loop, self.origin, self.param, self.color)
		if self.theattractor.success:
			self.thecanvas = AttracCanvas(self.width, self.height, self.margin, self.background, self.cmode, self.theattractor)
			self.thecanvas.save(self.outPath, self.outFile)
			Attractortive.saveToDatabase(self, "database/attractors.csv")
			print("-- time needed to build and paint this attractor: " + \
					Attractortive.getWorkingTime(self, self.starttime, tm.time()))
		else:
			print("-- there is no attractor to paint...", end="\n")

	#loading configuration parameters
	def setConfig(self, data, charcode):
		self.outPath = data["outPath"]
		self.outFile = data["outFile"]
		self.points = data["points"]
		self.loop = data["loop"]
		self.origin.append(data["originX"])
		self.origin.append(data["originY"])
		self.param.append(Attractortive.getParametersList(self, data["paramMode"], data["paramCodeX"], data["paramX"], charcode))
		self.param.append(Attractortive.getParametersList(self, data["paramMode"], data["paramCodeY"], data["paramY"], charcode))
		self.width = data["width"]
		self.height = data["height"]
		self.margin = data["margin"]
		self.cmode = data["colorMode"]
		self.color = Attractortive.getColor(self, data["facered"], data["facegreen"], data["faceblue"])
		self.background = Attractortive.getColor(self, data["backred"], data["backgreen"], data["backblue"])

	#building list of parameters for attractor equations
	def getParametersList(self, mode, code, list, charcode):
		if mode == "values":
			return Attractortive.getParametersFromValues(self, list)
		elif mode == "code":
			return Attractortive.getParametersFromCode(self, code, charcode)

	#transforming parameters list in a list of floats
	def getParametersFromValues(self, list):
		values = list.split(",")
		parameters = []
		for v in range(len(values)):
			parameters.append(float(values[v]))
		return parameters

	#function to get parameters from code as the one use in Spratt's book
	def getParametersFromCode(self, code, charcode):
		charlist = [char for char in code]
		parameters = []
		for c in range(len(charlist)):
			parameters.append(charcode[charlist[c]])
		return parameters

	#saving color data in a numpy array
	def getColor(self, r, g, b):
		color = np.zeros(3, dtype="float64")
		color[0] = r
		color[1] = g
		color[2] = b
		return color

	#calculating time needed for processing an image...
	def getWorkingTime(self, start, end):
		time = end - start
		formatedTime = Attractortive.formatTime(time)
		return formatedTime

	def formatTime(time):
		ms = ""
		minutes = time // 60
		seconds = time - minutes * 60
		seconds = round(seconds, 2)
		ms = "{:02d}".format(int(minutes))
		ms += ":"
		ms += "{:05.2f}".format(seconds)
		return ms

	def saveToDatabase(self, file):
		try:
			file = open(file, "a")
			file.write(str(self.points) + ",")
			file.write(str(self.param[0]) + ",")
			file.write(str(self.param[1]) + ",")
			file.write(str(self.theattractor.limX[0]) + ",")
			file.write(str(self.theattractor.limX[1]) + ",")
			file.write(str(self.theattractor.limY[0]) + ",")
			file.write(str(self.theattractor.limY[1]) + "\n")
			file.close()
		except:
			print("-- the attractor could not be saved to the database...", end="\n")

	def __str__(self):
		return "-- pixelative --\n" + \
				"-- Attractortive\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Playing with strange attractors.."
