import time
from utils import is_even
from utils import count_distance
from utils import count_transpositions
import numpy as np
import constant


def puzzle_is_solvable(initial_state):	
	tic = time.time()
	transpositions = count_transpositions(initial_state, constant.GOAL_STATE)
	print('transpositions', time.time() - tic)
	
	tic = time.time()
	distance_zero = count_distance(0, initial_state, constant.GOAL_STATE)
	print('distance', time.time() - tic)
	
	return is_even(transpositions) == is_even(distance_zero)