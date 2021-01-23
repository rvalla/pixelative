import time as tm
import numpy as np
from attractortive import Attractortive
from attractor import Attractor
from metaattractor import MetaAttractor
from attraccanvas import AttracCanvas

class MetaAttractortive(Attractortive):
	"Building and saving strange meta attractors"

	#the constructor
	def __init__(self, config, charcode):
		self.config = config
		self.starttime = tm.time()
		self.outPath = None
		self.outFile = None
		self.points = None
		self.depth = None
		self.sub = None
		self.loop = None
		self.origin = []
		self.param = []
		self.width = None
		self.height = None
		self.margin = None
		self.cmode = None
		self.colors = None
		self.background = None
		self.theattractor = None
		self.thecanvas = None
		MetaAttractortive.setConfig(self, self.config, charcode)
		print(self)
		MetaAttractortive.run(self)

	def run(self):
		print("-- Ready to build the base attractor...", end="\n")
		self.theattractor = Attractor(self.points, self.loop, self.origin, self.param[0], self.colors[0])
		for a in range(self.depth - 1):
			print("-- Ready to build the next meta attractor level...", end="\n")
			self.theattractor = MetaAttractor(self.loop, self.theattractor, self.param[a + 1], self.sub, self.colors)
		if self.theattractor.success:
			self.thecanvas = AttracCanvas(self.width, self.height, self.margin, self.background, self.cmode, self.theattractor)
			self.thecanvas.save(self.outPath, self.outFile)
			self.saveToDatabase("database/metaattractors.csv")
			print("-- time needed to build and paint this meta attractor: " + \
					self.getWorkingTime(self.starttime, tm.time()))
		else:
			print("-- there is no meta attractor to paint...", end="\n")

	#loading configuration parameters
	def setConfig(self, data, charcode):
		self.outPath = data["outPath"]
		self.outFile = data["outFile"]
		self.points = data["points"]
		self.depth = data["depth"]
		self.sub = MetaAttractortive.getSubdivisions(data["subdivisions"])
		self.loop = data["loop"]
		self.origin.append(data["originX"])
		self.origin.append(data["originY"])
		self.param = MetaAttractortive.loadParameters(self, data, self.depth)
		self.width = data["width"]
		self.height = data["height"]
		self.margin = data["margin"]
		self.cmode = data["colorMode"]
		self.colors = MetaAttractortive.getColors(self, data)
		self.background = self.getColor(data["backred"], data["backgreen"], data["backblue"])

	def loadParameters(self, data, depth):
		param = []
		for s in range(depth):
			aux = []
			if data["paramMode"] == "values":
				keyx = "paramX_" + str(s + 1)
				keyy = "paramY_" + str(s + 1)
				aux.append(self.getParametersFromValues(data[keyx]))
				aux.append(self.getParametersFromValues(data[keyy]))
			elif data["paramMode"] == "code":
				keyx = "paramCodeX_" + str(s + 1)
				keyy = "paramCodeY_" + str(s + 1)
				aux.append(self.getParametersFromCode(data[keyx]))
				aux.append(self.getParametersFromCode(data[keyy]))
			else:
				print("-- ups, something is wrong...", end="\n")
			param.append(aux)
		return param

	def getSubdivisions(list):
		values = list.split(",")
		steps = []
		for v in range(len(values)):
			steps.append(int(values[v]))
		return steps

	def getColors(self, data):
		colors = []
		r = data["facered"].split(",")
		g = data["facegreen"].split(",")
		b = data["faceblue"].split(",")
		for c in range(len(r)):
			colors.append(self.getColor(r[c], g[c], b[c]))
		return colors

	def __str__(self):
		return "-- pixelative --\n" + \
				"-- Meta Attractortive\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Playing with strange attractors.."
