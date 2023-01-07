import numpy as npy

converge_rate = 0.05
eq_range = 1e-15


class StimulatedAnnealing:
	def __init__(self, iteration, x0, temperature: npy.ndarray, trans_t, change_func, target_func, target_value = None,
	             target_change = None):
		"""
		:param iteration: An integer denote the maximum iteration to find the best solution in a certain temperature
		:param x0: The initial solution
		:param temperature: A list of 2 elements with the form of [init_T, bound_T], and init_T > bound_T
		:param trans_t: The transform function of T. The function receives a real number and returns a real number
		:param change_func: The function that introduces small changes to the solution. The function receives
		a solution and the temperature as parameters and returns a real number.
		:param target_func: The function whose minimum value we are interested at. The function receives a solution and
		returns a real value
		:param target_value: The value when substituting x0 into target function.
		:param target_change: The function that generates new solution and calculates the difference of target function's
		value between the new solution and the original solution. The function receives a solution and the temperature,
		returns the dx and dE.(dx denotes the difference between new solution and the original solution, dE denotes the
		difference of target function's value between the new and the original.)
		"""
		self.iter = iteration
		self.x = npy.array(x0)
		self.T = temperature
		self.trans_t = trans_t
		self.C = change_func
		self.E = target_func
		self.E_value = target_value
		self.dE = target_change
		self.history = [x0]

	def metropolis(self):
		"""
		Proceed the process of metropolis sampling and change the value inplace
		:return: no return
		"""
		if self.E_value is None:
			self.E_value = self.E(self.x)
		if self.dE is not None:
			dx, delta_E = self.dE(self.x, self.T)
			p = npy.exp(-delta_E / self.T)
			if delta_E < 0:
				self.x = self.x + dx
				self.E_value = self.E_value + delta_E
			elif npy.random.uniform() <= p:
				self.x = self.x + dx
				self.E_value = self.E_value + delta_E
		else:
			temp_x = self.C(self.x, self.T)
			temp_E = self.E(temp_x)
			delta_E = temp_E - self.E_value
			p = npy.exp(-delta_E / self.T[0])
			if delta_E < 0:
				self.x = temp_x
				self.E_value = temp_E
			elif npy.random.uniform() <= p:
				self.x = temp_x
				self.E_value = temp_E

	def solve(self):
		"""
		Find the minimum value point
		:return: returns the minimum value and corresponding point
		"""
		limit_count_iter = converge_rate * self.iter
		previous_x = None
		while self.T[0] > self.T[1]:
			count_iter = 0
			for i in range(self.iter):
				self.metropolis()
				if previous_x is not None:
					if npy.linalg.norm(self.x - previous_x) <= eq_range:
						count_iter += 1
					else:
						count_iter = 0
						self.history.append(self.x)
				else:
					previous_x = self.x
				if count_iter >= limit_count_iter:
					break
			self.T[0] = self.trans_t(self.T[0])
		return self.x, self.E_value
