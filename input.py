import numpy as np
import os
import array
from block import Block
dir_path = os.path.dirname(os.path.realpath(__file__))
class Input:

    def __init__(self,ProblemNo):
        self.contdim=[]
        self.ntype=[]
        self.boxes=[]
     ## Obtain Data ####
        ifile=open(dir_path+'\data.txt', "r")
        lines=ifile.readlines()
        self.ntype=int(lines[1].split()[0])
        lines=lines[ProblemNo*(self.ntype+2):(ProblemNo+1)*(self.ntype+2)]
        ifile.close()
    ### Convert strings to numbers ###
        self.contdim=lines[0].split()
        self.contdim=[int(a) for a in self.contdim]
        for line in lines[2:2+self.ntype]:
            input = line.split()
            data = [float(item) for item in input]
            feasibleDimentions = [int(data[1]), int(data[3]), int(data[5])]
            tempBlock = Block(data[0],data[2], data[4], data[7])
            tempBlock.feasibleDimentions = feasibleDimentions
            tempBlock.taxibility = data[8]
            self.boxes.append(tempBlock)
   ##### generate the constraint     
        self.Top_Bot=np.ones((self.ntype,self.ntype ))
        inx1=np.random.randint(0,self.ntype , self.ntype)
        inx2=np.random.randint(0,self.ntype , self.ntype)
        self.Top_Bot[inx1,inx2]=0


def main():
    data = Input(0)
    print(data.boxes)

if __name__ == '__main__':
    main()