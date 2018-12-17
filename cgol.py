ALIVE = "X"
DEAD = " "

def empty_board(width, height):
  return [[DEAD for cells in range(height)] for cells in range(width)]

if __name__ == "__main__":
    print empty_board(10, 10)
