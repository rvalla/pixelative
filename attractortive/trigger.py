#triggering an attractor construction
import json as js
from attractortive import Attractortive
from metaattractortive import MetaAttractortive

#loading character code set
charset = js.load(open("config/characterset.json"))

#loading configuration file
config = js.load(open("config/metafound/20210124_04.json"))

#creating and painting the attractor
a = MetaAttractortive(config, charset)
