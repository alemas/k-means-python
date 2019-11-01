import argparse
from iris_plant import IrisPlant

def readFile():
    file = open("iris.data", "r")
    lines = file.readlines()
    plants = []

    for line in lines:
        attributes = line.split(',')
        if (len(attributes) > 1):
            plant = IrisPlant(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4])
            plants.append(plant)

    return plants

