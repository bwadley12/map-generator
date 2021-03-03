import pygame, IMenuItem

pygame.init()

class Button(IMenuItem.IMenuItem):
    def __init__(self,x,y,height,width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)

    def handle_event(self):
        pass


