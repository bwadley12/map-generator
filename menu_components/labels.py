import pygame
from menu_components import IMenuItem

class LargeLabel(IMenuItem.IMenuItem):
    def __init__(self, x, y, text, font, color, element_height):
        self.text = text
        self.text_surface = font.render(self.text, True, color)
        self.x = x
        self.y = y + element_height/2 - self.text_surface.get_height()/2

    def handle_event(self, event):
        pass
    
    def draw(self, screen):
        screen.blit(self.text_surface, (self.x, self.y))
        