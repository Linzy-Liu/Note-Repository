import numpy as npy
import pandas as pd
import cvxpy as cvx
import scipy as sci
import scipy.stats as scist
import matplotlib.pyplot as matplt
import seaborn as sbn
import SA
import time

k = 0.99
T = npy.array([1e3, 1])
s = 0.1
accuracy = 1000


def func(x):
	x1, x2 = x
	return 2 * 418.9829 - x1 * npy.sin(npy.sqrt(npy.abs(x1))) - x2 * npy.sin(npy.sqrt(npy.abs(x2)))


def tran_t(t):
	return k * t


def new_root(x, t):
	dx = 1000 * s * npy.random.normal(size = 2)
	new_x = x + dx
	while not (-500 <= new_x[0] <= 500 and -500 <= new_x[1] <= 500):
		dx = 1000 * s * npy.random.normal(size = 2)
		new_x = dx + x
	return new_x


if __name__ == '__main__':
	iteration = 1000
	x0 = scist.uniform.rvs(loc = -500, scale = 1000, size = 2)
	model = SA.StimulatedAnnealing(iteration, x0, temperature = T, change_func = new_root, trans_t = tran_t,
	                               target_func = func)
	print(model.solve())
	model.history = npy.array(model.history)

	matplt.rc('font', size = 10)
	matplt.rc('text', usetex = True)
	x = npy.linspace(-500, 500, accuracy)
	y = npy.linspace(-500, 500, accuracy)
	X, Y = npy.meshgrid(x, y)
	z = 2 * 418.9829 - X * npy.sin(npy.sqrt(npy.abs(X))) - Y * npy.sin(npy.sqrt(npy.abs(Y)))

	fig = matplt.figure(figsize = (8, 6), dpi = 100)
	axe = fig.add_axes([0.1, 0.1, 0.8, 0.8])
	axe.spines[['right', 'top']].set_color(None)
	axe.set_xlabel('$x$')
	axe.set_ylabel('$y$')
	axe.set_title(r'$837.9658 - \sum\limits_{i=1}^2x_i\sin(\sqrt{|x_i|})$')
	axe.contourf(X, Y, z)
	# axe.scatter(model.history[:, 0], model.history[:, 1], s = 0.01, c = 'r')

	matplt.savefig('sa.png', dpi = 500)
	matplt.show()
	print(time.perf_counter())
