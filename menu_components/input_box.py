import pygame
from menu_components import IMenuItem

pygame.init()

Inactive_box_color = pygame.Color(200,200,255)
Active_box_color = pygame.Color(150,150,255)
BLACK = pygame.Color(0,0,0)
Font = pygame.font.SysFont("Calibri", 15)

class InputBox(IMenuItem.IMenuItem):
    def __init__(self,x,y,height,width,inner_text, text_label, element_height):
        self.rect = pygame.Rect(x,y,height,width)
        self.color = Inactive_box_color
        self.inner_text = inner_text
        self.text_label = text_label
        self.active = False
        self.text_label_surface = Font.render(self.text_label, True, BLACK)
        self.element_height = element_height
        self.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if not self.active:
                    self.temp_inner_text = self.inner_text
                    self.active = True
            else:
                if self.inner_text == "":
                    self.inner_text = self.temp_inner_text
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                keys_pressed = pygame.key.get_pressed()

                if event.unicode in "1234567890" and int(self.inner_text + event.unicode) < 250:
                    self.inner_text += event.unicode
                elif keys_pressed[pygame.K_BACKSPACE]:
                    self.inner_text = self.inner_text[:-1]
                
        self.update()

    def update(self):
        self.inner_text_surface = Font.render(self.inner_text, True, BLACK)

        if self.active:
            self.color = Active_box_color 
        else:
            self.color = Inactive_box_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.inner_text_surface, (self.rect.centerx - self.inner_text_surface.get_width()/2, self.rect.centery - self.inner_text_surface.get_height()/2))
        screen.blit(self.text_label_surface, (self.rect.x + self.rect.width + 5,self.rect.y + self.element_height/2 - self.text_label_surface.get_height()/2))

    def get_input(self):
        return int(self.inner_text)