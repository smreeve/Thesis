import STBStrategy
import random

random.seed()

class STBStrategyRandom(STBStrategy.STBStrategy):

	def chooseAddends(self, addendsArray):
		return addendsArray[random.randint(0,len(addendsArray)-1)]
