import numpy as np


def interpolate(x: np.ndarray, y: np.ndarray, method = 'Lagrange', cond = None):
	if method == 'Lagrange':
		index = np.arange(len(x))
		coef = [np.prod(x[i] - x[index != i]) for i in index]

		def f(t):
			res = 0
			for i in index:
				res += np.prod(t.reshape(-1, 1) - x[index != i].reshape(1, -1), axis = 1) / coef[i] * y[i]
			return res

		return f

	elif method == 'linear spline':
		h = x[1:] - x[:-1]
		k = (y[1:] - y[:-1]) / h
		b = np.array([(y[k] * x[k + 1] - y[k + 1] * x[k]) / h[k] for k in range(len(x) - 1)])

		def f(t):
			index = np.digitize(t, x) - 1
			if t[-1] == x[-1]:
				index[-1] = len(k) - 1
			return k[index] * t + b[index]

		return f

	elif method == 'cubic spline':
		if cond is None:
			raise ValueError
		# calculate coefficient
		h = x[1:] - x[:-1]
		mu = np.r_[h[:-1] / (h[:-1] + h[1:]), 1]
		lamda = np.r_[1, h[1:] / (h[:-1] + h[1:])]
		delta = (y[1:] - y[:-1]) / h
		d = 6 * np.r_[
			(delta[0] - cond[0]) / h[0],
			(delta[1:] - delta[:-1]) / (x[2:] - x[:-2]),
			(cond[1] - delta[-1]) / h[-1]
		]
		# Solve M
		A = np.diag([2] * len(d))
		for i in range(len(d) - 1):
			A[i, i + 1] = lamda[i]
			A[i + 1, i] = mu[i]
		M = np.linalg.solve(A, d)

		# Calculate param
		a1 = M[1:] / (6 * h)
		a2 = -M[:-1] / (6 * h)
		b1 = y[1:] / h - M[1:] * h / 6
		b2 = M[:-1] * h / 6 - y[:-1] / h

		def f(t):
			index = np.digitize(t, x) - 1
			if t[-1] == x[-1]:
				index[-1] = len(a1) - 1
			return a1[index] * (t - x[index]) ** 3 + a2[index] * (t - x[index + 1]) ** 3 + \
				b1[index] * (t - x[index]) + b2[index] * (t - x[index + 1])

		return f


def Legendre_polynomial(deg, return_type = 'function'):
	if deg == 0:
		coef = np.array([1])
	elif deg == 1:
		coef = np.array([0, 1])
	else:
		p_last = np.array([1])
		p_present = np.array([0, 1])

		for i in range(1, deg):
			tmp = (2 * i + 1) / (i + 1) * np.r_[0, p_present] - i / (i + 1) * np.r_[p_last, [0, 0]]
			p_last = p_present
			p_present = tmp
		coef = p_present

	if return_type == 'function':
		def f(x):
			t = np.array([x ** i for i in range(deg + 1)])
			return np.sum(t * coef)

		return f

	elif return_type == 'array':
		return coef
	else:
		raise ValueError


def Chebyshev_polynomial(deg: int, return_type = 'function'):
	if deg == 0:
		coef = np.array([1])
	elif deg == 1:
		coef = np.array([0, 1])
	else:
		p_last = np.array([1])
		p_present = np.array([0, 1])

		for i in range(1, deg):
			tmp = 2 * np.r_[0, p_present] - np.r_[p_last, [0, 0]]
			p_last = p_present
			p_present = tmp
		coef = p_present

	if return_type == 'function':
		def f(x):
			t = np.array([x ** i for i in range(deg + 1)])
			return coef @ t

		return f

	elif return_type == 'array':
		return coef
	else:
		raise ValueError


def product(f: np.ndarray, g: np.ndarray, x: np.ndarray, rho = np.array([1])):
	rho_x = rho @ np.array([x ** i for i in range(len(rho))])
	return np.sum(f * g * rho_x)


def fit_polynomial(deg: int, x: np.ndarray, y: np.ndarray, return_type = 'function'):
	space = np.array([x ** i for i in range(deg + 1)])
	A = np.zeros((deg + 1, deg + 1))
	for i in range(A.shape[0]):
		for j in range(A.shape[1]):
			A[i, j] = product(space[i], space[j], x)
	b = np.zeros(deg + 1)
	for i in range(b.shape[0]):
		b[i] = product(space[i], y, x)
	param = np.linalg.solve(A, b)

	if return_type == 'function':
		def f(x):
			t = np.array([x ** i for i in range(deg + 1)])
			return param @ t

		return f

	elif return_type == 'array':
		return param
	else:
		raise ValueError


def abs_error(f, p, section: np.ndarray):
	return np.max(np.abs(f(section) - p(section)))
