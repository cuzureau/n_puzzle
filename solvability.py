from utils import is_even
from utils import count_distance


def count_transpositions(state1, state2, size):
	transpositions = 0

	for column in range(size * size - 1):
		first = state1[column]
		for row in range(column + 1, size * size):
			second = state1[row]
			if state2.index(first) > state2.index(second):
				transpositions += 1

	return transpositions


def puzzle_is_solvable(initial_state, goal_state, size):
	transpositions = count_transpositions(initial_state, goal_state, size)
	distance_zero = count_distance(0, initial_state, goal_state, size)

	return is_even(transpositions) == is_even(distance_zero)