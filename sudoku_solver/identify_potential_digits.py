from typing import List


def get_digits_in_row(position: int, board: str) -> List[str]:
    """Get all the digits that are in the same row as the given position"""
    row_number = position // 9
    row = board[row_number * 9 : (row_number + 1) * 9]
    return list(row.replace("0", ""))


def get_digits_in_column(position: int, board: str) -> List[str]:
    """Get all the digits that are in the same column as the given position"""
    column_number = position % 9
    column = board[column_number::9]
    return list(column.replace("0", ""))
