import functions

print("N-Queens GA")
print("-----------------------------------------------------")

num_of_queens = 8 # number of queens
population_size = 100 # population size
population = [ functions.generate_chromosome(num_of_queens) for i in range(population_size) ] # generate initial population
maxFitness = functions.maxFitness(population[0]) # get max fitness for this problem

gen = 1 # generation counter

# while loop until we find a solution
while not maxFitness in [ functions.fitness(chromosome) for chromosome in population ]:
    print("Generation:", gen)
    
    # generate new population
    for i in range(population_size):
        x = functions.select_parent(population, maxFitness) # select parent 1
        y = functions.select_parent(population, maxFitness) # select parent 2
        child = functions.cross_over(x, y) # cross over function 
        population.append(child) # add child to population
        if functions.fitness(child) == maxFitness:
            break # if child has max fitness, stop

        # remove the weakest chromosome from the gene pool
        population.remove(min(population, key=functions.fitness))     

    gen += 1 # new generation created
print("Problem solved in generation: ", gen)

# find the solution chromosome
for chromosome in population:
    if functions.fitness(chromosome) == maxFitness:
        print("Solution:", chromosome)
        sol_chrom = chromosome
        break


board = []

for x in range(num_of_queens):
    board.append(["x"] * num_of_queens)
        
for i in range(num_of_queens):
    board[num_of_queens-sol_chrom[i]][i]="Q"
            

def print_board(board):
    for row in board:
        print (" ".join(row))
            
print()
print_board(board)