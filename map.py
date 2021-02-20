import pygame
import mytile

class Map():
    def __init__(self, rows, columns, tile_size):
        self.rows = rows
        self.columns = columns
        self.active_tile_x = 0
        self.active_tile_y = 0
        self.tile_size = tile_size
        self.tile_list = []

        for x_pos in range(self.columns):
            self.tile_list.append([])
            for y_pos in range(self.rows):
                new_tile = mytile.MyTile(x_pos, y_pos, self.tile_size)
                self.tile_list[x_pos].append(new_tile)

    def set_active_tile(self, x_grid, y_grid):
        self.active_tile_x = x_grid
        self.active_tile_y = y_grid

    def increment_active_tile(self, change_x, change_y):
        if change_x != 0:
            if(change_x > 0):
                if(self.active_tile_x < len(self.tile_list) - 1):
                    self.active_tile_x += change_x
                else:
                    self.active_tile_x = 0
            else:
                if(self.active_tile_x > 0):
                    self.active_tile_x += change_x
                else:
                    self.active_tile_x = len(self.tile_list) - 1

        if change_y != 0:
            if change_y > 0:
                if self.active_tile_y < len(self.tile_list) - 1:
                    self.active_tile_y += change_y
                else:
                    self.active_tile_y = 0
            else:
                if self.active_tile_y > 0:
                    self.active_tile_y += change_y
                else:
                    self.active_tile_y = len(self.tile_list[0]) - 1

    def get_active_tile(self):
        return self.active_tile_x, self.active_tile_y

    def get_tile_states(self):
        states = ""

        for x_pos in range(self.rows):
            for y_pos in range(self.columns):
                states += str(self.tile_list[y_pos][x_pos].get_state()) + ", "
            states += "\n"
    
        return states