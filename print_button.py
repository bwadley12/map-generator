import button, pygame

pygame.init()

class PrintButton(button.Button):
    def __init__(self,x,y,height,width,color,grid):
        super().__init__(x,y,height,width,color,)
        self.grid = grid

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.collidepoint(event.pos):
                #    print(active_map.get_tile_states())
                print(self.grid)


    def update_grid(self, grid):
        self.grid = grid