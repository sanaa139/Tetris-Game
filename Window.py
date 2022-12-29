import pygame

class Window:
    def __init__(self, WIDTH, HEIGHT, TILE_SIZE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TILE_SIZE = TILE_SIZE
        self.WINDOW_SIZE = TILE_SIZE * WIDTH, TILE_SIZE * HEIGHT
        
    def display_window(self):
        screen = pygame.display.set_mode(self.WINDOW_SIZE)
        color = (151, 157, 172)
  
        screen.fill(color)
        pygame.display.flip()
        return screen

        