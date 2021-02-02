#looking for some strange meta attractors
import copy
import math
import itertools
import json as js
from metaattractortive import MetaAttractortive

#loading the character code set
charset = js.load(open("config/characterset.json"))

#loading default configuration
inconfig = js.load(open("config/metasearch/ms_20210202_01.json"))
outconfig = copy.deepcopy(inconfig)
metadepth = inconfig["depth"]
search = inconfig["outFile"]
steps = range(metadepth)
permutations = list(itertools.permutations(steps))

def metaPermutation():
	for i in range(len(permutations)):
		for d in range(len(steps)):
			outkeyx = "paramX_" +  str(d + 1)
			inkeyx = "paramX_" +  str(permutations[i][d] + 1)
			outkeyy = "paramY_" +  str(d + 1)
			inkeyy = "paramY_" +  str(permutations[i][d] + 1)
			outconfig[outkeyx] = inconfig[inkeyx]
			outconfig[outkeyy] = inconfig[inkeyy]
		outconfig["outFile"] = search + str(i) + "_" + str(permutations[i])
		ma = MetaAttractortive(outconfig, charset)

metaPermutation()
