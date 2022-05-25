import numpy as np

class Block:
    def __init__(self, length, width, height, weight ):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.isCombined = False
        self.combineType = 0
        self.firstBlock = None
        self.secondBlock = None
    
    def __str__(self):
        info = "BLOCK: [{} {} {} {}] combineType: {} => (Block1: {}, Block2: {})".format(self.length, self.width, self.height, self.weight, self.combineType, self.firstBlock, self.secondBlock)
        return info

    def __repr__(self):
        return str(self)