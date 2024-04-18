# there are a few syntax mistakes and one logic one. 
# please correct them all before running the game

import os
import random

def clear_screen()
    os.system('cls' if os.name == 'nt' else 'clear')

Def init_board(n=10, m=10):
    return [[random.choice([0, 1]) for _ in range(m)] for _ in range(n)]

def count_neighbors(board, row, col):
    n, m = len(board), len(board[0])
    count = 0
    for i in range(max(0, row-1), min(n, row+2)):
        for j in range(max(0, col-1), min(m, col+2)):
            if (i, j) != (row, col):
                count += board[i][j]
    return count

def next_generation(board):
    n, m = len(board), len(board[0])
    new_board = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == 1 and neighbors in (2, 3):
                new_board[i][j] = 1
            elif board[i][j] == 0 and neighbors == 3:
                new_board[i][j] = 1
    return new_board

def print_board(board):
    for row in board:
        print(' '.join(['*' if cell else ' ' for cell in row]))
    print()

def main():
    board = init_board(20, 40)  # Change dimensions as needed
    try:
        while True:
            clear_screen()
            print_board(board)
            board = next_generation(board)
            time.sleep(0.5)  # Adjust time to control the evolution speed
    except KeyboardInterrupt:
        print("Game of Life terminated.")

if __name__ == "__main()__":
    main()

