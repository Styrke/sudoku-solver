from typing import Set


def get_digits_in_row(position: int, board: str) -> Set[str]:
    """Get all the digits that are in the same row as the given position"""
    row_number = position // 9
    row = board[row_number * 9 : (row_number + 1) * 9]
    return set(row.replace("0", ""))


def get_digits_in_column(position: int, board: str) -> Set[str]:
    """Get all the digits that are in the same column as the given position"""
    column_number = position % 9
    column = board[column_number::9]
    return set(column.replace("0", ""))


def get_digits_in_sector(position: int, board: str) -> Set[str]:
    """Get all the digits that are in the same sector as the given position"""
    sector_row = position // 27
    sector_column = position % 9 // 3
    rows = range(3 * sector_row, 3 * sector_row + 3)
    cols = range(3 * sector_column, 3 * sector_column + 3)
    return {
        board[row * 9 + col]
        for row in rows
        for col in cols
        if board[row * 9 + col] != "0"
    }


def identify_potential_digits(position: int, board: str) -> Set[str]:
    row = set(get_digits_in_row(position, board))
    column = set(get_digits_in_column(position, board))
    sector = set(get_digits_in_sector(position, board))
    all = set(str(digit) for digit in range(1, 10))
    return all.difference(row, column, sector)
