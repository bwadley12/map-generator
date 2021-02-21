import pygame
import mytile
import selected_tiles

class Map():
    def __init__(self, rows, columns, tile_size):
        self.rows = rows
        self.columns = columns
        self.tile_size = tile_size

        self.possible_states = [pygame.transform.scale(pygame.image.load("example_tile_image.png"), (tile_size,tile_size)), 
                        pygame.transform.scale(pygame.image.load("example_tile_image2.png"), (tile_size,tile_size)),
                        pygame.transform.scale(pygame.image.load("example_tile_image3.png"), (tile_size,tile_size)),
                        pygame.transform.scale(pygame.image.load("example_tile_image4.png"), (tile_size,tile_size)),]

        self.tile_list = []
        for x_pos in range(self.columns):
            self.tile_list.append([])
            for y_pos in range(self.rows):
                new_tile = mytile.MyTile(x_pos, y_pos, self.tile_size, self.possible_states)
                self.tile_list[x_pos].append(new_tile)

        self.active_tiles = selected_tiles.SelectedTiles()
        self.set_active_tile(0, 0, False)

    def set_active_tile(self, x_grid, y_grid, select_multiple):
        if not select_multiple:
            self.active_tiles.clear_list()

        self.active_tile_x = x_grid
        self.active_tile_y = y_grid
        self.active_tiles.add_tile(self.tile_list[self.active_tile_x][self.active_tile_y])

    def increment_active_tile(self, change_x, change_y, select_multiple):
        if not select_multiple:
            self.active_tiles.clear_list()

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
                    
        self.active_tiles.add_tile(self.tile_list[self.active_tile_x][self.active_tile_y])

    def get_active_tile(self):
        return self.active_tile_x, self.active_tile_y

    def get_tile_states(self):
        states = ""

        for x_pos in range(self.rows):
            for y_pos in range(self.columns):
                states += str(self.tile_list[y_pos][x_pos].get_state()) + ", "
            states += "\n"
    
        return states

    def change_active_tile_states(self, change_direction):
        for tile in self.active_tiles.get_tiles():
            tile.change_state(change_direction)