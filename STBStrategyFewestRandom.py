import STBStrategy
import random

random.seed()

class STBStrategyFewestRandom(STBStrategy.STBStrategy):

	def chooseAddends(self, addendsArray):
		if (len(addendsArray) < 2):
			return addendsArray[0]
		for i in range(len(addendsArray)):
			if (len(addendsArray[-i])<len(addendsArray[-i-1])):
				return addendsArray[random.randint(len(addendsArray)-i, len(addendsArray)-1)]
		return addendsArray[random.randint(0,len(addendsArray)-1)]
