import sys, pygame
from Tetromino import O_Tetromino, I_Tetromino, T_Tetromino, J_Tetromino, L_Tetromino, S_Tetromino, Z_Tetromino
pygame.init()

class Board:
    def __init__(self, WIDTH, HEIGHT, TILE_SIZE, screen):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TILE_SIZE = TILE_SIZE
        self.screen = screen
        
    def draw_board(self):
        for i in range(self.WIDTH):
            for j in range(self.HEIGHT):
                pygame.draw.rect(self.screen, (0, 8, 20), pygame.Rect(i * self.TILE_SIZE, j * self.TILE_SIZE, self.TILE_SIZE - 1, self.TILE_SIZE - 1))
        pygame.display.flip()
        
    def create_new_tetromino(self, typeOfTetromino):
        if typeOfTetromino == 0:
            new_tetromino = O_Tetromino(self.WIDTH, self.HEIGHT)
        elif typeOfTetromino == 1:
            new_tetromino = I_Tetromino(self.WIDTH, self.HEIGHT)    
        elif typeOfTetromino == 2:
            new_tetromino = T_Tetromino(self.WIDTH, self.HEIGHT)
        elif typeOfTetromino == 3:
            new_tetromino = J_Tetromino(self.WIDTH, self.HEIGHT)
        elif typeOfTetromino == 4:
            new_tetromino = L_Tetromino(self.WIDTH, self.HEIGHT)
        elif typeOfTetromino == 5:
            new_tetromino = S_Tetromino(self.WIDTH, self.HEIGHT)
        elif typeOfTetromino == 6:
            new_tetromino = Z_Tetromino(self.WIDTH, self.HEIGHT)
    
        return new_tetromino
        
    def draw_new_tetromino(self, new_tetromino):
        try:    
            for tetromino_blocks in new_tetromino.boardPositions:
                pygame.draw.rect(self.screen, new_tetromino.color, pygame.Rect(tetromino_blocks[0] * self.TILE_SIZE, tetromino_blocks[1] * self.TILE_SIZE, self.TILE_SIZE - 1, self.TILE_SIZE - 1))
            pygame.display.flip()
        except RuntimeError:
            print("Tetromino of given type doesnt exist!")
        
            
        