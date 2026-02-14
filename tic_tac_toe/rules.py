class Rules:
    def _get_left_diagonal(self, board):
        return [board.box[i][i] for i in range(len(board.box))]
    
    def _get_right_diagonal(self, board):
        return [board.box[i][len(board.box)-1-i] for i in range(len(board.box))]
    
    def _is_winning_line(self, line):
        if len(set(line)) == 1 and line[0] != ' ':
            return True
        return False
    
    def _get_all_cols(self, board):
        size = len(board.box)
        return [
            [board.box[row][col] for row in range(size)]
            for col in range(size)
        ]

    def has_winner(self, board):
        for val in board.box:
            if self._is_winning_line(val):
                return True
            
        for val in self._get_all_cols(board):
            if self._is_winning_line(val):
                return True
            
        if self._is_winning_line(self._get_left_diagonal(board)):
            return True
        
        if self._is_winning_line(self._get_right_diagonal(board)):
            return True
        
        return False
    
    def is_draw(self, board):
        for val in board.box:
            if ' ' in val:
                return False
        return True