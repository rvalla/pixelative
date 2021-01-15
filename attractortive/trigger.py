#Triggering different algorithms
import json as js
from attractortive import Attractortive


config = js.load(open("config/testing_2.json"))
a = Attractortive(config)

config = js.load(open("config/testing_3.json"))
a = Attractortive(config)
