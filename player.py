from circleshape import *
from constants import *


Class Player(circleshape):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__(PLAYER_RADIUS)
