from contextlib import redirect_stdout
from io import StringIO

from project import show_board, check_winner, generate_board


def test_validate_correct_board():
    board = [' ', 'X', ' ', '|', ' ', 'X', ' ', '|', ' ', 'X', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', ' ', '|', ' ', 'O', ' ', '|', ' ', 'O', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']

    table_output = (
        " X | X | X \n"
        "---|---|---\n"
        "   | O | O \n"
        "---|---|---\n"
        "   |   |   \n"
    )

    output = StringIO()
    with redirect_stdout(output):
        show_board(board)

    assert output.getvalue().strip() == table_output.strip()


def test_check_for_winners():
    index_pattern1 = {1: [1, 'X'], 2: [5, 'O'], 3: [9, ''], 4: [23, 'O'], 5: [27, 'X'], 6: [31, ''], 7: [45, 'O'], 8: [49, ''], 9: [53, 'X']}
    index_pattern2 = {1: [1, 'X'], 2: [5, 'X'], 3: [9, ''], 4: [23, 'O'], 5: [27, 'O'], 6: [31, 'O'], 7: [45, 'X'], 8: [49, ''], 9: [53, 'O']}
    index_pattern3 = {1: [1, 'O'], 2: [5, 'O'], 3: [9, 'X'], 4: [23, 'X'], 5: [27, 'X'], 6: [31, 'O'], 7: [45, 'O'], 8: [49, 'X'], 9: [53, 'X']}

    assert check_winner(index_pattern1, player1_symbol='X', player2_symbol='O') == 'Player'
    assert check_winner(index_pattern2, player1_symbol='X', player2_symbol='O') == 'Machine'
    assert check_winner(index_pattern3, player1_symbol='X', player2_symbol='O') == 'draw'


def test_generate_board():
    assert generate_board() == [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']