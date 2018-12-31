import random

ALIVE = "o"
DEAD = " "


def empty_board(width, height):
    return [[DEAD for cells in range(height)] for cells in range(width)]


def random_board(width, height):
    board = empty_board(width, height)
    for x in range(0, width):
        for y in range(0, height):
            number = random.random()
            board[x][y] = ALIVE if number > 0.5 else DEAD

    return board


def live_neighbours(coordinates, board):
    x = coordinates[0]
    y = coordinates[1]
    cell = board[x][y]
    live_neighbours = 0
    if board[x][y + 1] == ALIVE and (y + 1) < len(board):
        live_neighbours += 1
    if board[x][y - 1] == ALIVE and (y - 1) >= 0:
        live_neighbours += 1
    if board[x + 1][y] == ALIVE and (x + 1) < len(board[0]):
        live_neighbours += 1
    if board[x - 1][y] == ALIVE and (x - 1) >= 0:
        live_neighbours += 1
        
    return live_neighbours


def pretty_print(board, width, height):
    rows = []
    game_board = board(width, height)
    for y in range(0, height):
        row = ''
        for x in range(0, width):
            row += game_board[x][y]
        rows.append(row)
    print "\n".join(rows)


if __name__ == "__main__":
    pretty_print(random_board, 60, 20)
