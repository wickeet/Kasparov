from const import *
from quad import Quad
from piece import *

class Board:

    def __init__(self):
        self.quads = [[0 for _ in range(ROWS)] for col in range(COLS)]
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.quads[row][col] = Quad(row, col)
    
    def _add_pieces(self, color):
        row_pawn, row_other = (1, 0) if color == "black" else (6, 7)

        for col in range(COLS):
            self.quads[row_pawn][col] = Quad(row_pawn, col, Pawn(color)) # Pawns
        
        self.quads[row_other][0] = Quad(row_other, 0, Rook(color)) # Rooks
        self.quads[row_other][7] = Quad(row_other, 7, Rook(color))
        self.quads[row_other][1] = Quad(row_other, 1, Knight(color)) # Knights
        self.quads[row_other][6] = Quad(row_other, 6, Knight(color))
        self.quads[row_other][2] = Quad(row_other, 2, Bishop(color)) # Bishops
        self.quads[row_other][5] = Quad(row_other, 5, Bishop(color))
        self.quads[row_other][3] = Quad(row_other, 3, Queen(color)) # Queen
        self.quads[row_other][4] = Quad(row_other, 4, King(color)) # King
        
        
        