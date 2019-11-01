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

for i in range(0, k):
    cluster = Cluster(i)
    cluster.centroid = centroids[i]
    clusters.append(cluster)
    print(cluster)

for cluster in clusters:
    centroid = cluster.centroid
    for plant in plants:
        
