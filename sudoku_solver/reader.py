from typing import Tuple


def read_sudoku(puzzle_number: int, sudoku_file: str = None) -> Tuple[str, str]:
    if not sudoku_file:
        sudoku_file = "../sudoku.csv"
    with open(sudoku_file) as f:
        for i, line in enumerate(f):
            if i != puzzle_number:
                continue
            puzzle, solution = f.readline().strip().split(",")
            return puzzle, solution
