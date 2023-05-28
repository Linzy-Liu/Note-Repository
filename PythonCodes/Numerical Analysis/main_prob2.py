import numpy as np
from Integrate import quad


def f(x):
	return np.exp(2 * x)


section = [3, 5]
real_val = (np.exp(10) - np.exp(6)) / 2

if __name__ == '__main__':
	# puzzle 1
	puzzle = [quad(f, section, accuracy = 40, method = 'ladder')]
	# puzzle 2
	puzzle.append(quad(f, section, accuracy = 20, method = 'Simpson'))
	# puzzle 3
	puzzle.append(quad(f, section, accuracy = 20, method = 'Romberg', accelerate_level = 1))
	# puzzle 4
	puzzle.append(quad(f, section, accuracy = 10, method = 'Romberg', accelerate_level = 2))
	# puzzle 5
	puzzle.append(quad(f, section, accuracy = 5, method = 'Romberg', accelerate_level = 3))
	# puzzle 6
	puzzle.append(quad(f, section, accuracy = 20, method = 'Gauss', points = 2))
	# puzzle 7
	puzzle.append(quad(f, section, accuracy = 10, method = 'Gauss', points = 4))

	loss = np.abs(np.array(puzzle) - real_val)
	show_loss = '[' + ", ".join(["%.5g" % number for number in loss]) + ']'
	print(show_loss)
