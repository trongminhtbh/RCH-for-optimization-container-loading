from input import Input
from BOX import BOX
from space import space
Data = Input(1,0)
box0 = BOX(Data,0)
(L,W,H)=Data.contdim
S=space(0,0,0,L,W,H)
ori = box0.Possible_Oriatation(S)
print(ori)
f=[]  # Objective function
B=[]  # All six bloks
Ks=[] # Blok quantity