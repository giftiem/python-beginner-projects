def select_cell():
    """
    Prompt the user to select a cell.
    You can do this however you like.

    Return the row and column of that cell.
    """


def result(board):
    """
    Look at the board and determine the result.

    Return
    - "x" if X wins,
    - "o" if O wins,
    - "draw" if it's a draw,
    - "unfinished" if the game is unfinished.
    """


def place(board, cell, player):
    """
    Update the board so that the given player occupies the given cell.

    Return the new board.
    """


def new_board():
    """
    Return an empty board.
    """


def draw(board):
    """
    Draw the board like this:

    ox.
    .x.
    .o.
    """


def play():
    """
    Play an entire game of Tic-Tac-Toe, using all the
    other functions in this project.
    """


if __name__ == "__main__":
    play()