import numpy as np

class Board(object):
    def __init__(self, col, row, player1, player2):
        self.row = row
        self.col = col
        self.board_state = np.zeros((row, col))
        self.player1 = player1
        self.player2 = player2
    
    def show_board(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.board_state[i, j], end=" ")
            print()
        print()
            
    def reset_board(self):
        self.board_state = np.zeros((self.row, self.col))
    
    def get_flattened_state(self):
        return np.array(self.board_state.flatten())
    
    def apply_action(self, playerId, indice):
        action_row = int(indice / self.row)
        action_col = int(indice % self.col)
        self.board_state[action_row, action_col] = playerId
        
        if(self.check_winner() == playerId):
            return 1.0
        return 0.0
            
    def check_winner(self):
        for i in range(self.row):
            all_elements_same = True
            for j in range(1, self.col):
                if(self.board_state[i, j] == 0):
                    all_elements_same = False
                    break;
                if(self.board_state[i, j] != self.board_state[i, j - 1]):
                    all_elements_same = False
                    break;
            if(all_elements_same):
                return self.board_state[i, 0]
        
        
        for j in range(self.col):
            all_elements_same = True
            for i in range(1, self.row):
                if(self.board_state[i, j] == 0):
                    all_elements_same = False
                    break;
                if(self.board_state[i, j] != self.board_state[i - 1, j]):
                    all_elements_same = False
                    break
            if(all_elements_same):
                return self.board_state[0, j]
            
        all_diag_elements_same = True
        for i in range(1, self.row):
            if(self.board_state[i, i] == 0):
                all_diag_elements_same = False
                break;
            if(self.board_state[i, i] != self.board_state[i - 1, i - 1]):
                all_diag_elements_same = False
                break;
        if(all_diag_elements_same):
            return self.board_state[0,0]
        
        all_diag_elements_same = True
        for i in range(1, self.row):
            if(self.board_state[i, self.col - 1 - i] == 0):
                all_diag_elements_same = False
                break;
            if(self.board_state[i, self.col - 1 - i] != self.board_state[i - 1, self.col - i]):
                all_diag_elements_same = False
                break;
        if(all_diag_elements_same):
            return self.board_state[0,self.col - 1]
        
        return 0
            
                
                    
                
                    
            
        
        
        