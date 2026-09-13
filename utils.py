import random

def generate_random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]


def calculate_conflicts(board):
    n = len(board)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts