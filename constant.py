import numpy as np
import time


def define_goal_state(n):
	tic = time.time()

	global GOAL_STATE
	global BOARD_LENGTH
	global GLOBAL_STATE_DICT
	global GLOBAL_STATE_DICT2
	global GLOBAL_STATE_LIST2
	
	m = [[0] * n for i in range(n)]
	dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
	x, y, c = 0, -1, 1
	for i in range(n + n - 2):
		for j in range((n + n - i) // 2):
			x += dx[i % 4]
			y += dy[i % 4]
			m[x][y] = c
			c += 1

	GOAL_STATE = np.array(m)
	BOARD_LENGTH = len(GOAL_STATE)
	GLOBAL_STATE_DICT = {m[r][c]: (r, c) for r in range(BOARD_LENGTH) for c in range(BOARD_LENGTH)}
	GLOBAL_STATE_DICT2 = {(r, c): m[r][c] for r in range(BOARD_LENGTH) for c in range(BOARD_LENGTH)}
	GLOBAL_STATE_LIST2 = GLOBAL_STATE_DICT2.items()

	print('goal_state', time.time() - tic)