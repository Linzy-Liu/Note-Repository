import time
import numpy as npy

converge_rate = 0.05
eq_range = 1e-15


class StimulatedAnnealing:
	def __init__(self, iteration, x0, temperature, trans_t, change_func, target_func, target_value = None,
	             target_change = None):
		self.iter = iteration
		self.x = npy.array(x0)
		self.T = temperature
		self.trans_t = trans_t
		self.C = change_func
		self.E = target_func
		self.E_value = target_value
		self.dE = target_change
		self.history = [x0]

	# temperature is a list of 2 elements in the form of [init_T, bound_T]
	# change_func and target_change should receive two parameter: x and T; target_func only receive x.
	# And the parameter x in these three functions should be of same dimension.
	# change_func returns a vector which is the new x, target_func returns a real number
	# And target_change returns dx and dE. Namely, target_change should generate a new x by itself.

	def metropolis(self):
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
