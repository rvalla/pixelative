#triggering an attractor construction
import json as js
import os
from attractortive import Attractortive

#loading character code set
config_path = "config/found/"
charset = js.load(open("config/characterset.json"))

#loading configuration files and creating attractors
config_files = []
for f in os.listdir("config/found"):
    if f.startswith("20240114_"):
        config_files.append(f)

for f in config_files:
    config = js.load(open(config_path + f))
    a = Attractortive(config, charset)
