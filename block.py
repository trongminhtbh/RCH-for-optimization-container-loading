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
        self.feasibleDimentions = [1,1,1]
        self.taxibility = 0
    
    def __str__(self):
        info = "BLOCK: [{} {} {} {} {}] FEASIBLE_DIMENTIONS: {} ".format(self.length, self.width, self.height, self.weight,self.taxibility, self.feasibleDimentions) 
        combined = "CombineType: {} => (Block1: {}, Block2: {})".format(self.combineType, self.firstBlock, self.secondBlock)
        if self.combineType != 0:
            info += combined
        return info

    def __repr__(self):
        return str(self)