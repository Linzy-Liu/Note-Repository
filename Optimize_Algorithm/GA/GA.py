import numpy as npy
import matplotlib.pyplot as matplt

# fixed param
MUTATION_RATE = 0.05
CROSS_RATE = 0.8
GENETIC_LENGTH = 24
# Let r denote the converge rate. If max|x - y| < 2^r for any x and y in previous population,
# we assume the population is converged
CONVERGE_RADIUS = 1


class GeneticAlgorithm:
	def __init__(self, iteration, population, func, boundary: npy.ndarray, show = False, show_axe = None):
		"""
		:param iteration:An integer denotes the maximum iteration
		:param population:An integer denotes the population
		:param func: The function whose minimum value we are interested at. The function receives a solution and returns
		a real number.
		:param boundary: The boundary of each variable of the target function.
		:param show: A boolean value used for mark whether the user wants to draw
		:param show_axe: An axe where the points are put
		"""
		self.iter = iteration
		self.variable = boundary.shape[0]
		self.scale = npy.array([population, GENETIC_LENGTH * self.variable])
		self.boundary = boundary  # Should be in the shape of [x_min, x_max]
		self.target = func  # Should return a real number
		self.pop = npy.random.randint(0, 2, self.scale)
		self.show = show
		self.axe = show_axe

	def gene_decode(self, obj: npy.ndarray = None):
		"""
		:param obj: The code that needed to be decoded
		:return: The decoded code
		"""
		value_list = 2 ** npy.arange(0, GENETIC_LENGTH)[::-1]
		codes = []
		res = []
		# Separate the variable
		if obj is None:
			for i in range(self.variable):
				codes.append(self.pop[:, i::self.variable])
		elif obj.ndim == 1:
			for i in range(self.variable):
				codes.append(obj[i::self.variable])
		elif obj.ndim == 2:
			for i in range(self.variable):
				codes.append(obj[:, i::self.variable])
		else:
			raise ValueError
		# Decode
		if self.variable == 1:
			res.append(
				self.boundary[0] + (self.boundary[1] - self.boundary[0]) / (2 ** GENETIC_LENGTH - 1) * codes[0].dot(
					value_list))
		else:
			for i in range(self.variable):
				res.append(
					self.boundary[i, 0] + (self.boundary[i, 1] - self.boundary[i, 0]) / (2 ** GENETIC_LENGTH - 1) *
					codes[i].dot(value_list))
		return npy.array(res)

	def fitness(self):
		"""
		Calculate the fitness of present generation
		:return: A list of fitness
		"""
		source = self.gene_decode()
		value = self.target(source)
		return value - npy.min(value) + 1e-3

	def mutation(self, obj):
		if npy.random.uniform(0, 1) <= MUTATION_RATE:
			pt = npy.random.randint(0, self.scale[1])
			obj[pt] ^= 1

	def recreation(self):
		"""
		Mix the gene and generate the next generation
		:return: no return
		"""
		new_pop = []
		for individual in self.pop:
			child = individual.copy()
			if npy.random.uniform(0, 1) <= CROSS_RATE:
				mate = npy.random.randint(0, self.scale[0])
				while individual.all == self.pop[mate].all:
					mate = npy.random.randint(0, self.scale[0])
				pt = npy.random.randint(0, self.scale[1])
				child[pt:] = self.pop[mate, pt:]
			self.mutation(child)
			new_pop.append(child)
		self.pop = npy.array(new_pop)

	def selection(self):
		fitness = self.fitness()
		idx = npy.random.choice(npy.arange(0, self.scale[0]), size = self.scale[0], replace = True,
		                        p = fitness / fitness.sum())
		self.pop = self.pop[idx]
		return fitness

	def solve(self):
		fitness = None
		for _ in range(self.iter):
			self.recreation()
			if self.show:
				if self.axe is None:
					print('you should give me an axe to show the graph')
				else:
					if 'sca' in locals():
						sca.remove()
					source = self.gene_decode()
					sca = self.axe.scatter(*source, self.target(source), c = 'black', marker = 'o')
					matplt.show()
					matplt.pause(0.1)
			fitness = self.selection()
			if npy.max(fitness) - npy.min(fitness) <= 2 ** CONVERGE_RADIUS / (2 ** GENETIC_LENGTH - 1):
				break

		if fitness is None:
			raise ValueError
		else:
			idx = npy.argmax(fitness)
			ans = self.gene_decode(self.pop[idx])
			return ans, self.target(ans)
