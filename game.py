class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.winner = None

    def check_winner(self):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for a,b,c in combos:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                self.winner = self.board[a]
                return self.winner
        return None

    def make_move(self, position):
        if self.winner:
            return False

        if self.board[position] == "":
            self.board[position] = self.current_player
            self.check_winner()
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def get_board(self):
        return {
            "board": self.board,
            "player": self.current_player,
            "winner": self.winner
        }
