import argparse
from iris_plant import IrisPlant

# Retorna um array de IrisPlant a partir do arquivo
def readFile():
    file = open("iris.data", "r")
    lines = file.readlines()
    plants = []

    for line in lines:
        attributes = line.split(',')
        if (len(attributes) > 1):
            plant = IrisPlant(float(attributes[0]), float(attributes[1]), float(attributes[2]), float(attributes[3]), attributes[4])
            plants.append(plant)

    return plants

