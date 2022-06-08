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

    def Can_Load(self,space):
        # check if the volume of one box in less than or equal to the current remianig space volume
        check=0
        if space.volume>= self.length*self.width*self.height :
            if sum(map(lambda x: x[0] , self.Possible_Oriatation(space) ))>=1:
                check=1
        return check


    def Possible_Oriatation(self,S): 
        ori=[[0] for _ in range(6)]
        #Ori #1 y lenght x width
        #Ori #2 y lenght x hight
        if self.length <= S.W:
            if self.width <= S.L and self.height<=S.H and self.feasibleDimentions[2]==1:
                ori[0]=[1,self.length,self.height,self.width] #(w,h,l)
                
            if self.height<= S.L and self.width<=S.H and self.feasibleDimentions[1]==1:
                ori[1]=[1,self.length,self.width,self.height]
    
        #Ori #3 y width x lenght
        #Ori #4 y width x hight
        if self.width <= S.W:
            
            if self.length<= S.L and self.height<=S.H and self.feasibleDimentions[2]==1:
                ori[2]=[1,self.width,self.height,self.length]
                
            if self.height<= S.L and self.length<=S.H and self.feasibleDimentions[0]==1:
                ori[3]=[1,self.width,self.length,self.height]
        
        #Ori #5 y hight x lenght
        #Ori #6 y hight x width
        if self.height<= S.W:
            
            if self.length<= S.L and self.width<=S.H and self.feasibleDimentions[1]==1:
                ori[4]=[1,self.height,self.width,self.length]
                
            if self.width <= S.L and self.length<=S.H and self.feasibleDimentions[0]==1:
                ori[5]=[1,self.height,self.length,self.width]
        
        return ori