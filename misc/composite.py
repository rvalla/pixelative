from PIL import Image as im, ImageDraw as idraw, ImageFilter as ifil

class Composite():
	"Code to do some simple image compositions"

	def __init__(self, inPath, outPath):
		self.inPath = inPath
		self.outPath = outPath

	def meanImage(self, backFile, topFile, outName):
		backImage = im.open(self.inPath + backFile)
		topImage = im.open(self.inPath + topFile).resize(backImage.size)
		mask = im.new("L", backImage.size, 127)
		new = im.composite(backImage, topImage, mask)
		new.save(self.outPath + outName)

	def attractorMask(self, background, maskFile, topFile, outName):
		topImage = im.open(self.inPath + topFile)
		backImage = im.new("RGB", topImage.size, background)
		mask = im.open(self.inPath + maskFile).convert("L").resize(topImage.size)
		new = im.composite(backImage, topImage, mask)
		new.save(self.outPath + outName)

	def __str__(self):
		return "-- pixelative --\n" + \
				"-- Misc\n" + \
				"-- https://gitlab.com/azarte/pixelative\n" + \
				"-- version: 0.50\n" + \
				"-- Some code to play with compositions..."
