import numpy as np


class ResultData:
	def __init__(self, sol: np.ndarray, steps, residual):
		self.steps = steps
		self.residual = residual
		self.solution = sol
		self.error = np.inf

	def set_error(self, accurate_sol: np.ndarray):
		self.error = np.max(np.abs(accurate_sol - self.solution))

	def show_result(self):
		result_string = [
			"steps= %d" % self.steps,
			"residual= %.5g" % self.residual,
			"error= %.5g" % self.error
		]
		print("\t".join(result_string))


def solve_linear_eq(A: np.ndarray, b: np.ndarray, x0 = None, epsilon = 1e-8, method = 'Gauss-Seidel', omega = None):
	"""
	Solve the linear equation Ax=b where A is the coefficient matrix with the shape of NxN and b is a vector in R^N.
	:param A: The coefficient matrix. It should be a square matrix
	:param b: The vector
	:param x0: The initial value. The x0 will be set as 0 by default.
	:param epsilon: The upper bound of ||x_{k+1} - x_k||. The norm here is the infinite norm.
	:param method: Supports 'Jacobi', 'Gauss-Seidel', 'SOR' and 'Conjugate gradient'. Please make sure that the input matrix A,
	corresponding to the Jacobi iteration matrix J, can be diagonalized over the field of real numbers when 'SOR' is enabled;
	and ensure that the input matrix A is positive definite when 'Conjugate gradient' is enabled.
	:param omega: The factor in SOR. It will be set as the best SOR factor by default.
	:return: The result with iteration steps, residual, error and solution.
	"""
	D = np.array([A[i, i] for i in range(A.shape[0])])
	B = np.diag(D) - A
	if x0 is None:
		x0 = np.zeros(A.shape[1])

	if method == 'Jacobi':
		x_latest = (B @ x0 + b) / D
		x_previous = x0
		iter_num = 1
		while np.max(np.abs(x_latest - x_previous)) >= epsilon:
			x_previous = x_latest
			x_latest = (B @ x_previous + b) / D
			iter_num += 1
		return ResultData(x_latest, iter_num, np.max(np.abs(b - A @ x_latest)))
	elif method == 'Gauss-Seidel':
		delta = np.inf
		iter_num = 0
		x = x0
		while delta >= epsilon:
			x_temp = x.copy()
			iter_num += 1
			for i in range(len(x)):
				x[i] = (np.dot(B[i], x) + b[i]) / D[i]
			delta = np.max(np.abs(x_temp - x))
		return ResultData(x, iter_num, np.max(np.abs(b - A @ x)))
	elif method == 'SOR':
		if omega is None:
			J = np.diag(1 / D) @ B
			eigen_val, eigen_vec = np.linalg.eig(J)
			omega = 2 / (1 + np.sqrt(1 - np.max(np.abs(eigen_val)) ** 2))
		delta = np.inf
		iter_num = 0
		x = x0
		while delta >= epsilon:
			x_bar = x.copy()
			iter_num += 1
			for i in range(len(x_bar)):
				x_bar[i] = (np.dot(B[i], x_bar) + b[i]) / D[i]
			delta = np.max(np.abs(omega * (x_bar - x)))
			x += omega * (x_bar - x)
		return ResultData(x, iter_num, np.max(np.abs(b - A @ x)))
	elif method == 'Conjugate gradient':
		delta = np.inf
		x = x0
		iter_num = 0
		while delta >= epsilon:
			iter_num += 1
			p = b - A @ x
			alpha = np.dot(p, p) / np.dot(A @ p, p)
			delta = np.max(np.abs(alpha * p))
			x += alpha * p
		return ResultData(x, iter_num, np.max(np.abs(b - A @ x)))
