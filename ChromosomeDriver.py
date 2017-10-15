__author__ = 'yves0_000'

import random
import math

class Chromosome:

    def __init__(self, geneticData):
        self.geneticData = geneticData

    def replicate(self):
        temp = []
        for i in range(len(self.geneticData)):
            temp.append(self.geneticData[i])
        chromosome = Chromosome(temp)
        return chromosome

    def mutate(self):
        replaceIndex = random.randint(1, len(self.geneticData)-1)
        self.geneticData[replaceIndex] = random.randint(1, 2 * math.pow(10, 9))
        return

    def getData(self):
        dataString = ''
        for i in range(len(self.geneticData)):
            dataString += str(self.geneticData[i]) + ' '
        return dataString

    def crossover(self, chromosome):
        if len(self.geneticData) == len(chromosome.geneticData):
            for i in range(random.randint(1, len(self.geneticData)-1), len(self.geneticData)):
                temp = self.geneticData[i]
                self.geneticData[i] = chromosome.geneticData[i]
                chromosome.geneticData[i] = temp
        return

c1 = Chromosome([1, 2, 3, 4, 5, 6])
c2 = Chromosome([11, 12, 13, 14, 15, 16])
c3 = c1.replicate()
c3.mutate()
print 'c3 = ', c3.getData()
c1.crossover(c2)
print 'c1 = ', c1.getData()
print 'c2 = ', c2.getData()








