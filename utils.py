import numpy as np

# a verifier
def is_even(number):
	return number % 2

def count_transpositions(state1, state2):
	tmp = np.copy(state1)
	transpositions = 0

	for number in range(len(state1) ** 2):
		position1 = np.where(tmp == number)
		position2 = np.where(state2 == number)
		if position1 != position2:
			tmp[position1], tmp[position2] = tmp[position2], tmp[position1]
			transpositions += 1

	return transpositions


def count_distance(number, state1, state2):
	position1 = np.where(state1 == number)
	position2 = np.where(state2 == number)

	return manhattan_distance(position1, position2)


def manhattan_distance(a, b):
	return abs(b[0] - a[0]) + abs(b[1] - a[1])