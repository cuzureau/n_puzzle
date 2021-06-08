# import time


def define_goal_state(length):
	# tic = time.time()

	global GOAL_STATE
	global BOARD_LENGTH
	global EMPTY_TILE
	global NUMBER_OF_TILES

	m = [[0] * length for i in range(length)]
	dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
	x, y, c = 0, -1, 1
	for i in range(length + length - 2):
		for j in range((length + length - i) // 2):
			x += dx[i % 4]
			y += dy[i % 4]
			m[x][y] = c
			c += 1
	n = []
	for i in m:
		for j in i:
			n.append(j)

	GOAL_STATE = tuple(n)
	BOARD_LENGTH = length
	EMPTY_TILE = 0
	NUMBER_OF_TILES = length * length

	# print('goal_state', time.time() - tic)
