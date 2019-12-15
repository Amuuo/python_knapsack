import sys
import os
import random as rd
from item import Item

class ItemList:


	def __init__(self):
		
		#self.list = []
		rd.seed()
		self.itemArray = []

		# this loop will generate 200 random items to use as input for the algorithm
		# range for cost:      1-100
		# range for weight:    1-50
		# range for address.x: 1-50
		# range for address.y: 1-50
		for i in range(200):
			self.itemArray.append(Item(rd.randrange(1, 100),  \
																 rd.randrange(1, 50) ,  \
												        (rd.randrange(1, 50) , rd.randrange(1, 50)))
														)
		
		for itm in self.itemArray:
			itm.calculateDistanceToCities(self.itemArray)

	def printList(self):
		for i, x in enumerate(self.itemArray):
			print(f'Item #{i}: weight: {x.weight}, cost: {x.cost}, address: {x.address}')
