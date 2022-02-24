import pytest

from sudoku_solver.identify_potential_digits import (
    get_digits_in_row,
    get_digits_in_column,
    get_digits_in_sector,
)

board = (
    "070000043040009610800634900094052000358460020000800530080070091902100005007040802"
)


@pytest.mark.parametrize(
    "row_index,expected_digits",
    [
        (0, {"7", "4", "3"}),
        (1, {"4", "9", "6", "1"}),
        (8, {"7", "4", "8", "2"}),
    ],
)
@pytest.mark.parametrize("column_index", list(range(9)))
def test_get_digits_in_row(row_index, column_index, expected_digits):
    assert get_digits_in_row(row_index * 9 + column_index, board) == expected_digits


@pytest.mark.parametrize(
    "column_index,expected_digits",
    [
        (0, {"8", "3", "9"}),
        (1, {"7", "4", "9", "5", "8"}),
        (8, {"3", "1", "5", "2"}),
    ],
)
@pytest.mark.parametrize("row_index", list(range(9)))
def test_get_digits_in_column(row_index, column_index, expected_digits):
    assert get_digits_in_column(row_index * 9 + column_index, board) == expected_digits


@pytest.mark.parametrize(
    "position,expected_digits",
    [(position, {"7", "4", "8"}) for position in [0, 1, 2, 9, 10, 11, 18, 19, 20]]
    + [
        (position, {"9", "6", "3", "4"})
        for position in [3, 4, 5, 12, 13, 14, 21, 22, 23]
    ]
    + [
        (position, {"9", "1", "5", "8", "2"})
        for position in [60, 61, 62, 69, 70, 71, 78, 79, 80]
    ],
)
def test_get_digits_in_sector(position, expected_digits):
    assert get_digits_in_sector(position, board) == expected_digits
