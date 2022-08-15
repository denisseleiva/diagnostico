import os

ruta = os.path.join("farmers-protest-tweets-2021-03-5.json")
with open(ruta, 'rt') as file:
    lineas = file.readlines()

print(len(lineas))

#for i in range(1):
    #text = lineas[i].split(",")
    #print(text)
