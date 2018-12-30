import random

ALIVE = "X"
DEAD = " "

def empty_board(width, height):
    return [[DEAD for cells in range(height)] for cells in range(width)]


def random_number():
    return random.random()


def random_board(width, height):
    board = empty_board(width, height)
    for x in range(0, width):
        for y in range(0, height):
            number = random_number()
            board[x][y] = ALIVE if random_number() > 0.5 else DEAD

    return board


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
