import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Circle
import random

class Connect4Board:
    
    UNPLAYED=0
    PLAYER1=1
    PLAYER2=2
        
    def __init__(self, shape=(6,7)):
        self.board = np.zeros(shape=shape)
    
    def draw_board(self):
        colors = ["white", "red", "blue"]

        # Create a figure and axes
        fig, ax = plt.subplots()
        #color every square to black
        plt.imshow(self.board, cmap=ListedColormap(["black", "black", "black"]), vmin=0, vmax=3)

        # Iterate over the rows and columns of the board
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                # Place the corresponding color where it belongs
                circle = Circle((j, i), 0.5, color=colors[int(self.board[i,j])])
                ax.add_artist(circle)
        # Hide the axis ticks and labels
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # Show the plot
        plt.show()
        
    def check_win(self):
        """
        Determine if either player has won
        Return 0 for no win, 1 or 2 for a
        victory
        """
        
        # Check horizontal
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]-3):
                if(self.board[row, col] == self.board[row, col+1] and 
                  self.board[row, col+1] == self.board[row, col+2] and 
                  self.board[row, col+2] == self.board[row, col+3] and
                  self.board[row, col] != 0):
                    return int(self.board[row,col])
                
        # Check Vertical
        for row in range(self.board.shape[0] - 3):
            for col in range(self.board.shape[1]):
                if(self.board[row, col] != 0 and 
                    self.board[row, col] == self.board[row+1, col] and
                    self.board[row+1, col] == self.board[row+2, col] and
                    self.board[row+2, col] == self.board[row+3, col]):
                    return int(self.board[row,col])
                
        # Check Diag top left to bottom right
        for row in range(self.board.shape[0] - 3):
            for col in range(self.board.shape[1] - 3):
                if(self.board[row, col] != 0 and 
                    self.board[row, col] == self.board[row+1, col+1] and
                    self.board[row+1, col+1] == self.board[row+2, col+2] and
                    self.board[row+2, col+2] == self.board[row+3, col+3]):
                    return int(self.board[row,col])
                
        # Check diag bottom left to top right
        for row in range(3, self.board.shape[0]):
            for col in range(0, self.board.shape[1]-3):
                if(self.board[row, col] != 0 and 
                    self.board[row, col] == self.board[row-1, col+1] and
                    self.board[row-1, col+1] == self.board[row-2, col+2] and
                    self.board[row-2, col+2] == self.board[row-3, col+3]):
                    return int(self.board[row,col])
        
        return 0
    
    def moves(self):
        """Return a list of valid columns the player can play in"""
        valid_moves = []
        for col in range(self.board.shape[1]):
            if self.board[0, col] == 0:
                valid_moves.append(col)
        return valid_moves

    def move(self, player, col):
        """
        Have player place their piece in col
        Return True -> Piece was placed
        Return False -> It was an invalid move
        Return None -> Error state
        """
        
        # Check if move is valid
        if self.board[0, col] != 0:
            return False
        
        # Find the lowest hole
        for row in reversed(range(self.board.shape[0])):
            if self.board[row, col] == 0:
                self.board[row, col] = player
                return True
        
        return None
    
    def get_numpy(self):
        return self.board
    
    def load_board(self, np_board):
        self.board = np_board
        
    def deepcopy(self):
        b_array = np.copy(self.board)
        b_object = Connect4Board() # This needs to handle more than 6x7 but for now it is just 6x7
        b_object.board = b_array
        return b_object