import warnings
import math
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
		self.direction = None
		self.iw = None
		self.ih = None
		self.imagedata = None
		self.cfactors = []
		self.audiosr = None
		self.audioch = None
		self.audiodata = None
		SoundsColor.setConfig(self, self.config)
		print(self)
		SoundsColor.run(self)
		SoundsColor.save(self.outPath, self.outFile, self.imagedata)
		print("-- time needed to build the mistery image: " + \
				SoundsColor.getWorkingTime(self.starttime, tm.time()))

	def run(self):
		self.starttime = tm.time()
		if self.audioch == 1:
			print("-- ready to process " + str(self.audiodata.shape) + " samples...")
			if self.direction == "horizontal":
				SoundsColor.mapMono(self.audiodata, self.imagedata, self.iw, self.ih, self.cfactors, 0)
			elif self.direction == "vertical":
				SoundsColor.mapMono(self.audiodata, self.imagedata, self.iw, self.ih, self.cfactors, 1)
			elif self.direction == "both":
				SoundsColor.mapMono(self.audiodata, self.imagedata, self.iw, self.ih, self.cfactors, 2)
			else:
				print("-- I don't know what to do with this mode...", end="\n")
		elif self.audioch == 2:
			print("-- ready to process " + str(self.audiodata.shape[0]) + " samples...")
			if self.direction == "horizontal":
				SoundsColor.mapStereo(self.audiodata, self.imagedata, self.iw, self.ih, self.cfactors, 0)
			elif self.direction == "vertical":
				SoundsColor.mapStereo(self.audiodata, self.imagedata, self.iw, self.ih, self.cfactors, 1)
			elif self.direction == "both":
				SoundsColor.mapStereo(self.audiodata, self.imagedata, self.iw, self.ih, self.cfactors, 2)
			else:
				print("-- I don't know what to do with this mode...", end="\n")
		else:
			print("-- I only know what to do with 1 or 2 audio channels...", end="\n")

	def mapMono(adata, idata, w, h, cf, mode):
		print("-- mapping amplitude to color...", end="\r")
		for s in range(adata.shape[0]):
			if mode == 0:
				p = divmod(s, w)
				idata[p[0]][p[1]] +=  SoundsColor.getColor(abs(adata[s]), cf[0], cf[1], cf[2])
			elif mode == 1:
				p = divmod(s, h)
				idata[p[1]][p[0]] += SoundsColor.getColor(abs(adata[s]), 255 - cf[0], 255 - cf[1], 255 - cf[2])
			elif mode == 2:
				p = divmod(s, w)
				idata[p[0]][p[1]] += SoundsColor.getHalfColor(abs(adata[s]), cf[0], cf[1], cf[2])
				p = divmod(s, h)
				idata[p[1]][p[0]] += SoundsColor.getHalfColor(abs(adata[s]), 255 - cf[0], 255 - cf[1], 255 - cf[2])
		print("-- color data is ready!             ", end= "\n")

	def mapStereo(adata, idata, w, h, cf, mode):
		print("-- mapping amplitude to color...", end="\r")
		for s in range(adata.shape[0]):
			if mode == 0:
				p = divmod(s, w)
				idata[p[0]][p[1]] +=  SoundsColor.getColor(abs(adata[s][0]), cf[0], cf[1], cf[2])
			elif mode == 1:
				p = divmod(s, h)
				idata[p[1]][p[0]] += SoundsColor.getColor(abs(adata[s][1]), 255 - cf[0], 255 - cf[1], 255 - cf[2])
			elif mode == 2:
				p = divmod(s, w)
				idata[p[0]][p[1]] += SoundsColor.getHalfColor(abs(adata[s][0]), cf[0], cf[1], cf[2])
				p = divmod(s, h)
				idata[p[1]][p[0]] += SoundsColor.getHalfColor(abs(adata[s][1]), 255 - cf[0], 255 - cf[1], 255 - cf[2])
		print("-- color data is ready!             ", end= "\n")

	def getColor(amplitude, rf, gf, bf):
		color = np.zeros(3, dtype="uint8")
		color[0] = round(SoundsColor.mapAmplitude(amplitude, rf))
		color[1] = round(SoundsColor.mapAmplitude(amplitude, gf))
		color[2] = round(SoundsColor.mapAmplitude(amplitude, bf))
		return color

	def getHalfColor(amplitude, rf, gf, bf):
		color = np.zeros(3, dtype="uint8")
		color[0] = round(SoundsColor.mapAmplitude(amplitude, rf) / 2)
		color[1] = round(SoundsColor.mapAmplitude(amplitude, gf) / 2)
		color[2] = round(SoundsColor.mapAmplitude(amplitude, bf) / 2)
		return color

	def mapAmplitude(amplitude, factor):
		return math.sqrt(amplitude) * factor

	def save(filepath, filename, idata):
		image = im.fromarray(idata)
		image.save(filepath + filename + ".jpg")
		print("-- output image file saved!", end="\n")

	def setConfig(self, data):
		self.direction = data["direction"]
		self.outPath = data["outPath"]
		self.outFile = data["outFile"]
		self.iw = data["width"]
		self.ih = data["height"]
		self.imagedata = np.zeros((self.ih, self.iw, 3), dtype="uint8")
		self.audioch = SoundsColor.getAudioChannels(data)
		self.cfactors.append(data["redfactor"])
		self.cfactors.append(data["greenfactor"])
		self.cfactors.append(data["bluefactor"])
		self.audiosr, self.audiodata = wf.read(data["inPath"] + data["inFile"])
		self.startTime = tm.time()

	def getAudioChannels(data):
		if data["audio"] == "mono":
			return 1
		elif data["audio"] == "stereo":
			return 2
		else:
			return 0

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
