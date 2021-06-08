import re
import sys
from solvability import puzzle_is_solvable
from solver import solve
import numpy as np
import time
import constant

from test2 import linear_conflict_heuristic



def board_is_valid(board, size):
	if len(board) == size >= 3:
		for row in board:
			if len(row) != size:
				return False
	else:
		return False


def parse_input():
	try:
		file = open(sys.argv[1], 'r')
	except:
		error('open')

	file = [line.strip().split('#')[0] for line in file] 	# remove comments
	file = [line for line in file if len(line) > 0]			# remove empty lines

	# print(f"PARSE")
	# tic = time.time()
	board = []
	size = int(file[0][0])		# TODO max size should be 9
	for fi in file[1:]:
		fi = re.findall('[0-9]+', fi)
		for f in fi:
			board.append(int(f))
	# print(f'{tuple(board)}\n{(time.time() - tic) * 1000}')
	# exit()

	# TODO check if board is valid
	# if board_is_valid(board, puzzle_size) == False:
	# 	error('invalid')

	return size, tuple(board)


def error(name):
	if name == 'usage':
		print(f"Usage:\n\tpython3 {sys.argv[0]} <puzzle_file>")
	elif name == 'open':
		print(f"Error:\n\tfile '{sys.argv[1]}' cannot be open")
	elif name == 'invalid':
		print(f"Error:\n\tthe board is not valid")
	elif name == 'unsolvable':
		print(f"Error:\n\tthe puzzle is unsolvable")
	exit()


def generate_board():
	print("generate random board")

	# ADD DETAILS
	arr = np.arange(9).reshape((3, 3))
	arr2 = np.random.permutation(arr)

	return arr2


def main():
	if 1 <= len(sys.argv) <= 2:
		# TODO board generation
		# if len(sys.argv) == 1:
		# 	initial_state = generate_board()
		# else:
		size, initial_state = parse_input()
		
		constant.define_goal_state(size)

		# TODO check if puzzle is solvable
		# if puzzle_is_solvable(initial_state):
		if True:				# to be deleted
			tic = time.time()

			path = solve(initial_state)

			print('solver', time.time() - tic)
		# else:
		# 	error('unsolvable')
	else:
		error('usage')


if __name__ == '__main__':
	main()
