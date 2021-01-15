#Triggering different algorithms
import json as js
from attractortive import Attractortive

charset = js.load(open("config/characterset.json"))
config = js.load(open("config/spratt/spaceship.json"))
a = Attractortive(config, charset)
