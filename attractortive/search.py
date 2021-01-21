#looking for some strange attractors
import json as js
import random as rd
from attractortive import Attractortive

search = "005_" #number to indentify search
count = 1000 #number of intends
paramInterval = 2.0 #limiting the random values to (-paramInterval, paramInterval)
paramVarLimit = 0.1 #limiting the random variations to (-paramVarLimit, paramVarLimit)

#loading the character code set
charset = js.load(open("config/characterset.json"))

#loading default configuration
configSearch = js.load(open("config/search/searching.json"))
configVariations = js.load(open("config/variations/variations.json"))

#function to get random values
def getRandomValue(interval):
	v = rd.uniform(-interval, interval)
	return round(v, 3)

#function to get random variations
def getRandomVariation(value, variation):
	v = rd.uniform(-variation, variation)
	value += v
	return round(value, 3)

#function to create a random parameters list
def randomParameters():
	parameters = ""
	for p in range(10):
		parameters += str(getRandomValue(paramInterval))
		if p < 9:
			parameters += ","
	return parameters

#function to create a random parameters list
def randomVariation(list):
	parameters = list.split(",")
	newparameters = ""
	for p in range(10):
		newparameters += str(getRandomVariation(float(parameters[p]), paramVarLimit))
		if p < 9:
			newparameters += ","
	return newparameters

#the loop to look for attractors
def randomSearch():
	for t in range(count):
		paramX = randomParameters()
		paramY = randomParameters()
		configSearch["outFile"] = search + paramX + paramY
		configSearch["paramX"] = paramX
		configSearch["paramY"] = paramY
		a = Attractortive(configSearch, charset)

#the loop to look for attractors' variations
def variationSearch():
	for t in range(count):
		paramX = randomVariation(configVariations["paramX"])
		paramY = randomVariation(configVariations["paramY"])
		configVariations["outFile"] = search + paramX + paramY
		configVariations["paramX"] = paramX
		configVariations["paramY"] = paramY
		a = Attractortive(configVariations, charset)

randomSearch()
variationSearch()
