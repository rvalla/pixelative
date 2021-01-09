import os
import json as js
import time as tm
import numpy as np
from PIL import Image as im
from intercanvas import InterCanvas
from interlayer import InterLayer

class Interferative():
	"Blending images one on top of the other"

	def __init__(self, configpath):
		self.config = js.load(open(configpath))
		self.starttime = None
		self.outPath = None
		self.outFile = None
		self.mode = None
		self.position = None
		self.cw = None
		self.ch = None
		self.omit = None
		self.omittedcolor = None
		self.canvas = None
		self.fList = []
		self.iList = []
		Interferative.setConfig(self, self.config)
		print(self)
		Interferative.buildLayers(self.config["inPath"], self.fList, self.iList, self.cw, self.ch, self.position)
		Interferative.blend(self)
		self.canvas.save(self.outPath, self.outFile)
		print("-- time needed to build the blended image: " + \
				Interferative.getWorkingTime(self.starttime, tm.time()))

	def blend(self):
		if self.mode == "average":
			for l in range(len(self.iList)):
				print("-- pasting layer number " + str(l + 1), end="\r")
				if self.omit:
					Interferative.sumLayerIf(self.canvas, self.iList[l], self.omittedcolor)
				else:
					Interferative.sumLayer(self.canvas, self.iList[l])
			print("-- all layers pasted!             ", end="\n")
			Interferative.getAverage(self.canvas)

	def getAverage(canvas):
		print("-- calculating color average...", end="\r")
		for w in range(canvas.idata.shape[1]):
			for h in range(canvas.idata.shape[0]):
				if canvas.pstate[h][w] > 0:
					canvas.idata[h][w] = canvas.idata[h][w] / canvas.pstate[h][w]
		print("-- average ready!                 ", end="\n")

	def sumLayer(canvas, image):
		for w in range(image.w):
			for h in range(image.h):
				x = image.woffset + w
				y = image.hoffset + h
				if canvas.pstate[y][x] > 0:
					canvas.idata[y][x] += image.idata[h][w]
					canvas.pstate[y][x] += 1
				else:
					canvas.idata[y][x] = image.idata[h][w]
					canvas.pstate[y][x] += 1

	def sumLayerIf(canvas, image, omittedcolor):
		for w in range(image.w):
			for h in range(image.h):
				if Interferative.compareColor(image.idata[h][w], omittedcolor) == False:
					x = image.woffset + w
					y = image.hoffset + h
					if canvas.pstate[y][x] > 0:
						canvas.idata[y][x] += image.idata[h][w]
						canvas.pstate[y][x] += 1
					else:
						canvas.idata[y][x] = image.idata[h][w]
						canvas.pstate[y][x] += 1

	def compareColor(color, omittedcolor):
		return color[0] == omittedcolor[0] and color[1] == omittedcolor[1] and color[2] == omittedcolor[2]

	def setConfig(self, data):
		self.outPath = data["outPath"]
		self.outFile = data["name"]
		self.mode = data["mode"]
		self.position = data["position"]
		self.cw = data["width"]
		self.ch = data["height"]
		self.omit = data["omit"]
		self.omittedcolor = np.zeros((3), dtype="uint8")
		self.omittedcolor[0] = data["omitred"]
		self.omittedcolor[1] = data["omitgreen"]
		self.omittedcolor[2] = data["omitblue"]
		self.canvas = InterCanvas(self.cw, self.ch, data["backred"], data["backgreen"], data["backblue"])
		self.fList = Interferative.cleanFileList(os.listdir(data["inPath"]))
		self.starttime = tm.time()

	def buildLayers(path, flist, ilist, cw, ch, position):
		print("-- building layers...", end="\r")
		for i in range(len(flist)):
			ilist.append(InterLayer(path + flist[i], cw, ch, position))
		print("-- " + str(len(flist)) + " layers were built!     ", end="\n")

	def cleanFileList(flist):
		f = 0
		while (f < len(flist)):
			if flist[f].startswith("."):
				del flist[f]
			else:
				f += 1
		return flist

	#Calculating time needed for processing an image...
	def getWorkingTime(startTime, endTime):
		time = endTime - startTime
		formatedTime = Interferative.formatTime(time)
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
				"-- Interferative\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Blending images one on top of the other..."
