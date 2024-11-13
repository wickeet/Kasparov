import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(surface, LIGHT_GREEN, (col * QUAD_SIZE, row * QUAD_SIZE, QUAD_SIZE, QUAD_SIZE))
                else:
                    pygame.draw.rect(surface, DARK_GREEN, (col * QUAD_SIZE, row * QUAD_SIZE, QUAD_SIZE, QUAD_SIZE))
    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.quads[row][col].has_piece(): # If the quad has a piece
                    if self.board.quads[row][col].piece is not self.dragger.piece: # If the piece is not being dragged
                        img = pygame.image.load(self.board.quads[row][col].piece.texture)
                        img_center = col * QUAD_SIZE + QUAD_SIZE // 2, row * QUAD_SIZE + QUAD_SIZE // 2
                        self.board.quads[row][col].piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, self.board.quads[row][col].piece.texture_rect)