#triggering an attractor construction
import json as js
from metaattractortive import MetaAttractortive

#loading character code set
charset = js.load(open("config/characterset.json"))

#loading configuration file
config = js.load(open("config/metafound/20210315_01.json"))

#creating and painting the attractor
a = MetaAttractortive(config, charset)
