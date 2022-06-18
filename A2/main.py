import functions

print("N-Queens GA")
print("-----------------------------------------------------")

num_of_queens = 8
maxFitness = functions.maxFitness(num_of_queens)
population_size = 100

population = [ functions.generate_chromosome(num_of_queens) for i in range(population_size) ]

gen = 1

while not maxFitness in [ functions.fitness(chromosome) for chromosome in population ]:
    print("Generation:", gen)
    
    # generate new population
    for i in range(population_size):
        x = function.select_parent(population, maxFitness) # select parent 1
        y = function.select_parent(population, maxFitness) # select parent 2
        child = function.cross_over(x, y) # cross over function 
        population.append(child) # add child to population
        if fitness(child) == maxFitness:
            break # if child has max fitness, stop

        # get rid of the weakest chromosome
        population.sort(key=lambda chromosome: fitness(chromosome), reverse=True)
        population = population[:population_size - 1]
        

    gen += 1 # new generation created
print("Problem solving in generation: ", gen)

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