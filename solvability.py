from utils import is_even
from utils import count_distance
from utils import count_transpositions


def puzzle_is_solvable(initial_state):	
	transpositions = count_transpositions(initial_state, constant.GOAL_STATE)
	distance_zero = count_distance(0, initial_state, constant.GOAL_STATE)

	return is_even(transpositions) == is_even(distance_zero)