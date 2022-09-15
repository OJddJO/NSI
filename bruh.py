from kandinsky import fill_rect as fRect,draw_string as dStr,get_pixel as gCol,set_pixel as pixel
from ion import *
from random import randint

class Dino:
    
    def __init__(self):
        self.pos = (40, 160)
        self.col= (0, 0, 0)

    def draw(self):
        fRect(self.pos[0], self.pos[1], )