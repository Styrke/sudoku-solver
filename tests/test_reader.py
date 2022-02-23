import pytest

from sudoku_solver.reader import read_sudoku


@pytest.mark.parametrize(
    "puzzle_number,expected_puzzle,expected_solution",
    [
        (
            0,
            "070000043040009610800634900094052000358460020000800530080070091902100005007040802",
            "679518243543729618821634957794352186358461729216897534485276391962183475137945862",
        ),
        (
            5,
            "561092730020780090900005046600000427010070003073000819035900670700103080000000050",
            "561492738324786195987315246659831427418279563273564819135928674746153982892647351",
        ),
        (
            9,
            "000003610000015007000008090086000700030800100500120309005060904060900530403701008",
            "728493615349615827651278493186539742932847156574126389815362974267984531493751268",
        ),
    ],
)
def test_read_sudoku(puzzle_number, expected_puzzle, expected_solution):
    puzzle, solution = read_sudoku(
        puzzle_number, sudoku_file="test_data/test_sudokus.csv"
    )
    assert puzzle == expected_puzzle
    assert solution == expected_solution
