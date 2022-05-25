from block import Block
from input import Input
from utils import displayBoxes
import numpy as np
import random


def combineBlocksSharingTwoDimention(block1, block2):
    caseNo = random.randint(1,2)
    if block1.length == block2.length and block1.width == block2.width:
        temp = Block(block1.length, block1.width, block1.height+block2.height, block1.weight+block2.weight)
        temp.combineType = caseNo
        temp.firstBlock = block1
        temp.secondBlock = block2
        return temp

    if block1.length == block2.length and block1.height == block2.height:
        temp = Block(block1.length, block1.width + block2.width, block1.height, block1.weight+block2.weight)
        temp.combineType = caseNo
        temp.firstBlock = block1
        temp.secondBlock = block2
        return temp

    if block1.width == block2.width and block1.height == block2.height:
        temp = Block(block1.length + block2.length, block1.width, block1.height + block2.height, block1.weight+block2.weight)
        temp.combineType = caseNo
        temp.firstBlock = block1
        temp.secondBlock = block2
        return temp
    return None

def combineBlocksSharingAllDimention(block1, block2):
    caseNo = random.randint(3,8) 
    if caseNo == 3 or caseNo == 4:
        temp = Block(block1.length + block2.length, block1.width, block1.height, block1.weight+block2.weight)
        temp.combineType = caseNo
        temp.firstBlock = block1
        temp.secondBlock = block2
        return temp

    if caseNo == 5 or caseNo == 6:
        temp = Block(block1.length, block1.width + block2.width, block1.height, block1.weight+block2.weight)
        temp.combineType = caseNo
        temp.firstBlock = block1
        temp.secondBlock = block2
        return temp

    if caseNo == 7 or caseNo == 8:
        temp = Block(block1.length, block1.width, block1.height + block2.height, block1.weight+block2.weight)
        temp.combineType = caseNo
        temp.firstBlock = block1
        temp.secondBlock = block2
        return temp

def compareBox(box1, box2):
    if box1.length == box2.length and box1.width == box2.width and box1.height == box2.height:
        return 1
    if (box1.length == box2.length and box1.width == box2.width) or (box1.width == box2.width and box1.height == box2.height) or (box1.length == box2.length and box1.height == box2.height):
        return 2
    return 0

def processBoxes(listBoxes):
    result = []
    caseNo = random.randint(1,3)
    if caseNo == 1:
        return listBoxes
    if caseNo == 2:
        while listBoxes != []:
            box = listBoxes[0]
            for item in listBoxes[1:]:
                type = compareBox(box, item)
                if type ==2:
                    newBox = combineBlocksSharingTwoDimention(box, item)
                    result.append(newBox)
                    listBoxes.remove(box)
                    listBoxes.remove(item)
                    break
            if box in listBoxes:
                result.append(box)
                listBoxes.remove(box)
        return result

    if caseNo == 3:
        while listBoxes != []:
            box = listBoxes[0]
            for item in listBoxes[1:]:
                type = compareBox(box, item)
                if type ==1:
                    newBox = combineBlocksSharingAllDimention(box, item)
                    result.append(newBox)
                    listBoxes.remove(box)
                    listBoxes.remove(item)
                    break
            if box in listBoxes:
                result.append(box)
                listBoxes.remove(box)
        return result



def main():
    data = Input(0)
    combineBoxes = processBoxes(data.boxes)
    displayBoxes(combineBoxes)

if __name__ == '__main__':
    main()
        