import pygame

pygame.init()

Inactive_box_color = pygame.Color(200,200,255)
Active_box_color = pygame.Color(150,150,255)
BLACK = pygame.Color(0,0,0)
Font = pygame.font.SysFont("Calibri", 14)

class InputBox():
    def __init__(self,x,y,length,width,inner_text, text_label):
        self.rect = pygame.Rect(x,y,length,width)
        self.color = Inactive_box_color
        self.inner_text = inner_text
        self.text_label = text_label
        self.text_surface = Font.render(self.inner_text, True, BLACK)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if not self.active:
                    self.inner_text = ""
                    #self.text_surface = Font.render(self.inner_text, True, BLACK)
                    self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                keys_pressed = pygame.key.get_pressed()

                self.inner_text += event.unicode
                
        self.update()

    def update(self):
        self.text_surface = Font.render(self.inner_text, True, BLACK)
        
        if self.active:
            self.color = Active_box_color 
        else:
            self.color = Inactive_box_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
        

