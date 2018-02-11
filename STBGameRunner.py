import ShutTheBox
import STBStrategy
import STBStrategyEnd
import STBStrategyRandom
import numpy as np

class STBGameRunner:

	def __init__(self, strategy=STBStrategy.STBStrategy(), numberOfTiles=8, dieSize=6, numDie=2, iterations=2000):
		self.numTiles = numberOfTiles
		self.dieSize = dieSize
		self.numDie = numDie
		self.strategy = strategy
		self.iterations = iterations
		self.resultsNumTiles = []
		self.resultsSumTiles = []


	def runGames(self):
		for i in range(self.iterations):
			game = ShutTheBox.ShutTheBox(self.numTiles, self.dieSize, self.numDie)
			while len(game.getAddends()) > 0:
				game.removeTiles(self.strategy.chooseAddends(game.getAddends()))
			self.resultsNumTiles += [len(game.getTiles())]
			self.resultsSumTiles += [game.sumTiles()]


	def runGamesVerbose(self):
		for i in range(self.iterations):
			game = ShutTheBox.ShutTheBox(self.numTiles, self.dieSize, self.numDie)
			while len(game.getAddends()) > 0:
				game.removeTilesVerbose(self.strategy.chooseAddends(game.getAddends()))
			self.resultsNumTiles += [len(game.getTiles())]
			print "Number of Tiles Result: " + str(len(game.getTiles()))
			self.resultsSumTiles += [game.sumTiles()]
			print "Sum of Tiles Result: " + str(game.sumTiles())
			print ' '

	def getResultsNumTiles(self):
		return self.resultsNumTiles

	def getAverageNumTiles(self):
		return np.mean(self.resultsNumTiles)

	def getResultsSumTiles(self):
		return self.resultsSumTiles

	def getAverageSumTiles(self):
		return np.mean(self.resultsSumTiles)

	def getSTDSumTiles(self):
		return np.std(self.resultsSumTiles)

	def getSTDNumTiles(self):
		return np.std(self.resultsNumTiles)

	def countZeros(self):
		zeroCount = 0
		for i in range(self.iterations):
			if (self.resultsNumTiles[i] == 0):
				zeroCount += 1
		return zeroCount
