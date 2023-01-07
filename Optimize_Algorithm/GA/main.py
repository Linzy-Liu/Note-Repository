import numpy as npy
import pandas as pd
import cvxpy as cvx
import scipy as sci
import scipy.stats as scist
import matplotlib.pyplot as matplt
import seaborn as sbn
import GA
import time


def f1(x):
	x1, x2 = x
	return x1 * npy.sin(npy.sqrt(npy.abs(x1))) + x2 * npy.sin(npy.sqrt(npy.abs(x2))) - 837.9658


def f2(x):
	x1, x2 = x
	return -(3 * npy.log(x1) - 20 * npy.sin(x1 * x2) + npy.cos(x2 ** 2))


def f3(x):
	x1, x2 = x
	return 3 * (1 - x1) ** 2 * npy.exp(-(x1 ** 2) - (x2 + 1) ** 2) - 10 * (x1 / 5 - x1 ** 3 - x2 ** 5) * npy.exp(
		-x1 ** 2 - x2 ** 2) - 1 / 3 ** npy.exp(-(x1 + 1) ** 2 - x2 ** 2)


if __name__ == '__main__':
	accuracy = 1000
	iteration = 200
	bound = npy.array([
		[-3, 3],
		[-3, 3]
	])
	population = 200

	fig = matplt.figure(figsize = (8, 6), dpi = 100)
	axe = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection = '3d')
	model = GA.GeneticAlgorithm(iteration = iteration, population = population, func = f3, boundary = bound)
	"""
	matplt.ion()
	x = npy.linspace(*bound[0], accuracy)
	y = npy.linspace(*bound[1], accuracy)
	x, y = npy.meshgrid(x, y)
	z = f3([x, y])
	axe.set_xlabel('$x$')
	axe.set_ylabel('$y$')
	axe.set_zlabel('$z$')
	axe.plot_surface(x, y, z, cmap = matplt.cm.coolwarm)
	matplt.show()
	matplt.pause(3)
	"""
	print(model.solve())
	# matplt.savefig('ga.png', dpi = 500)
	# matplt.ioff()
	print(time.perf_counter())
