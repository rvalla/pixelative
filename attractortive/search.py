#looking for some strange attractors
import json as js
import random as rd
from attractortive import Attractortive

count = 100 #number of intends
paramInterval = 4 #limiting the random values

#loading the character code set
charset = js.load(open("config/characterset.json"))

#loading default configuration
config = js.load(open("config/search/searching.json"))
filename = config["outFile"]

#function to get random values
def getRandomValue(interval):
	v = rd.random()
	v = v * interval - interval / 2
	return round(v, 2)

#function to create a rando parameters list
def randomParameters():
	parameters = ""
	for p in range(10):
		parameters += str(getRandomValue(paramInterval))
		if p < 9:
			parameters += ","
	return parameters

#the loop to look for attractors
for t in range(count):
	paramX = randomParameters()
	paramY = randomParameters()
	config["outFile"] = paramX + paramY
	config["paramX"] = paramX
	config["paramY"] = paramY
	a = Attractortive(config, charset)
