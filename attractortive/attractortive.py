import time as tm
import numpy as np
from attractor import Attractor
from attraccanvas import AttracCanvas

class Attractortive():
	"Building and saving strange attractors"

	#the constructor
	def __init__(self, config):
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
		self.color = None
		self.background = None
		Attractortive.setConfig(self, self.config)
		print(self)
		self.theattractor = Attractor(self.points, self.loop, self.origin, self.param, self.color)
		self.thecanvas = AttracCanvas(self.width, self.height, self.margin, self.background, self.theattractor)
		self.thecanvas.save(self.outPath, self.outFile)
		print("-- time needed to build and paint this attractor: " + \
				Attractortive.getWorkingTime(self.starttime, tm.time()))

	#loading configuration parameters
	def setConfig(self, data):
		self.outPath = data["outPath"]
		self.outFile = data["outFile"]
		self.points = data["points"]
		self.loop = data["loop"]
		self.origin.append(data["originX"])
		self.origin.append(data["originY"])
		self.param.append(Attractortive.getParametersList(data["paramMode"], data["paramCodeX"], data["paramX"]))
		self.param.append(Attractortive.getParametersList(data["paramMode"], data["paramCodeY"], data["paramY"]))
		self.width = data["width"]
		self.height = data["height"]
		self.margin = data["margin"]
		self.color = Attractortive.getColor(data["facered"], data["facegreen"], data["faceblue"])
		self.background = Attractortive.getColor(data["backred"], data["backgreen"], data["backblue"])

	#building list of parameters for attractor equations
	def getParametersList(mode, code, list):
		if mode == "values":
			return Attractortive.getParametersFromValues(list)
		elif mode == "code":
			return Attractortive.getParametersFromCode(code)

	#transforming parameters list in a list of floats
	def getParametersFromValues(list):
		values = list.split(",")
		parameters = []
		for v in range(len(values)):
			parameters.append(float(values[v]))
		return parameters

	#function to get parameters from code as the one use in Spratt's book
	def getParametersFromCode(list):
		print("-- under construction, sorry")

	#saving color data in a numpy array
	def getColor(r, g, b):
		color = np.zeros(3, dtype="float64")
		color[0] = r
		color[1] = g
		color[2] = b
		return color

	#calculating time needed for processing an image...
	def getWorkingTime(start, end):
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

	def __str__(self):
		return "-- pixelative --\n" + \
				"-- Attractortive\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Playing with strange attractors.."
