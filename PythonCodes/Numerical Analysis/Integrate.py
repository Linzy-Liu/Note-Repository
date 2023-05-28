import numpy as np
from Interpolate import Legendre_polynomial


def quad(f, section, accuracy: int,
         method = 'ladder',
         accelerate_level = None,
         epsilon = 1e-4,
         points = 2):
	"""
	Integrate the real-valued function f in the closed section.
	:param f: The real-valued function
	:param section: A list with two numbers [a, b]
	:param accuracy:
	:param method: The method that will be used to integrate. Including 'ladder', 'Simpson', 'Cotes', 'Romberg' and 'Gauss'
	:param accelerate_level: When 'romberg' is available, if 'accelerate_level' is None, the method Romberg will accelerate the value until the loss is lower than epsilon. Otherwise, the method will accelerate to the given level.
	:param epsilon: The upper bound of loss that could be tolerated.
	:param points: When 'Gauss' is available, this parameter is necessary for the accuracy of the integration.
	:return:
	"""
	if method == 'ladder':
		x = np.linspace(section[0], section[1], accuracy + 1)
		y = f(x)
		return np.sum((y[:-1] + y[1:]) / 2) * (x[1] - x[0])
	elif method == 'Simpson':
		x = np.linspace(section[0], section[1], 2 * accuracy + 1)
		y = f(x)
		return (x[1] - x[0]) / 3 * np.sum(y[:-1:2] + 4 * y[1::2] + y[2::2])
	elif method == 'Cotes':
		x = np.linspace(section[0], section[1], 4 * accuracy + 1)
		y = f(x)
		return 2 / 45 * (x[1] - x[0]) * np.sum(7 * y[:-1:4] + 32 * y[1::4] + 12 * y[2::4] + 32 * y[3::4] + 7 * y[4::4])
	elif method == 'Romberg':
		if accelerate_level is None:
			T = [[quad(f, section, accuracy)]]
			i = 2
			while True:
				T.append([quad(f, section, i * accuracy)])
				for j in range(len(T[-2])):
					m = len(T[-2]) - 1
					T[-1].append((4 ** m * T[-1][j] - T[-2][j]) / (4 ** m - 1))
				if np.abs(T[-1][-1] - T[-2][-1]) < epsilon:
					break
			return T[-1][-1]
		else:
			T = np.zeros((accelerate_level + 1, accelerate_level + 1))
			for i in range(accelerate_level + 1):
				T[i, 0] = quad(f, section, 2 ** i * accuracy)
			for j in range(1, accelerate_level + 1):
				for i in range(j, accelerate_level + 1):
					T[i, j] = (4 ** j * T[i, j - 1] - T[i - 1, j - 1]) / (4 ** j - 1)
			return T[accelerate_level, accelerate_level]
	elif method == 'Gauss':
		t = np.linspace(section[0], section[1], accuracy + 1)
		res = 0

		param = Legendre_polynomial(points, return_type = 'array')
		x = np.roots(param)
		for i in range(accuracy):
			x_temp = (t[i] + t[i+1]) / 2 + (t[i+1] - t[i]) / 2 * x
			A = np.array([x_temp ** i for i in range(len(x))])
			b = np.array(
				[(t[i+1] ** (j + 1) - t[i] ** (j + 1)) / (j + 1) for j in range(len(x_temp))])
			p = np.linalg.solve(A, b)
			res += np.dot(p, f(x_temp))
		return res
	else:
		raise ValueError
