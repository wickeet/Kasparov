import pygame
import sys

from const import *
from game import Game

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ajedrez")
        self.game = Game()

    def mainloop(self):

        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger
        
        while True:

            game.show_bg(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicks
                    dragger.update(event.pos)
                    clicked_row, clicked_col = dragger.mouse_y // QUAD_SIZE, dragger.mouse_x // QUAD_SIZE

                    if board.quads[clicked_row][clicked_col].has_piece(): # If the clicked quad has a piece
                        piece = board.quads[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                elif event.type == pygame.MOUSEMOTION: # If the user moves the mouse
                    if dragger.dragging:
                        dragger.update(event.pos)
                        dragger.update_blit(screen)

                elif event.type == pygame.MOUSEBUTTONUP: # If the user releases the click
                    dragger.undrag_piece()

                elif event.type == pygame.QUIT: # If the user closes the window
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

main = Main()
main.mainloop()