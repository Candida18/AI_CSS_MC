# At a university, Professor Symons wishes to employ two people, John and Mary, to grade papers for his classes. John is a graduate student and can grade 20 papers per hour; John earns $15 per hour for grading papers. Mary is an post-doctoral associate and can grade 30 papers per hour; Mary earns $25 per hour for grading papers. Each must be employed at least one hour a week to justify their employment.
# If Prof. Symons has at least 110 papers to be graded each week, how many hours per week should he employ each person to minimize the cost?


import random as r
import sys

geneCount = 2
chromosomeCount = 6
minChromosomes = [sys.maxsize] * geneCount
minValue = sys.maxsize


def objectiveFunction(chromosome):
    return (15*chromosome[0] + 25 *chromosome[1])

def condition(chromosome):
    return (20*chromosome[0] + 30*chromosome[1]) >= 110

def randomFloatGenerator():
    return r.random()


def randomIntGenerator(x, y):
    return r.randint(x, y)


def selection(cumulative, random_value):
    for i in range(len(cumulative)):
        if random_value < cumulative[i]:
            return i


def findCrossoverChromosomes(R, crossoverRate):
    crossoverChromosomes = []
    for i in range(len(R)):
        if R[i] < crossoverRate:
            crossoverChromosomes.append(i)
    return crossoverChromosomes


def crossoverCombination(crossoverChromosomes):
    combinations = []
    for i in range(0, len(crossoverChromosomes) - 1):
        for j in range(i + 1, len(crossoverChromosomes)):
            combinations.append([crossoverChromosomes[i], crossoverChromosomes[j]])
    return combinations


def crossoverInterchange(chromosome1, chromosome2, crossoverPoint):
    newChromosome = []
    for i in range(0, crossoverPoint + 1):
        newChromosome.append(chromosome1[i])
    for j in range(crossoverPoint + 1, len(chromosome2)):
        newChromosome.append(chromosome2[j])
    return newChromosome


def doCrossover(chromosomes, crossoverChromosomes):
    combinations = crossoverCombination(crossoverChromosomes)
    crossoverPoints = []
    for _ in range(len(combinations)):
        crossoverPoints.append(randomIntGenerator(0, len(chromosomes[0]) - 2))

    # Crossover between combinations
    for combination in combinations:
        chromosomes[combination[0]] = crossoverInterchange(
            chromosomes[combination[0]],
            chromosomes[combination[1]],
            crossoverPoints[combinations.index(combination)],
        )
    return chromosomes


def mutate(chromosomes, mutationValues):
    temp = 0
    k = 0
    for i in range(len(chromosomes)):
        for j in range(len(chromosomes[i])):
            if k == mutationValues[temp]:
                chromosomes[i][j] = randomIntGenerator(1, 10)
                temp += 1
                if temp == len(mutationValues):
                    return chromosomes
            k += 1
    return chromosomes


def getChromosome(chromosomes, minValue, minChromosomes):
    for chromosome in chromosomes:
        if minValue > abs(objectiveFunction(chromosome)) and condition(chromosome):
        
            minValue = abs(objectiveFunction(chromosome))
            minChromosomes = chromosome
    return minValue, minChromosomes


def geneticAlgorithm(geneCount, chromosomeCount, minValue, minChromosomes):
    chromosomes = []
    newChromosomes = []
    F_obj = []
    fitness = []
    probability = []
    cumulative = []
    R = []
    crossoverRate = 0.30
    mutationRate = 0.20
    randomMutation = []

    for i in range(chromosomeCount):
        chromosomes.append([])
        newChromosomes.append([])
        for j in range(geneCount):
            chromosomes[i].append(randomIntGenerator(1, 60))

    for i in range(chromosomeCount):
        F_obj.append(abs(objectiveFunction(chromosomes[i])))

    for i in range(chromosomeCount):
        fitness.append(round(1 / (1 + F_obj[i]), 4))
    totalFitness = round(sum(fitness), 4)

    for i in range(chromosomeCount):
        probability.append(round(fitness[i] / totalFitness, 4))
        cumulative.append(0)
    for i in range(chromosomeCount):
        cumulative[i] = round(sum(probability[0 : i + 1]), 4)

    for i in range(chromosomeCount):
        R.append(round(randomFloatGenerator(), 4))

    for i in range(chromosomeCount):
        newChromosomes[i] = chromosomes[selection(cumulative, R[i])]
    chromosomes = newChromosomes

    R = []
    for i in range(chromosomeCount):
        R.append(round(randomFloatGenerator(), 3))

    crossoverChromosomes = findCrossoverChromosomes(R, crossoverRate)
    if len(crossoverChromosomes) > 2:
        chromosomes = doCrossover(chromosomes, crossoverChromosomes)

    totalGenes = chromosomeCount * geneCount
    mutationCount = int(totalGenes * mutationRate)

    for i in range(mutationCount):
        randomMutation.append(randomIntGenerator(0, totalGenes - 1))
    randomMutation.sort()
    chromosomes = mutate(chromosomes, randomMutation)

    minValue, minChromosomes = getChromosome(chromosomes, minValue, minChromosomes)
    return minValue, minChromosomes


for iteration in range(150):
    print(f"🧬 GENERATION {iteration + 1}")
    minValue, minChromosomes = geneticAlgorithm(
        geneCount, chromosomeCount, minValue, minChromosomes
    )
    print("Critical Point : ",minChromosomes)
    print("Minimum Cost : ₹", minValue)
    print("\n")
    

print("\n🔬 FINAL RESULT \n")
print("Critical Point : ",minChromosomes)
print("Minimum Cost : ₹", minValue)

