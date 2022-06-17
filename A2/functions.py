


# Fitness Function
from locale import DAY_1


def fitness(chromosome):
    """
    This function takes a chromosome and returns its fitness.
    """
    size = len(chromosome)

    t1 = 0
    t2 = 0
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
        


    return int(maxFitness(chromosome) - (horiz_col + diag_col))

def maxFitness(chromosome):
    """
    This function takes a chromosome and returns its max fitness.
    """
    nq = len(chromosome)
    return (nq*(nq-1))/2