class Board:
    def __init__(self, board):
        self.board = board

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None
    def valid_in_row(self, row, num):
        return num not in self.board[row]
    
    def valid_in_col(self, col, num):
        pass