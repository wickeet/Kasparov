from math import inf
import os

class Piece:
    
    def __init__(self, name, color, value, img=None, texture_rect=None):
        
        self.name = name
        self.color = color
        self.value = value * (-1 if color == "black" else 1)

        self.texture = img
        self.set_texture()
        self.texture_rect = texture_rect
        
        self.moved = False
        self.moves = []
    
    def add_move(self, move):
        self.moves.append(move)
    
    def set_texture(self, size=80):
        self.texture = os.path.join(f'assets/img/imgs-{size}px/{self.color}_{self.name}.png')


class Pawn(Piece):
    
    def __init__(self, color):
        self.direction = -1 if color == "black" else 1
        super().__init__("pawn", color, 1.0)

class Knight(Piece):

    def __init__(self, color):
        super().__init__("knight", color, 3.0)

class Bishop(Piece):
    
    def __init__(self, color):
        super().__init__("bishop", color, 3.0)

class Rook(Piece):

    def __init__(self, color):
        super().__init__("rook", color, 5.0)

class Queen(Piece):
    
    def __init__(self, color):
        super().__init__("queen", color, 9.0)

class King(Piece):
    
    def __init__(self, color):
        super().__init__("king", color, inf)
