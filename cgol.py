import random
import time


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


def get_next_cell_state(coordinates, board):
    width = len(board)
    height = len(board[0])
    x = coordinates[0]
    y = coordinates[1]
    live_neighbours = 0

    for x1 in range((x-1), (x+1)+1):
        if x1 < 0 or x1 >= width: continue

        for y1 in range((y-1), (y+1)+1):
            if y1 < 0 or y1 >= height: continue
            if x1 == x and y1 == y: continue

            if board[x1][y1] == ALIVE:
                live_neighbours += 1

    if board[x][y] == ALIVE:
        if live_neighbours <= 1:
            return DEAD
        elif live_neighbours <= 3:
            return ALIVE
        else:
            return DEAD
    else:
        if live_neighbours == 3:
            return ALIVE
        else:
            return DEAD


def next_board_state(board):
    width = len(board)
    height = len(board[0])
    next_board = empty_board(width, height)

    for x in range(0, width):
        for y in range(0, height):
            next_board[x][y] = get_next_cell_state((x, y), board)

    return next_board


def pretty_print(board):
    display_as = {
        DEAD: ' ',
        ALIVE: 'O'
    }
    width = len(board)
    height = len(board[0])
    lines = []
    for y in range(0, height):
        line = ''
        for x in range(0, width):
            line += display_as[board[x][y]] * 2
        lines.append(line)
    print "\n".join(lines)


def run(board):
    next_state = board
    while True:
        pretty_print(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.08)


if __name__ == "__main__":
    run(random_board(60, 20))
