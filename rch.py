from preprocessing import processBoxes
from block import Block
from input import Input
from utils import displayBoxes
import random

def sortBoxes(listBoxes):
    caseNo = random.randint(1,2)
    listBoxes.sort(key=lambda x: x.taxibility, reverse=True)
    return listBoxes

def RCH(listBoxes, n):
    for i in range(n):
        print("\n")
        print("<------------Iteration {}-------------->".format(i))
        listBoxes = processBoxes(listBoxes)
        sortBoxes(listBoxes)
        displayBoxes(listBoxes)


def main():
    data = Input(0)
    RCH(data.boxes, 9)

if __name__ == '__main__':
    main()
        