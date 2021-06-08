from utils import count_distance
from utils import manhattan_distance
import numpy as np
import constant
import time
from test2 import linear_conflict_heuristic


class Node():
	def __init__(self, zero_pos, state_dict2):
		self.state_dict2 = state_dict2
		self.zero_pos = zero_pos

	def __str__(self):
		return f"state=\n{self.state}"

	def __repr__(self):
		return f"state=\n{self.state}"

	# def __eq__(self, other):
	# 	return np.array_equal(self.state, other.state)

	# def __hash__(self):
	# 	return hash(self.state.tobytes())

	def nextnodes(self):
		r, c = map(int, self.zero_pos)
		moves = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
		
		for move in moves:
			if 0 <= move[0] < constant.BOARD_LENGTH and 0 <= move[1] < constant.BOARD_LENGTH:
				# print(f"\nMOVE = {move}")
				
				# tmp = np.copy(self.state)
				tmp2 = self.state_dict2.copy()
				# goal = constant.GLOBAL_STATE_DICT[tmp[move]]

				# print(f"STATE 000 = {self.state}")
				tmp2[move], tmp2[r, c] = tmp2[r, c], tmp2[move]
				# print(f"STATE 111 = {tmp}")
				# print(self.state_dict)
				
				# tmp2 = self.state_dict[0]
				# print(f"STATE_DICT 000 = {self.state_dict}")
				# tmp[0], tmp[self.state_dict2[move]] = tmp[self.state_dict2[move]], tmp[0]
				# print(f"STATE_DICT 111 = {tmp2}")
				# self.state_dict[tmp[move]] = tmp2
				
				yield Node(move, tmp2)

	


# def manhattan_heuristic_short(previous_heuristic, direction, goal, r, c):
# 	dir_goal_distance = manhattan_distance(direction, goal)
# 	goal_zero_distance = manhattan_distance(goal, (r, c))

# 	return previous_heuristic - dir_goal_distance + goal_zero_distance


# def nextnodes(node):
# 	zero = node.zero_pos

# 	r, c = map(int, zero)
# 	directions = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
# 	nodes = []
	
# 	for direction in directions:
# 		if 0 <= direction[0] < constant.BOARD_LENGTH and 0 <= direction[1] < constant.BOARD_LENGTH:
# 			tmp = np.copy(node.state)
# 			goal = constant.GLOBAL_STATE_DICT[tmp[direction]]

# 			tmp[direction], tmp[zero] = tmp[zero], tmp[direction]

# 			nodes.append(Node(tmp, direction))
# 	return nodes


def manhattan_heuristic(state):
	tic = time.time()
	print(f"MANHATTAN2")
	print(f"--> STATE = {state}")
	distance = 0

	for key,value in state.items():
		if key != constant.GLOBAL_STATE_DICT[value] and value != 0: # si possible enlever le zero
			distance += manhattan_distance(key, constant.GLOBAL_STATE_DICT[value])
	print('MANHATTAN2', (time.time() - tic) * 1000)
	exit()
	return distance


def search(path, g, threshold):
		node = list(path.keys())[-1]
		# f = g + linear_conflict_heuristic(node.state_dict2)
		f = g + manhattan_heuristic(node.state_dict2)

		if f > threshold:
			return f
		if node.state_dict2 == constant.GLOBAL_STATE_DICT2:
			return True

		minimum = float('inf')
		for n in node.nextnodes():
			if n not in path:
				path[n] = None
				tmp = search(path, g + 1, threshold)
				if tmp == True:
					return True
				if tmp < minimum:
					minimum = tmp
				path.popitem()

		return minimum


def solve(initial_state):

	print('GOAL_STATE = ')
	print(constant.GOAL_STATE)
	print()
	print('INITIAL STATE = ')
	print(initial_state)
	print()

	zero = np.where(initial_state == 0)
	state_dict = {initial_state[r][c]: (r, c) for r in range(constant.BOARD_LENGTH) for c in range(constant.BOARD_LENGTH)}
	state_dict2 = {(r, c) : initial_state[r][c]  for r in range(constant.BOARD_LENGTH) for c in range(constant.BOARD_LENGTH)}
	
	initial_node = Node(zero, state_dict2)	
	threshold = manhattan_heuristic(state_dict2)
	# threshold = linear_conflict_heuristic(state_dict2)
	path = {initial_node: None}



	while 1:
		tmp = search(path, 0, threshold)
		if tmp == True:
			print(f"GOOD!")
			return path.keys()
		elif tmp == float('inf'):
			print(f"WRONG!")
			return False
		threshold = tmp