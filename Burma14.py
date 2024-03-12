import random

def generate_population(size, num_genes):
    population = []
    for _ in range(size):
        individual = []
        for _ in range(num_genes):
            gene = random.randint(0, 1)
            individual.append(gene)
        population.append(individual)
    return population

def calculate_fitness(individual):
    fitness = 0
    for gene in individual:
        fitness += gene
    return fitness

def select_parents(population, num_parents):
    parents = []
    for _ in range(num_parents):
        max_fitness = 0
        selected_parent = None
        for individual in population:
            fitness = calculate_fitness(individual)
            if fitness > max_fitness:
                max_fitness = fitness
                selected_parent = individual
        parents.append(selected_parent)
        population.remove(selected_parent)
    return parents

def crossover(parents, num_offspring):
    offspring = []
    for _ in range(num_offspring):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        offspring.append(child)
    return offspring

def mutate(offspring, mutation_rate):
    for individual in offspring:
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                individual[i] = 1 - individual[i]
    return offspring

def genetic_algorithm(num_genes, population_size, num_parents, num_offspring, mutation_rate, num_generations):
    population = generate_population(population_size, num_genes)
    for _ in range(num_generations):
        parents = select_parents(population, num_parents)
        offspring = crossover(parents, num_offspring)
        offspring = mutate(offspring, mutation_rate)
        population = parents + offspring
    return population

num_genes = 10
population_size = 100
num_parents = 10
num_offspring = 90
mutation_rate = 0.01
num_generations = 100

population = genetic_algorithm(num_genes, population_size, num_parents, num_offspring, mutation_rate, num_generations)
best_individual = max(population, key=calculate_fitness)
print(best_individual)

def find_optimal_generation(population):
    generations = 0
    while population > 1:
        if population % 2 == 0:
            population = population // 2
        else:
            population = (population // 2) + 1
        generations += 1
    return generations

    population = int(input("Enter the population size: "))
    optimal_generation = find_optimal_generation(population)
    print("The minimum number of generations to reach an optimal population size is:", optimal_generation)