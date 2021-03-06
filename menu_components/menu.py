import pygame
from menu_components import input_box, buttons, labels, checkbox

pygame.init()

WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
LIGHT_GRAY = pygame.Color(200,200,200)
DARK_GRAY = pygame.Color(100,100,100)

font = pygame.font.SysFont("Calibri", 20)
font_small = pygame.font.SysFont("Calibri", 15)

class Menu:
    def __init__(self, x, width, height, rows, columns, grid, tile_size):
        self.menu_items = []
        self.x = x
        self.width = width
        self.height = height
        self.rows = rows
        self.columns = columns
        self.element_height = 30

        # Reset area
        self.menu_items.append(labels.LargeLabel(self.x, len(self.menu_items)*self.element_height, "Reset Grid", font, BLACK, self.element_height))
        self.menu_items.append(input_box.InputBox(self.x, len(self.menu_items)*self.element_height, self.element_height, self.element_height, str(rows), "Rows", self.element_height))
        self.menu_items.append(input_box.InputBox(self.x, len(self.menu_items)*self.element_height, self.element_height, self.element_height, str(columns), "Columns", self.element_height))
        self.menu_items.append(buttons.ResetButton(self.x, len(self.menu_items)*self.element_height, self.element_height,self.width, LIGHT_GRAY, grid, "Reset", font, BLACK))

        # Preferences area
        self.menu_items.append(labels.LargeLabel(self.x, len(self.menu_items)*self.element_height, "Preferences", font, BLACK, self.element_height))
        self.menu_items.append(checkbox.Checkbox_Grid_X(self.x, len(self.menu_items)*self.element_height, self.element_height, self.element_height - 16, LIGHT_GRAY, BLACK, "Enable X Grid", BLACK, font_small, self.element_height, self.rows, self.x, WHITE, tile_size))
        self.menu_items.append(checkbox.Checkbox_Grid_Y(self.x, len(self.menu_items)*self.element_height, self.element_height, self.element_height - 16, LIGHT_GRAY, BLACK, "Enable Y Grid", BLACK, font_small, self.element_height, self.columns, self.height, WHITE, tile_size))

        # Output area
        self.menu_items.append(buttons.PrintButton(self.x, len(self.menu_items)*self.element_height, self.element_height,self.width, LIGHT_GRAY, grid, "Print", font, BLACK))

    def get_menu(self):
        return self.menu_items    

    def update_grid(self, new_grid):
        for item in self.menu_items:
            if isinstance(item, buttons.PrintButton):
                item.update_grid(new_grid)

    def get_row_and_column_inputs(self):
        coordinates = []

        # need a better way to do this in the future. possibly group the entire reset area as its own object stored within 
        # the menu so that input box values are more accessible
        for item in self.menu_items:
            if isinstance(item, input_box.InputBox):
                coordinates.append(item.get_input())
        
        return coordinates[0], coordinates[1]