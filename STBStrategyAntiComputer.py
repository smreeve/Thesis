import STBStrategy

class STBStrategyAntiComputer(STBStrategy.STBStrategy):

	def chooseAddends(self, addendsArray):
		if (len(addendsArray) < 2):
			return addendsArray[0]
		for i in range(len(addendsArray)):
			if (len(addendsArray[-i])<len(addendsArray[-i-1])):
				return addendsArray[-i]
		return addendsArray[0]
