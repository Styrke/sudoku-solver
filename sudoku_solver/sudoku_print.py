from sudoku_solver.reader import read_sudoku


def sudoku_print(board: str):
    board = board.replace("0", " ")
    for line in range(9):
        print(board[9*line:9*line+3] + " | " + board[9*line+3:9*line+6] + " | " + board[9*line+6:9*line+9])
        if line in (2, 5):
            print("-"*4 + "+" + "-"*5 + "+" + "-"*4)


if __name__ == '__main__':
    puzzle, solution = read_sudoku(0)

    print(puzzle)
    print(solution)

    sudoku_print(puzzle)
