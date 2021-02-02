#triggering an attractor construction
import json as js
from attractortive import Attractortive

#loading character code set
charset = js.load(open("config/characterset.json"))

#loading configuration file
config = js.load(open("config/found/20210202_03.json"))

#creating and painting the attractor
a = Attractortive(config, charset)
