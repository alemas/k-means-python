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