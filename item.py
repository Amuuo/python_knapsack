import os
import sys
import math



class Item:


	def __init__(self, cost, weight, address):
			
		self.cost    = cost
		self.weight  = weight
		self.address = address
		self.value   = 0	

	
	def calculateDistanceToCities(self, itemList):
								
		for i, itm in enumerate(itemList):
			
			distanceToCity = int(math.sqrt(                      \
				math.pow((self.address[0] - itm.address[0]), 2) + \
				math.pow((self.address[1] - itm.address[1]), 2)))
						
			#print(f'Distance to city #{x}: {distance}')
			
			value = int(itm.cost*.10 - distanceToCity)
			
			#sets the value to zero if it's below 0
			if (value <= 0): 
				value = 0
			
			else:
				print(f'Item {i} - value: {value}')

			
	