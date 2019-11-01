from iris_plant import IrisPlant

class Cluster:

    index = None
    lastCentroid = None
    centroid = None
    plants = []

    def __init__(self, index):
        self.index = index

    def recalculateCentroid(self):
        sl = sw = pl = pw = 0
        for plant in self.plants:
            sl += plant.sepal_length
            sw += plant.sepal_width
            pl += plant.petal_length
            pw += plant.petal_width
        
        total = len(self.plants)
        self.lastCentroid = self.centroid
        self.centroid = IrisPlant(sl/total, sw/total, pl/total, pw/total, "Fake plant")

    def hasChangedCentroid(self):
        return not self.centroid.equals(self.lastCentroid)

    def printDetails(self):
        print("\nCluster número: " + str(self.index))
        content = ""
        for plant in self.plants:
            content += " " + plant.name
        print(content)
