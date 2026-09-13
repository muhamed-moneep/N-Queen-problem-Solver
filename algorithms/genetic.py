import time
import random
from utils import generate_random_board, calculate_conflicts


def solve(n):

    start_time = time.time()

    #initialize the parameters
    population_size = 50
    mutation_rate = 0.2
    max_generations = 500

    #helper functions

    def fitness(board):
        return -calculate_conflicts(board)  # higher is better

    def selection(population):
        population.sort(key=lambda x: fitness(x), reverse=True)
        return population[:10]  # top 10

    def crossover(parent1, parent2):
        n = len(parent1)
        point = random.randint(0, n - 1)
        return parent1[:point] + parent2[point:]

    def mutate(board):
        if random.random() < mutation_rate:
            row = random.randint(0, n - 1)
            col = random.randint(0, n - 1)
            board[row] = col
        return board

    #initial population
    population = [generate_random_board(n) for _ in range(population_size)]

    best_solution = None
    steps = 0

    #evolution loop
    for generation in range(max_generations):
        steps += 1

        #sort by fitness
        population.sort(key=lambda x: fitness(x), reverse=True)

        best = population[0]

        #check solution
        if calculate_conflicts(best) == 0:
            best_solution = best
            break

        #selection
        selected = selection(population)

        #create next generation
        new_population = []

        while len(new_population) < population_size:
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)

            child = crossover(parent1, parent2)
            child = mutate(child)

            new_population.append(child)

        population = new_population

    end_time = time.time()

    metrics = {
        "algorithm": "Genetic Algorithm",
        "time": end_time - start_time,
        "steps": steps,
        "success": best_solution is not None
    }

    return best_solution, metrics