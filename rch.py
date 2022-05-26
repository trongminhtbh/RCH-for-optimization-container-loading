from preprocessing import processBoxes
from block import Block
from input import Input
from utils import displayBoxes

def RCH(listBoxes, n):
    for i in range(n):
        print("\n")
        print("<------------Iteration {}-------------->".format(i))
        listBoxes = processBoxes(listBoxes)
        displayBoxes(listBoxes)


def main():
    data = Input(0)
    RCH(data.boxes, 9)

if __name__ == '__main__':
    main()
        