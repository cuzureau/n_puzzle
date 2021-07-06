from solvability import puzzle_is_solvable
from utils import define_goal_state
from solver import solve
from parser import parse
from printer import display


def main():
    initial_state, size, heuristic = parse()
    if not all([initial_state, size, heuristic]):
        exit()

    goal_state = define_goal_state(size)
    if puzzle_is_solvable(initial_state, goal_state, size):
        path, node_count = solve(heuristic, initial_state, goal_state, size)
        if not all([path, node_count]):
            exit()
        display(path, node_count)
    else:
        print('Sadly... puzzle initial state is unsolvable.')


if __name__ == '__main__':
    main()
