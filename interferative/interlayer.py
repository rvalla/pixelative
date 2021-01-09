import numpy as np
import random as rd
from PIL import Image as im

class InterLayer():
	"One of the layers to be blended"

	def __init__(self, ifile, cw, ch, position):
		self.idata = np.array(im.open(ifile))
		self.h = self.idata.shape[0]
		self.w = self.idata.shape[1]
		self.woffset = InterLayer.getOffset(self.w, cw, position)
		self.hoffset = InterLayer.getOffset(self.h, ch, position)

	def getOffset(size, csize, position):
		offset = 0
		space = csize - size
		if position == "random":
			offset = rd.randint(0, space)
		elif position == "center":
			offset = space // 2
		return offset

	def __str__(self):
		return "-- pixelative --\n" + \
				"-- InterLayer\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Blending images one on top of the other...\n"
