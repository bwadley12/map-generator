import pygame
import menu_item

pygame.init()

Inactive_box_color = pygame.Color(200,200,255)
Active_box_color = pygame.Color(150,150,255)
BLACK = pygame.Color(0,0,0)
Font = pygame.font.SysFont("Calibri", 14)

class InputBox(menu_item.MenuItem):
    def __init__(self,x,y,length,width,inner_text, text_label):
        self.rect = pygame.Rect(x,y,length,width)
        self.color = Inactive_box_color
        self.inner_text = inner_text
        self.text_label = text_label
        self.active = False
        self.text_label_surface = Font.render(self.text_label, True, BLACK)
        self.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if not self.active:
                    self.inner_text = ""
                    self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                self.inner_text += event.unicode
                
        self.update()

    def update(self):
        self.inner_text_surface = Font.render(self.inner_text, True, BLACK)

        if self.active:
            self.color = Active_box_color 
        else:
            self.color = Inactive_box_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.inner_text_surface, (self.rect.x + 5, self.rect.y + 5))
        screen.blit(self.text_label_surface, (self.rect.x + self.rect.width + 5,self.rect.y + 5))

    def get_input(self):
        return int(self.inner_text)
        

