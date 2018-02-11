from ShutTheBox import *
from STBGameRunner import *
import STBStrategyEnd
import STBStrategyRandom
import STBStrategyAntiComputer
import STBStrategyFewestRandom
import random
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
#import plotly.plotly as py

# list1 = [1, 2, 3]
# list2 = [2, 3]
# list3 = []
#
# print getAddendsTest(5, list1)
# print getAddendsTest(5, list2)
# print getAddendsTest(5, list3)
#
# list1 = [1, 2, 3, 4]
# list2 = [2, 3]
# list3 = []
#
# print getAddendsTest(5, list1)
# print getAddendsTest(5, list2)
# print getAddendsTest(5, list3)
#
# list1 = [4, 5, 7]
# list2 = [1, 2]
# list3 = []
#
# print getAddendsTest(3, list1)
# print getAddendsTest(3, list2)
# print getAddendsTest(3, list3)
#
# list1 = [4, 5, 7]
# list2 = [1, 2]
# list3 = []
#
# print getAddendsTest(9, list1)
# print getAddendsTest(30, list2)
# print getAddendsTest(30, list3)
#
# #%%
#
# game = ShutTheBox()
#
# print game.numTiles
# print game.tileArray
# print "Die Value: " + str(game.getDieValue())
# print "Addends: " + str(game.getAddends())
#
# game = ShutTheBox(10,3,5)
#
# print game.numTiles
# print game.tileArray


numTiles = 9
dieSize = 6
numDie = 2
iterations = 1
print 'Max Tile: ' + str(numTiles)
print 'Die Size: ' + str(dieSize)
print 'Number of Die: ' + str(numDie)
print 'Iterations: ' + str(iterations)
print ' '
#
# gameRunner1 = STBGameRunner(strategy=STBStrategyAntiComputer.STBStrategyAntiComputer(),numberOfTiles=numTiles, dieSize=dieSize, numDie=numDie, iterations=iterations)
# print 'Fewest then most extreme: '
# gameRunner1.runGamesVerbose()
# # print 'Not last value addends sum average: ' + str(gameRunner1.getAverageSumTiles())
# # print 'Not last value addends sum STD: ' + str(gameRunner1.getSTDSumTiles())
# # print 'Not last value addends num average: ' + str(gameRunner1.getAverageNumTiles())
# # print 'Not last value addends num STD: ' + str(gameRunner1.getSTDNumTiles())
# # print 'Not last value addends win percentage: ' + str((gameRunner1.countZeros()/float(iterations))*100)
# # print ' '
#
# gameRunner2 = STBGameRunner(strategy=STBStrategyEnd.STBStrategyEnd(),numberOfTiles=numTiles, dieSize=dieSize, numDie=numDie, iterations=iterations)
# print 'Fewest then least extreme: '
# gameRunner2.runGamesVerbose()
# # print 'Fewest addends sum average: ' + str(gameRunner2.getAverageSumTiles())
# # print 'Fewest addends sum STD: ' + str(gameRunner2.getSTDSumTiles())
# # print 'Fewest addends num average: ' + str(gameRunner2.getAverageNumTiles())
# # print 'Fewest addends num STD: ' + str(gameRunner2.getSTDNumTiles())
# # print 'Fewest addends win percentage: ' + str((gameRunner2.countZeros()/float(iterations))*100)
# # print ' '
#
# gameRunner3 = STBGameRunner(strategy=STBStrategyFewestRandom.STBStrategyFewestRandom(),numberOfTiles=numTiles, dieSize=dieSize, numDie=numDie, iterations=iterations)
# print 'Fewest then random: '
# gameRunner3.runGamesVerbose()



# f = open("NOT LAST VALUE Num Results.txt", "w")
# f.write("\n".join(map(lambda x: str(x), gameRunner1.getResultsNumTiles())))
# f.close
#
# f = open("LAST VALUE Num Results.txt", "w")
# f.write("\n".join(map(lambda x: str(x), gameRunner2.getResultsNumTiles())))
# f.close()


