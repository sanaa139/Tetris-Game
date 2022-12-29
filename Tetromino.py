class Tetromino():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        
    
class O_Tetromino():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = (255, 190, 11)
        self.boardPositions = [ [int(self.WIDTH/2) - 1, 0], [int(self.WIDTH/2),0], [int(self.WIDTH/2)- 1, 1], [int(self.WIDTH/2),1] ]
        
class I_Tetromino():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = (58, 134, 255)
        self.boardPositions = [ [int(self.WIDTH/2) - 2, 0], [int(self.WIDTH/2) - 1,0], [int(self.WIDTH/2), 0], [int(self.WIDTH/2) + 1,0] ]
        
class T_Tetromino():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = (255, 0, 110)
        self.boardPositions = [ [int(self.WIDTH/2), 0], [int(self.WIDTH/2) - 1,1], [int(self.WIDTH/2), 1], [int(self.WIDTH/2) + 1,1] ]
        
class J_Tetromino():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = (128, 147, 241)
        self.boardPositions = [ [int(self.WIDTH/2) - 2, 0], [int(self.WIDTH/2) - 2,1], [int(self.WIDTH/2) - 1, 1], [int(self.WIDTH/2),1] ]
        
class L_Tetromino():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = (251, 86, 7)
        self.boardPositions = [ [int(self.WIDTH/2) - 2, 1], [int(self.WIDTH/2) - 1,1], [int(self.WIDTH/2), 1], [int(self.WIDTH/2),0] ]
        
class S_Tetromino():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = (124, 181, 24)
        self.boardPositions = [ [int(self.WIDTH/2) - 1, 1], [int(self.WIDTH/2),1], [int(self.WIDTH/2), 0], [int(self.WIDTH/2) + 1,0] ]
        
class Z_Tetromino():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.color = (217, 4, 41)
        self.boardPositions = [ [int(self.WIDTH/2) - 1, 0], [int(self.WIDTH/2),0], [int(self.WIDTH/2), 1], [int(self.WIDTH/2) + 1,1] ]