import numpy as np
import random
random.seed(5)

class ShutTheBox:
	def __init__(self, numberOfTiles=8, dieSize=6, numDie=2): #this is where you would input a strategy
		self.numTiles = numberOfTiles
		self.dieSize = dieSize
		self.numDie = numDie
		self.tileArray = range(1,self.numTiles + 1)
		self.addends = []
		# self.predictedRolls = [11,7,3,6,7,7,7,3,10,8,9,10,8,8,10,7,4,6,10,4,3,6,6,8,8,4,7,5,5,8,4,10,5,8,12,10,4,7,11,11,6,8,5,4,10,12]
		self.predictedRolls = [7,6,7,4,9,6,5,11,3,4,6,6,7,6,5,5,10,6,8]
		self.dieValue = 0
		self.rollDie()



	# def rollDie(self):
	# 	dieTotal = self.predictedRolls.pop()
	# 	self.dieValue = dieTotal
	# 	self.addends = self.findAddends(self.dieValue, self.tileArray)

	def rollDie(self):
		dieTotal = 0
		for i in range(self.numDie):
			dieTotal += random.randint(1, self.dieSize)
		self.dieValue = dieTotal
		self.addends = self.findAddends(self.dieValue, self.tileArray)

	def getAddends(self):
		return self.addends

	def getDieValue(self):
		return self.dieValue

	def getTiles(self):
		return self.tileArray

	def sumTiles(self):
		currentSum = 0
		for i in range(len(self.tileArray)):
			currentSum += self.tileArray[i]
		return currentSum

	def removeTiles(self, tilesToRemove):
		for i in range(len(tilesToRemove)):
			if tilesToRemove[i] in self.tileArray:
				self.tileArray.remove(tilesToRemove[i])
			else: return False
		self.rollDie()
		return True

	def removeTilesVerbose(self, tilesToRemove):
		print "Current Tiles:" + str(self.tileArray)
		print "Die Value:" + str(self.dieValue)
		print "Addends:" + str(self.addends)
		print "tilesToRemove: " + str(tilesToRemove)
		for i in range(len(tilesToRemove)):
			if tilesToRemove[i] in self.tileArray:
				self.tileArray.remove(tilesToRemove[i])
			else: return False
		self.rollDie()
		return True

	def findAddends(self, dieRoll, tiles):
		if len(tiles) == 0:
			return []
		if tiles[0] == dieRoll:
			return [[tiles[0]]]
		if tiles[0] > dieRoll:
			return []

		workingCombinations = []

		useIt = self.findAddends(dieRoll - tiles[0], tiles[1:])

		if len(useIt) > 0:
			for i in range(len(useIt)):
				workingCombinations += [[tiles[0]]+useIt[i]]

		loseIt = self.findAddends(dieRoll, tiles[1:])
		workingCombinations += loseIt

		return workingCombinations



def getAddendsBoolean(dieRoll, tiles):
	if len(tiles) == 0:
		return False
	if tiles[0] == dieRoll:
		return True
	if tiles[0] > dieRoll:
		return False

	loseIt = getAddends(dieRoll, tiles[1:])
	useIt = getAddends(dieRoll - tiles[0], tiles[1:])

	return (useIt or loseIt)

def getAddendsTest(dieRoll, tiles):
	if len(tiles) == 0:
		return []
	if tiles[0] == dieRoll:
		return [[tiles[0]]]
	if tiles[0] > dieRoll:
		return []

	workingCombinations = []

	loseIt = getAddendsTest(dieRoll, tiles[1:])
	workingCombinations += loseIt
	useIt = getAddendsTest(dieRoll - tiles[0], tiles[1:])

	if len(useIt) > 0:
		for i in range(len(useIt)):
			workingCombinations += [[tiles[0]]+useIt[i]]

	return workingCombinations