gameRunner1 = STBGameRunner(numberOfTiles=numTiles, dieSize=dieSize, numDie=numDie, iterations=iterations)
gameRunner1.runGames()
print 'Most addends sum average: ' + str(gameRunner1.getAverageSumTiles())
print 'Most addends sum STD: ' + str(gameRunner1.getSTDSumTiles())
print 'Most addends num average: ' + str(gameRunner1.getAverageNumTiles())
print 'Most addends num STD: ' + str(gameRunner1.getSTDNumTiles())
print 'Most addends win percentage: ' + str((gameRunner1.countZeros()/float(iterations))*100)
print ' '

gameRunner2 = STBGameRunner(strategy=STBStrategyEnd.STBStrategyEnd(),numberOfTiles=numTiles, dieSize=dieSize, numDie=numDie, iterations=iterations)
gameRunner2.runGames()
print 'Fewest addends sum average: ' + str(gameRunner2.getAverageSumTiles())
print 'Fewest addends sum STD: ' + str(gameRunner2.getSTDSumTiles())
print 'Fewest addends num average: ' + str(gameRunner2.getAverageNumTiles())
print 'Fewest addends num STD: ' + str(gameRunner2.getSTDNumTiles())
print 'Fewest addends win percentage: ' + str((gameRunner2.countZeros()/float(iterations))*100)
print ' '

gameRunner3 = STBGameRunner(strategy=STBStrategyRandom.STBStrategyRandom(),numberOfTiles=numTiles, dieSize=dieSize, numDie=numDie, iterations=iterations)
gameRunner3.runGamesVerbose()
print 'Random addends sum average: ' + str(gameRunner3.getAverageSumTiles())
print 'Random addends sum STD: ' + str(gameRunner3.getSTDSumTiles())
print 'Random addends num average: ' + str(gameRunner3.getAverageNumTiles())
print 'Random addends num STD: ' + str(gameRunner3.getSTDNumTiles())
print 'Random addends win percentage: ' + str((gameRunner3.countZeros()/float(iterations))*100)
print ' '


# f = open("Num Results (Most, Fewest, Random)", "w")
# lines_of_text = ["Most, Fewest, Random" + "\n"]
# for i in range(iterations):
#     lines_of_text += (str(gameRunner1.getResultsNumTiles()[i]) + ", " + str(gameRunner2.getResultsNumTiles()[i]) + ", " + str(gameRunner3.getResultsNumTiles()[i]) + "\n")
# f.writelines(lines_of_text)
# f.close()

f = open("Most Addends SUM Results.txt", "w")
f.write("\n".join(map(lambda x: str(x), gameRunner1.getResultsSumTiles())))
f.close

f = open("Fewest Addends SUM Results.txt", "w")
f.write("\n".join(map(lambda x: str(x), gameRunner2.getResultsSumTiles())))
f.close()

f = open("Random Addends SUM Results.txt", "w")
f.write("\n".join(map(lambda x: str(x), gameRunner3.getResultsSumTiles())))
f.close()

# def WriteListToCSV(csv_file,data_list):
#     try:
#         with open(csv_file, 'w') as csvfile:
#             writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
#             #writer.writerow(csv_columns)
#             for data in data_list:
#                 writer.writerow(data)
#     except IOError as (errno, strerror):
#             print("I/O error({0}): {1}".format(errno, strerror))
#     return
#
# csv_columns = ['Row','Name','Country']
# csv_data_list = [[gameRunner1.getResultsNumTiles()], [gameRunner2.getResultsNumTiles()], [gameRunner3.getResultsNumTiles()]]
#
# currentPath = os.getcwd()
# csv_file = currentPath + "/csv/Names.csv"
#
#
# WriteListToCSV(csv_file,csv_data_list)

#plt.hist(gameRunner.getAverageSumTiles)
#plt.title("Random Sum Results")
#plt.xlabel("Value")
#plt.ylabel("Frequency")

#fig = plt.gcf()
#plot_url = py.plot_mpl(fig, filename='Random-Results-Histogram')
