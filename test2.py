import numpy as np
import constant
import time



# to be deleted for import
def manhattan_distance(a, b):
	return abs(b[0] - a[0]) + abs(b[1] - a[1])


def manhattan_heuristic(state):
	# tic = time.time()
	# print(f"MANHATTAN2")
	# print(f"--> STATE = {state}")
	distance = 0

	for key,value in state.items():
		if key != constant.GLOBAL_STATE_DICT[value] and value != 0: # si possible enlever le zero
			distance += manhattan_distance(key, constant.GLOBAL_STATE_DICT[value])
	# print('MANHATTAN2', (time.time() - tic) * 1000)
	return distance


# J'en suis la : ca rame ! reste a tester avec l'ancien linear_conflicts tout en gardant le double : test_state (dict) et state (numpy array). Pour voir si le probleme vient de l'utilisation de ces deux la simultanement ou bien si c'est mon implementation de linear conflicts qui rame (ou bug ?)

def linear_conflict_heuristic(state):
	# tic = time.time()

	# print('GOAL_STATE = ')
	# print(constant.GLOBAL_STATE_DICT2)
	# print()
	# print('INITIAL STATE = ')
	# print(state)
	# print()


	# result = 0
	result = manhattan_heuristic(state)
	for current_position,current_num in state.items():
		goal_position = constant.GLOBAL_STATE_DICT[current_num]

		if current_num != 0:
			# print(f"{current_num}:{current_position}")

			if current_position[0] == goal_position[0]:
				# print(f"	--> same_row!")
				
				if goal_position[1] <= current_position[1]:
					# print(f"		--> to the left! from {current_position[1]} to {goal_position[1]}")
					for test in range(goal_position[1], current_position[1]):
						new_num = state[(current_position[0], test)]
						if new_num != 0:
							# print(f"			NUM2={new_num}{(current_position[0], test)}	GOAL={constant.GLOBAL_STATE_DICT[new_num]}")
							if goal_position[0] == constant.GLOBAL_STATE_DICT[new_num][0]:
								if goal_position[1] < constant.GLOBAL_STATE_DICT[new_num][1]:
									# print(f"####################################################### CONFLICT TILES ==> {current_num} & {new_num}")
									result += 1

				else:
					# print(f"		--> to the right! from {current_position[1]} to {goal_position[1]}")
					for test in range(current_position[1], goal_position[1]):
						new_num = state[(current_position[0], test)]
						if new_num != 0:
							# print(f"			NUM2={new_num}{(current_position[0], test)}	GOAL={constant.GLOBAL_STATE_DICT[new_num]}")
							if goal_position[0] == constant.GLOBAL_STATE_DICT[new_num][0]:
								if goal_position[1] > constant.GLOBAL_STATE_DICT[new_num][1]:
									# print(f"####################################################### CONFLICT TILES ==> {current_num} & {new_num}")
									result += 1


			if current_position[1] == goal_position[1]:
				position = goal_position[0]
				# print(f"	--> same_column!")

				if goal_position[0] <= current_position[0]:
					# print(f"		--> to the up! from {current_position[0]} to {goal_position[0]}")
					for test in range(goal_position[0], current_position[0]):
						new_num = state[(current_position[1], test)]
						if new_num != 0:
							# print(f"			NUM2={new_num}{(current_position[0], test)}	GOAL={constant.GLOBAL_STATE_DICT[new_num]}")
							if goal_position[1] == constant.GLOBAL_STATE_DICT[new_num][1]:
								if goal_position[0] < constant.GLOBAL_STATE_DICT[new_num][0]:
									# print(f"####################################################### CONFLICT TILES ==> {current_num} & {new_num}")
									result += 1

				else:
					# print(f"		--> to the down! from {current_position[0]} to {goal_position[0]}")
					for test in range(current_position[0], goal_position[0]):
						new_num = state[(current_position[1], test)]
						if new_num != 0:
							# print(f"			NUM2={new_num}{(current_position[0], test)}	GOAL={constant.GLOBAL_STATE_DICT[new_num]}")
							if goal_position[1] == constant.GLOBAL_STATE_DICT[new_num][1]:
								if goal_position[0] > constant.GLOBAL_STATE_DICT[new_num][0]:
									# print(f"####################################################### CONFLICT TILES ==> {current_num} & {new_num}")
									result += 1


	# print('LINEAR', (time.time() - tic) * 1000)
	# print(f"RESULT END = {result}")
	# exit()
	return result