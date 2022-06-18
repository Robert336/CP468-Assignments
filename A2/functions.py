import random


def fitness(chromosome):
    """
    This function takes a chromosome and returns its fitness.
    """
    size = len(chromosome)

    diag1 = [0] * 2 * size # left and up diagonal
    diag2 = [0] * 2 * size # right and up diagonal
    
    horiz_col = sum([chromosome.count(queen)-1 for queen in chromosome]) / 2 # horizontal collisions
    diag_col = 0 # diagonal collisions

    for i in range(size):
        diag1[i + chromosome[i - 1]] += 1
        diag2[size - 1 + chromosome[i] - 2] += 1


    diag_col = 0
    for i in range(2 * size - 1):
        counter = 0
        if diag1 [i] > 1:
            counter += diag1[i] - 1
        if diag2 [i] > 1:
            counter += diag2[i] - 1
        diag_col += counter / (size - abs(i - size + 1))
        

    # loewr is better for fitness (less collisions)
    return int(maxFitness(chromosome) - (horiz_col + diag_col)) #28-(2+3)=23

def maxFitness(chromosome):
    """
    This function takes a chromosome and returns its max fitness.
    """
    nq = len(chromosome)
    return (nq*(nq-1))/2

def cross_over(chromosome1, chromosome2):
    """
    This function takes two chromosomes and returns their crossover.
    """
    size = len(chromosome1)
    cross_point = random.randint(0, size-1) # random cross point generation
    return chromosome1[:cross_point] + chromosome2[cross_point:] # return crossover of chromosomes at cross point


def generate_chromosome(size):
    """
    This function takes a size of the chess board and returns a random chromosome.
    """
    return [ random.randint(1, size) for i in range(size) ]

def mutate(chromosome):
    """
    This function takes a chromosome and returns its mutated chromosome.
    We are only changing the position of one queen.
    """
    size = len(chromosome)
    mutate_point = random.randint(0, size-1)
    mutate_value = random.randint(1, size)
    chromosome[mutate_point] = mutate_value
    return chromosome

def get_probability(chromosome, max_fitness):
    """
    This function takes a chromosome and max fitness and returns its probability of being selected.
    """
    return fitness(chromosome) / max_fitness

def select_parent(population, max_fitness):
    """
    This function takes a population and max fitness and returns a random parent.
    """
    probability = [ get_probability(chromosome, max_fitness) for chromosome in population ]
    total_probability = sum(probability)
    random_probability = random.uniform(0, total_probability)
    for i in range(len(population)):
        random_probability -= probability[i]
        if random_probability <= 0:
            return population[i]


def genetic_child(population, max_fitness):
    """
    This function takes a population and max fitness and returns a child.
    """
    parent1 = select_parent(population, max_fitness)
    parent2 = select_parent(population, max_fitness)
    child = cross_over(parent1, parent2)
    child = mutate(child)
    return child

