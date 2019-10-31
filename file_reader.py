import argparse

def readFile():
    file = open("iris.data", "r")
    text = file.read()
    print(text)
