class TicTacToe:
    def __init__(self):
        self.board = [""] * 9
        self.current_player = "X"

    def make_move(self, position):
        if self.board[position] == "":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def get_board(self):
        return self.board
