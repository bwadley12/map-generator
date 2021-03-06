import pygame
from menu_components import IMenuItem

class Button(IMenuItem.IMenuItem):
    def __init__(self,x,y,height,width, color, text, font, font_color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.font_color = font_color
        self.font = font
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = font.render(text, True, font_color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)
        screen.blit(self.text, (self.rectangle.centerx - self.text.get_width()/2, self.rectangle.centery - self.text.get_height()/2))

    def handle_event(self):
        pass


class PrintButton(Button):
    def __init__(self,x,y,height,width,color,grid, text, font, font_color):
        super().__init__(x,y,height,width,color,text,font, font_color)
        self.grid = grid

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                print(self.grid)


    def update_grid(self, grid):
        self.grid = grid


class ResetButton(Button):
    def __init__(self, x, y, height, width, color, grid, text, font, font_color):
        super().__init__(x,y,height,width,color,text,font, font_color)
        self.grid = grid

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                return True