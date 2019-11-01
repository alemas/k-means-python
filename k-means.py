import argparse
import random
import file_reader
from cluster import Cluster
from iris_plant import IrisPlant

parser = argparse.ArgumentParser()
parser.add_argument('k', metavar='k', type=int,
                    help='The number of clusters to be used')
args = parser.parse_args()

k = args.k

clusters = []
plants = file_reader.readFile()
centroids = random.sample(plants, k)

# Inicia os clusters com centroids randômicos
for i in range(0, k):
    cluster = Cluster(i)
    cluster.centroid = centroids[i]
    clusters.append(cluster)

isConverging = False
iterationsLimit = 1000
currentIteration = 0

while (currentIteration < iterationsLimit and not isConverging):

    for cluster in clusters:
        cluster.plants = []

    for plant in plants:
        # O primeiro elemento representa o cluster mais próxima e o segundo
        # representa a distância até o centróide do mesmo
        closestCluster = [0, 99999999]
        for cluster in clusters:
            centroid = cluster.centroid
            distanceToCentroid = plant.distanceToPlant(centroid)
            if (distanceToCentroid < closestCluster[1]):
                closestCluster = [cluster.index, distanceToCentroid]
        
        clusters[closestCluster[0]].plants.append(plant)

    isConverging = True

    for cluster in clusters:
        cluster.recalculateCentroid()
        isConverging = isConverging and not cluster.hasChangedCentroid()

    currentIteration += 1

if (isConverging):
    print("\nParou pois correu convergência")
else:
    print("\nParou pois atingiu limite de iterações")

print("Resultados:")

for cluster in clusters:
    cluster.printDetails()