from Interpolate import fit_polynomial, interpolate, abs_error
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return 1 / (1 + x ** 2)


def d_f(x):
	return -2 * x / (1 + x ** 2) ** 2


if __name__ == '__main__':
	# puzzle 1
	"""x = np.arange(-5, 6)
	y = f(x)	 
	p = interpolate(x, y)"""
	# puzzle 2
	"""x = np.cos([(2 * k + 1) / 22 * np.pi for k in range(11)]) * 5
	y = f(x)
	p = interpolate(x, y)"""
	# puzzle 3
	"""x = np.arange(-5, 6)
	y = f(x)
	p = interpolate(x, y, method = 'linear spline')"""
	# puzzle 4
	"""x = np.arange(-5, 6)
	y = f(x)
	cond = [d_f(-5), d_f(5)]
	p = interpolate(x, y, method = 'cubic spline', cond = cond)"""
	# puzzle 5
	x = np.arange(-5, 6)
	y = f(x)
	p = fit_polynomial(deg = 6, x = x, y = y)

	x0 = np.linspace(-5, 5, 1000)
	plt.rc("font", family = 'MicroSoft YaHei')
	plt.plot(x0, p(x0), 'r', label = '拟合函数')
	plt.plot(x0, f(x0), 'g', label = '原函数')
	print("%.5g" % abs_error(f, p, np.arange(-5, 5.1, 0.1)))
	plt.legend()
	plt.show()
