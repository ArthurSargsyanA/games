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

    def get_winner(self, board):
        for val in board.box:
            if self._is_winning_line(val):
                return val[0]
            
        for val in self._get_all_cols(board):
            if self._is_winning_line(val):
                return val[0]
            
        left_diagonal = self._get_left_diagonal(board)
        if self._is_winning_line(left_diagonal):
            return left_diagonal[0]
        
        right_diagonal = self._get_right_diagonal(board)
        if self._is_winning_line(right_diagonal):
            return right_diagonal[0]
        
        return None
    
    def is_draw(self, board):
        for val in board.box:
            if ' ' in val:
                return False
        return True