import numpy as np
from PIL import Image as im

class InterCanvas():
	"The canvas where the images are blended"

	def __init__(self, w, h, br, bg, bb):
		self.w = w
		self.h = h
		self.background = InterCanvas.backgroundColor(br, bg, bb)
		self.pstate = np.zeros((h, w), dtype="int")
		self.idata = np.full((h, w, 3), self.background)
		print("-- Canvas is ready!", end="\n")

	def save(self, filepath, filename):
		data = np.array(np.round(self.idata), dtype="uint8")
		image = im.fromarray(data)
		image.save(filepath + filename + ".jpg")
		print("-- Canvas was saved!", end="\n")

	def backgroundColor(r, g, b):
		color = np.zeros(3, dtype="float64")
		color[0] = r
		color[1] = g
		color[2] = b
		return color

	def __str__(self):
		return "-- pixelative --\n" + \
				"-- InterCanvas\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Blending images one on top of the other...\n"
