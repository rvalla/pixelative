import os
import json as js
import random as rd
#creating json configuration files for metaattractors...

n = 50
path = "config/found/"
output_path = "output/metafound/"
prefix = "20" #files to read...

width = 1080
height = 1080
margin = 50
points = 100000
base_depth = 2
loop = 10000
originX = 0
originY = 0
paramMode = "values"
colorMode = "additive"
facered = 0
facegreen = 0
faceblue = 0
backred = 255
backgreen = 255
backblue = 255

filename = "20241110_"
f_list = []
for f in os.listdir(path):
    if f.startswith(prefix):
        f_list.append(f)

for f in range(n):
    depth = base_depth + rd.randint(0,3)
    selection = rd.sample(f_list, depth)
    attractors = []
    name = filename + "{:03}".format(f) + ".json"
    file = open("config/metafound/" + name, "w")
    file.write('{\n')
    file.write('"reference": "-",\n')
    file.write('"outPath": "' + output_path + '",\n')
    file.write('"outFile": "' + name[:len(name)-5] + '",\n')
    file.write('"width": ' + str(width) + ',\n')
    file.write('"height": ' + str(height) + ',\n')
    file.write('"margin": ' + str(margin) + ',\n')
    file.write('"points": ' + str(points) + ',\n')
    subdivisions = ''
    facereds = ''
    facegreens = ''
    faceblues = ''
    for i in range(depth):
        subdivisions += str(points*pow(2,i))
        facereds += str((facered + rd.randint(0,100))%256)
        facegreens += str((facegreen + rd.randint(0,100))%256)
        faceblues += str((faceblue + rd.randint(0,100))%256)
        if i < depth - 1:
            subdivisions += ','
            facereds += ','
            facegreens += ','
            faceblues += ','
    file.write('"depth": ' + str(depth) + ',\n')
    file.write('"subdivisions": "' + subdivisions + '",\n')
    file.write('"loop": ' + str(loop) + ',\n')
    file.write('"originX": ' + str(originX) + ',\n')
    file.write('"originY": ' + str(originY) + ',\n')
    file.write('"paramMode": "' + paramMode + '",\n')
    file.write('"paramCodeX": "",\n')
    file.write('"paramCodeY": "",\n')
    for s in selection:
        attractors.append(js.load(open(path + s)))
    for i in range(depth):
        file.write('"paramX_' + str(i+1) + '": "' + attractors[i]["paramX"] + '",\n')
        file.write('"paramY_' + str(i+1) + '": "' + attractors[i]["paramY"] + '",\n')
    file.write('"colorMode": "' + colorMode + '",\n')
    file.write('"facered": "' + facereds + '",\n')
    file.write('"facegreen": "' + facegreens + '",\n')
    file.write('"faceblue": "' + faceblues + '",\n')
    file.write('"backred": ' + str(backred) + ',\n')
    file.write('"backgreen": ' + str(backgreen) + ',\n')
    file.write('"backblue": ' + str(backblue) + '\n')
    file.write('}\n')
    file.close
