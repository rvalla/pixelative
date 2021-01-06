import os
import warnings
import time as tm
import numpy as np
import json as js
from PIL import Image as im
from scipy.io import wavfile as wf

warnings.simplefilter("ignore", wf.WavFileWarning)

class SoundsColor():
	"Transforming sound in colors"

	def __init__(self, configpath):
		self.config = js.load(open(configpath))
		self.starttime = None
		self.outPath = None
		self.outFile = None
		self.mode = None
		self.iw = None
		self.ih = None
		self.imagedata = None
		self.audiosr = None
		self.audiodata = None
		SoundsColor.setConfig(self, self.config)
		print(self)
		SoundsColor.run(self)
		SoundsColor.save(self.outPath, self.outFile, self.imagedata)
		print("-- time needed to build the mistery image: " + \
				SoundsColor.getWorkingTime(self.starttime, tm.time()))

	def run(self):
		self.starttime = tm.time()
		if self.mode == "horizontal":
			SoundsColor.map(self.audiodata, self.imagedata, self.iw, self.ih, 0)
		elif self.mode == "vertical":
			SoundsColor.map(self.audiodata, self.imagedata, self.iw, self.ih, 1)
		elif self.mode == "both":
			SoundsColor.map(self.audiodata, self.imagedata, self.iw, self.ih, 2)
		else:
			print("-- I don't know what to do with this mode...", end="\n")

	def map(adata, idata, w, h, mode):
		print("-- mapping amplitude to color...", end="\r")
		for s in range(adata.shape[0]):
			if mode == 0:
				p = divmod(s, w)
				idata[p[0]][p[1]] +=  SoundsColor.getColor(abs(adata[s]))
			elif mode == 1:
				p = divmod(s, h)
				idata[p[1]][p[0]] += SoundsColor.getColor(abs(adata[s]))
			elif mode == 2:
				p = divmod(s, w)
				idata[p[0]][p[1]] += SoundsColor.getHalfColor(abs(adata[s]))
				p = divmod(s, h)
				idata[p[1]][p[0]] += SoundsColor.getHalfColor(abs(adata[s]))
		print("-- color data is ready!             ", end= "\n")

	def getColor(amplitude):
		color = np.zeros(3, dtype="uint8")
		color[0] = round(amplitude * 255)
		color[1] = round(amplitude * 181)
		color[2] = round(amplitude * 130)
		return color

	def getHalfColor(amplitude):
		color = np.zeros(3, dtype="uint8")
		color[0] = round(amplitude * 127)
		color[1] = round(amplitude * 90)
		color[2] = round(amplitude * 65)
		return color

	def save(filepath, filename, idata):
		image = im.fromarray(idata)
		image.save(filepath + filename + ".jpg")
		print("-- output image file saved!", end="\n")

	def setConfig(self, data):
		self.mode = data["mode"]
		self.outPath = data["outPath"]
		self.outFile = data["outFile"]
		self.iw = data["width"]
		self.ih = data["height"]
		self.imagedata = np.zeros((self.ih, self.iw, 3), dtype="uint8")
		self.audiosr, self.audiodata = wf.read(data["inPath"] + data["inFile"])
		self.startTime = tm.time()

	#Calculating time needed for processing an image...
	def getWorkingTime(start, end):
		time = end - start
		formatedTime = SoundsColor.formatTime(time)
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
				"-- SoundsColor\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Painting with sound..."
