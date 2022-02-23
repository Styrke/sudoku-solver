def sudoku_print(board: str):
    board = board.replace("0", " ")
    for line in range(9):
        print(board[9*line:9*line+3] + " | " + board[9*line+3:9*line+6] + " | " + board[9*line+6:9*line+9])
        if line in (2, 5):
            print("-"*4 + "+" + "-"*5 + "+" + "-"*4)


if __name__ == '__main__':
    with open('../sudoku.csv') as f:
        f.readline()  # Skip the header line
        s = f.readline()

    puzzle, solution = s.split(",")

    print(puzzle)
    print(solution)

    sudoku_print(puzzle)
