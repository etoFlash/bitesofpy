WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for i in range(size):
        s = ""
        for j in range(size):
            if i % 2 + j % 2 == 1:
                s += BLACK
            else:
                s += WHITE
        print(s)
