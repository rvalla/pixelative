import os
#creating json configuration files for found attractors...

path = "output/search"
output_path = "output/found/"
prefix = "018" #files to read...

width = 1080
height = 1080
margin = 50
points = 1500000
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

filename = "20242310_"
f_list = []
for f in os.listdir(path):
    if f.startswith(prefix):
        f_list.append(f[4:len(f)-4])

for f in range(len(f_list)):
    name = filename + "{:03}".format(f) + ".json"
    parameters = f_list[f].split("__")
    file = open("config/found/" + name, "w")
    file.write('{\n')
    file.write('"reference": "-",\n')
    file.write('"outPath": "' + output_path + '",\n')
    file.write('"outFile": "' + name[:len(name)-5] + '",\n')
    file.write('"width": ' + str(width) + ',\n')
    file.write('"height": ' + str(height) + ',\n')
    file.write('"margin": ' + str(margin) + ',\n')
    file.write('"points": ' + str(points) + ',\n')
    file.write('"loop": ' + str(loop) + ',\n')
    file.write('"originX": ' + str(originX) + ',\n')
    file.write('"originY": ' + str(originY) + ',\n')
    file.write('"paramMode": "' + paramMode + '",\n')
    file.write('"paramCodeX": "",\n')
    file.write('"paramCodeY": "",\n')
    file.write('"paramX": "' + parameters[0] + '",\n')
    file.write('"paramY": "' + parameters[1] + '",\n')
    file.write('"colorMode": "' + colorMode + '",\n')
    file.write('"facered": ' + str(facered) + ',\n')
    file.write('"facegreen": ' + str(facegreen) + ',\n')
    file.write('"faceblue": ' + str(faceblue) + ',\n')
    file.write('"backred": ' + str(backred) + ',\n')
    file.write('"backgreen": ' + str(backgreen) + ',\n')
    file.write('"backblue": ' + str(backblue) + '\n')
    file.write('}\n')
    file.close
