import os
import sys
import random
import array
from   item       import Item
from   items_list import ItemList


MAX_WEIGHT = 50

knapSack = [[None] * MAX_WEIGHT] * 200


def createKnapSack(itmList):

	for i in range(200):
		for j in range(MAX_WEIGHT):

			previousItem = itmList.itemArray[i-1]

			if (i == 0 or j == 0):			
				knapSack[i][j] = 0
				print("zero placed")
			
			elif (previousItem.weight <= j):
				knapSack[i][j] = max(itmList.itemArray[i-1].value + knapSack[i-1][j-itmList.itemArray[i-1].weight], 
														 knapSack[i-1][j])
				print(f'{knapSack[i][j]} inserted. (previousItem.weight < j)')
			
			else:
				knapSack[i][j] = knapSack[i-1][j]
				print(f'{str(knapSack[i][j])} inserted. (previousItem.weight > j)')
			


def main():

	itemList = ItemList()
	itemList.printList()
	createKnapSack(itemList)


if __name__ == "__main__":
    main()
