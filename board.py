class Board:
    def __init__(self, board_size):
        self.board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
    
    def isEmpty(self,x,y):
        if x < len(self.board) and y < len(self.board):
            if self.board[x][y] == -1:
                return True
        return False
    
    def setValue(self, player, x, y):
        if self.isEmpty(x,y):
            self.board[x][y] = player[0]
    
    def get(self):
        return self.board
    
    def getSize(self):
        return len(self.board)

    def __str__(self):
        board_to_print = ' '+'--- ' * len(self.board) + '\n'
        for x in self.board:
            board_to_print += '|'
            for y in x:
                if y == -1: y = ' '
                board_to_print += ' ' + y + ' |'
            board_to_print += '\n '+'--- ' * len(self.board) + '\n'
        return board_to_print