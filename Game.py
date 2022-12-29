import sys, pygame, random, time
from Window import Window
from Board import Board
pygame.init()

class Game():
    def __init__(self, WIDTH, HEIGHT, TILE_SIZE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TILE_SIZE = TILE_SIZE
    
    def run(self):
        window = Window(self.WIDTH, self.HEIGHT, self.TILE_SIZE)
        screen = window.display_window()
        board = Board(self.WIDTH, self.HEIGHT, self.TILE_SIZE, screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                    
            print("Hello")
            
            new_tetromino_type = random.randint(0,7)
            
            board.draw_board()
            new_tetromino = board.create_new_tetromino(2)
            board.draw_new_tetromino(new_tetromino)
            time.sleep(1)
            