
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

    # create board
    self.board = self.make_new_board()


def play(dim_size=20, num_bombs=10):
    # step 1: create the board and plant the bombs
    # step 2: show the user the board and ask for where they want to dig
    # step 3a: if location is a bomb, show game over message
    # step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # step 4: repeat steps 2 and 3a/b until there are no more places to dig -> victory!
    pass
