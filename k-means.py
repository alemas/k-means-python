import argparse
import file_reader
import cluster
import iris_plant

parser = argparse.ArgumentParser()
parser.add_argument('k', metavar='k', type=int,
                    help='The number of clusters to be used')
args = parser.parse_args()

k = args.k

clusters = []

plants = file_reader.readFile()

print(plants)

# for i in range(0, k):
#     clusters[i] = Cluster()