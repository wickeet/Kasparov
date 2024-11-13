import pygame
from const import *
from piece import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False

        self.mouse_x = 0
        self.mouse_y = 0
        self.initial_row = 0
        self.initial_col = 0
        
    
    def update(self, pos):
        self.mouse_x, self.mouse_y = pos
    
    def update_blit(self, surface):
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        img = pygame.image.load(texture)
        img_center = (self.mouse_x, self.mouse_y)
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)
    
    def save_initial(self, pos):
        self.initial_row = pos[1] // QUAD_SIZE
        self.initial_col = pos[0] // QUAD_SIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    
    def undrag_piece(self):
        self.piece.set_texture()
        self.piece = None
        self.dragging = False