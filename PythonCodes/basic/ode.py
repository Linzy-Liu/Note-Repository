import numpy as npy
import pandas as pd
from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt

S = npy.pi
rho = 1025
g = 9.8
f = 6250
omega = 1.4005
k = 80000
mu = 656.3616
m1 = 4866
m2 = 2433
m3 = 1335.535
h_coat = 3
h_cone = 0.8
L = 0.5


def get_data(lower_bound, upper_bound, accuracy = 1000):
	def func(x, y):
		y10, y20, y11, y21 = y
		factor = 10000
		return [
			y11,
			y21,
			(f * npy.cos(omega * x) - y10 * S * rho * g - k * (y10 - y20) - factor * (y11 - y21) - mu * y11) / (
					m1 + m3),
			k * (y10 - y20) + factor * (y11 - y21)
		]

	t = npy.linspace(lower_bound, upper_bound, accuracy)
	y0 = [0, 0, 0, 0]
	# data = solve_ivp(func, (0, 1), y0, t_eval = t, method = 'Radau').y
	data = odeint(func, y0, t, tfirst = True).T
	return t, data


if __name__ == '__main__':
	t, data = get_data(0, 1)
	h0 = m1 / (rho * S) - h_cone / 3
	F_elastic = k * (data[0] - data[1])
	plt.rc('text', usetex = True)
	plt.rc('font', size = 10)
	# plt.yscale('symlog')
	plt.plot(t, data[0], 'r-.', label = '$x_1$')
	plt.plot(t, data[1], 'b-.', label = '$x_2$')
	plt.plot(t, data[2], label = r'$\frac{d\,x_1}{d\,t}$')
	plt.plot(t, data[3], label = r'$\frac{d\,x_2}{d\,t}$')
	pd.DataFrame(data = data.T, columns = ['x1', 'x2', 'dx1', 'dx2']).to_excel('data.xlsx')
	'''
	fig1 = plt.figure(0, figsize = (8, 6))
	axe1 = fig1.add_axes([0.12, 0.12, 0.76, 0.76])
	axe1.spines[['right', 'top']].set_color(None)
	axe1.set_xlabel('$t$')
	fig2 = plt.figure(1, figsize = (8, 6))
	axe2 = fig2.add_axes([0.12, 0.12, 0.76, 0.76])
	axe2.spines[['right', 'top']].set_color(None)
	axe2.set_xlabel('$t$')
	axe1.plot(t, data[0])
	axe1.plot(t, npy.array([h0] * len(t)))
	axe1.plot(t, npy.array([h0 - h_coat] * len(t)))
	axe2.plot(t, F_elastic + m2 * g, label = '$F_{elastic}+m_2g$')
	axe2.plot(t, [L * k] * len(t))
	'''
	plt.legend()
	plt.show()
