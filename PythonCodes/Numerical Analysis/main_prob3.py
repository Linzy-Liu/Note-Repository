import numpy as np
from Matrix import solve_linear_eq

if __name__ == '__main__':
	A = np.array([
		[3, 1, 1],
		[1, 3, 1],
		[1, 1, 3]
	])
	b = np.array([3, 0, 2])
	accurate_sol = np.array([1, -0.5, 0.5])
	# puzzle 1
	sol1 = solve_linear_eq(A, b, method = 'Jacobi')
	sol1.set_error(accurate_sol)
	sol1.show_result()
	# puzzle 2
	sol2 = solve_linear_eq(A, b, method = 'Gauss-Seidel')
	sol2.set_error(accurate_sol)
	sol2.show_result()
	# puzzle 3
	sol3 = solve_linear_eq(A, b, method = 'SOR')
	sol3.set_error(accurate_sol)
	sol3.show_result()
	# puzzle 4
	sol4 = solve_linear_eq(A, b, method = 'Conjugate gradient')
	sol4.set_error(accurate_sol)
	sol4.show_result()

