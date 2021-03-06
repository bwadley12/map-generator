import pygame
from menu_components import IMenuItem

class Checkbox(IMenuItem.IMenuItem):
    def __init__(self, x, y, size_outer, size_inner, color_outer, color_inner, text, text_color, font, element_height):
        self.x = x
        self.y = y
        self.size_outer = size_outer
        self.checked = True
        self.outer_box = pygame.Rect(x, y, size_outer, size_outer)
        self.inner_box = pygame.Rect(x + size_outer/2 - size_inner/2, y + size_outer/2 - size_inner/2, size_inner, size_inner)
        self.label = font.render(text, True, text_color)
        self.color_outer = color_outer
        self.color_inner = color_inner
        self.element_height = element_height

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.outer_box.collidepoint(event.pos):
                self.checked = not self.checked

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_outer, self.outer_box)
        if self.checked:
           pygame.draw.rect(screen, self.color_inner, self.inner_box)
        screen.blit(self.label, (self.x + self.size_outer + 5, self.y + self.element_height/2 - self.label.get_height()/2))


class Checkbox_Grid_X(Checkbox):
    def __init__(self, x, y, size_outer, size_inner, color_outer, color_inner, text, text_color, font, element_height, rows, width, line_color, tile_size):
        super().__init__(x, y, size_outer, size_inner, color_outer, color_inner, text, text_color, font, element_height)
        self.rows = rows
        self.width = width
        self.line_color = line_color
        self.tile_size = tile_size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_outer, self.outer_box)
        if self.checked:
           pygame.draw.rect(screen, self.color_inner, self.inner_box)
        screen.blit(self.label, (self.x + self.size_outer + 5, self.y + self.element_height/2 - self.label.get_height()/2))

        if self.checked:
            for y_pos in range(self.rows+1):
                pygame.draw.line(screen, self.line_color, (0,self.tile_size*y_pos), (self.width, self.tile_size*y_pos))


class Checkbox_Grid_Y(Checkbox):
    def __init__(self, x, y, size_outer, size_inner, color_outer, color_inner, text, text_color, font, element_height, columns, height, line_color, tile_size):
        super().__init__(x, y, size_outer, size_inner, color_outer, color_inner, text, text_color, font, element_height)
        self.columns = columns
        self.height = height
        self.line_color = line_color
        self.tile_size = tile_size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_outer, self.outer_box)
        if self.checked:
           pygame.draw.rect(screen, self.color_inner, self.inner_box)
        screen.blit(self.label, (self.x + self.size_outer + 5, self.y + self.element_height/2 - self.label.get_height()/2))

        if self.checked:
            for x_pos in range(self.columns+1):
                pygame.draw.line(screen, self.line_color, (x_pos*self.tile_size, 0), (x_pos*self.tile_size, self.height))             
            


        