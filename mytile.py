import pygame

class MyTile():
    def __init__(self, x_pos, y_pos, tile_size, image_list):
        self.possible_states = image_list
        self.current_state = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tile_size = tile_size

        self.change_state(0)

    def change_state(self, change_direction):
        if (change_direction > 0):
             if(self.current_state < len(self.possible_states) - 1):
                self.current_state += change_direction
             else:
                 self.current_state = 0

        elif(change_direction < 0):
            if(self.current_state > 0):
                self.current_state += change_direction
            else:
                self.current_state = len(self.possible_states) - 1

        self.image = self.possible_states[self.current_state]
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos*self.tile_size
        self.rect.y = self.y_pos*self.tile_size

    def get_state(self):
        return self.current_state
    