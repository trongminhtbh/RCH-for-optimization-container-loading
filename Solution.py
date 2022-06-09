from numpy.random import choice
from space import space
from block import Block
from Blok import Blok

class Solution:
    DisFromFront=[]
    def __init__(self, value ):
        self.value = value
        self.h_score = None
        self.VU=None
        self.WCG=None
        self.DFF=None
        self.Loading_Results=None

    def loading(self,Data):
    #### loading hurestic ###
        space.reset()
        BOX.reset()
        Blok.reset()
        (L,W,H)=Data.contdim
        S=space(0,0,0,L,W,H)
        BOXS=[]
        for j in self.value:
            BOXS.append(BOX(Data,j))
    
        while len(space.remainlist)!=0 or BOX.Is_unloaded_BOX():
            S=S.merge()
            j=0
            while(j<Data.ntype and len(space.remainlist)!=0):
                currentbox=BOXS[j]
                
                if (currentbox.quantity>0 and currentbox.Can_Load(Data,S)):
                    BBlok=currentbox.Best_Blok(S)
                    BBlok.partition(S)
                    if len(space.remainlist)!=0:
                        S=space.curentspace()
                        j=0
                    else:
                        break
                        
                    S=S.merge()
                    #j+=1
                else:
                    j+=1
                    
            S.waste()
            if len(space.remainlist)!=0:
                S=space.curentspace()
            else:
                break