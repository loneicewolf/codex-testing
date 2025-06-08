"""Play Tic-Tac-Toe against a simple AI using the minimax algorithm."""

from typing import List, Optional

PLAYER, AI = 'X', 'O'


def print_board(board: List[str]) -> None:
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
    print()


def check_winner(board: List[str]) -> Optional[str]:
    lines = [
        board[0:3], board[3:6], board[6:9],
        board[0:9:3], board[1:9:3], board[2:9:3],
        [board[0], board[4], board[8]], [board[2], board[4], board[6]]
    ]
    for line in lines:
        if line[0] != ' ' and line.count(line[0]) == 3:
            return line[0]
    if ' ' not in board:
        return 'Tie'
    return None


def minimax(board: List[str], is_ai: bool) -> int:
    winner = check_winner(board)
    if winner == AI:
        return 1
    if winner == PLAYER:
        return -1
    if winner == 'Tie':
        return 0

    scores = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI if is_ai else PLAYER
            score = minimax(board, not is_ai)
            scores.append(score)
            board[i] = ' '
    return max(scores) if is_ai else min(scores)


def best_move(board: List[str]) -> int:
    best_score, move = -float('inf'), -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score, move = score, i
    return move


def main() -> None:
    board = [' '] * 9
    print("You are X. Enter positions 0-8.")
    while True:
        print_board(board)
        user = int(input('Move: '))
        if board[user] != ' ':
            print('Invalid move.')
            continue
        board[user] = PLAYER
        if check_winner(board):
            break
        ai_move = best_move(board)
        board[ai_move] = AI
        if check_winner(board):
            break
    print_board(board)
    result = check_winner(board)
    if result == 'Tie':
        print('It\'s a tie!')
    else:
        print(f'{result} wins!')


if __name__ == '__main__':
    main()
