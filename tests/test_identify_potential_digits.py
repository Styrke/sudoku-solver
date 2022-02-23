import pytest

from sudoku_solver.identify_potential_digits import (
    get_digits_in_row,
    get_digits_in_column,
)

board = (
    "070000043040009610800634900094052000358460020000800530080070091902100005007040802"
)


@pytest.mark.parametrize(
    "row_index,_board,expected_digits",
    [
        (0, board, ["7", "4", "3"]),
        (1, board, ["4", "9", "6", "1"]),
        (8, board, ["7", "4", "8", "2"]),
    ],
)
@pytest.mark.parametrize("column_index", list(range(9)))
def test_get_digits_in_row(row_index, column_index, _board, expected_digits):
    assert get_digits_in_row(row_index * 9 + column_index, _board) == expected_digits


@pytest.mark.parametrize(
    "column_index,_board,expected_digits",
    [
        (0, board, ["8", "3", "9"]),
        (1, board, ["7", "4", "9", "5", "8"]),
        (8, board, ["3", "1", "5", "2"]),
    ],
)
@pytest.mark.parametrize("row_index", list(range(9)))
def test_get_digits_in_column(row_index, column_index, _board, expected_digits):
    assert get_digits_in_column(row_index * 9 + column_index, _board) == expected_digits
