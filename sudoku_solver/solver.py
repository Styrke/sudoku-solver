from tqdm import tqdm

from sudoku_solver.identify_potential_digits import identify_potential_digits
from sudoku_solver.reader import read_sudoku


def solve(board):
    updated_board = list(board)
    for position in range(81):
        if updated_board[position] != "0":
            continue
        potential_digits = identify_potential_digits(position, "".join(updated_board))
        if len(potential_digits) == 1:
            updated_board[position] = tuple(potential_digits)[0]

    updated_board = "".join(updated_board)
    if board == updated_board:
        return updated_board
    return solve(updated_board)


if __name__ == "__main__":
    num_tests = 10000
    correct = 0
    for i in tqdm(range(num_tests)):
        puzzle, solution = read_sudoku(1)
        correct += solve(puzzle) == solution

    print(f"{correct} out of {num_tests} were solved correctly")
