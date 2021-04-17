import matplotlib.pyplot as plt
import math
import random
class SA:
    def __init__(self, matrix, T=-1, alpha=-1, stopping_T=-1, stopping_iter=-1):
        self.matrix = matrix
        self.N = len(matrix)
        self.T = math.sqrt(self.N) if T == -1 else T
        self.alpha = 0.995 if alpha == -1 else alpha
        self.stopping_temperature = 0.00000001 if stopping_T == -1 else stopping_T
        self.stopping_iter = 100000 if stopping_iter == -1 else stopping_iter
        self.iteration = 1

        self.nodes = [i for i in range(self.N)]

        self.cur_solution = self.initial_solution()
        self.initial_solution_value = self.cur_solution
        self.best_solution = list(self.cur_solution)

        self.cur_fitness = self.fitness(self.cur_solution)
        self.initial_fitness = self.cur_fitness
        self.best_fitness = self.cur_fitness

        self.fitness_list = [self.cur_fitness]

    def initial_solution(self):
        cur_node = random.choice(self.nodes)
        solution = [cur_node]
        free_list = list(self.nodes)
        free_list.remove(cur_node)
        while free_list:
            closest_dist = min([self.matrix[cur_node][j] for j in free_list])
            idx_rep = [i for i, item in enumerate(self.matrix[cur_node]) if item == closest_dist]
            for i in idx_rep:
                cur_node = i
                if cur_node in free_list:
                    free_list.remove(cur_node)
                    break
            solution.append(cur_node)

        return solution

    def fitness(self, solution):
        return round(sum([self.matrix[solution[i - 1]][solution[i]] for i in range(1, self.N)]) +
                     self.matrix[solution[0]][solution[self.N - 1]], 4)

    def p_accept(self, candidate_fitness):
        return math.exp(-abs(candidate_fitness - self.cur_fitness) / self.T)

    def accept(self, candidate):
        candidate_fitness = self.fitness(candidate)
        if candidate_fitness < self.cur_fitness:
            self.cur_fitness = candidate_fitness
            self.cur_solution = candidate
            if candidate_fitness < self.best_fitness:
                self.best_fitness = candidate_fitness
                self.best_solution = candidate
        else:
            if random.random() < self.p_accept(candidate_fitness):
                self.cur_fitness = candidate_fitness
                self.cur_solution = candidate

    def plot_learning(self):
        plt.plot([i for i in range(len(self.fitness_list))], self.fitness_list)
        plt.ylabel('Fitness')
        plt.xlabel('Iteration')
        plt.show()

    def sa(self, file):
        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            candidate = list(self.cur_solution)
            j = random.randint(2, self.N - 1)
            i = random.randint(0, self.N - j)
            candidate[i:(i + j)] = reversed(candidate[i:(i + j)])
            self.accept(candidate)
            self.T *= self.alpha
            self.iteration += 1
            self.fitness_list.append(self.cur_fitness)

        file.write('Initial Solution: {}\n'.format(self.initial_solution_value))
        file.write('Best solution: {}\n'.format(self.best_solution))
        file.write('Initial fitness: {}\n'.format(self.initial_fitness))
        file.write('Best fitness obtained: {}\n'.format(self.best_fitness))