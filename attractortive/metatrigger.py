#triggering an attractor construction
import json as js
import os
from metaattractortive import MetaAttractortive

#loading character code set
config_path = "config/metafound/"
charset = js.load(open("config/characterset.json"))

#loading configuration files and creating attractors
config_files = []
for f in os.listdir("config/metafound"):
    if f.startswith("20241110_"):
        config_files.append(f)

for f in config_files:
    config = js.load(open(config_path + f))
    a = MetaAttractortive(config, charset)
