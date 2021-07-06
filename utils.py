
# a verifier
def is_even(number):
	return number % 2


def count_distance(number, state1, state2, size):
	position1 = state1.index(number)
	position2 = state2.index(number)

	return manhattan_distance(position1, position2, size)


def manhattan_distance(a, b, size):
	return abs(b // size - a // size) + abs(b % size - a % size)