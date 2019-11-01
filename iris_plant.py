import math

class IrisPlant:

    sepal_length = 0
    sepal_width = 0
    petal_length = 0
    petal_width = 0
    name = ""
    
    def __init__(self, sl, sw, pl, pw, name):
        self.sepal_length = sl
        self.sepal_width = sw
        self.petal_length = pl
        self.petal_width = pw
        self.name = name

    # Distância euclidiana entre uma planta e outra
    def distanceToPlant(self, plant):
        return math.sqrt(pow(self.sepal_length - plant.sepal_length, 2) + 
                        pow(self.sepal_width - plant.sepal_width, 2) + 
                        pow(self.petal_length - plant.petal_length, 2) + 
                        pow(self.petal_width - plant.petal_width, 2))

    def equals(self, plant):
        return (self.sepal_length == plant.sepal_length and
                self.sepal_width == plant.sepal_width and
                self.petal_length == plant.petal_width and
                self.petal_width == plant.petal_width)
    
    def copy(self):
        return IrisPlant(self.sepal_length, self.sepal_width, self.petal_length, self.petal_width, self.name)