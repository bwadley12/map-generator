import pygame
import input_box, print_button

pygame.init()

LIGHT_GRAY = pygame.Color(200,200,200)

class Menu:
    def __init__(self, x, width, height, rows, columns, grid):
        self.menu_items = []
        self.x = x
        self.width = width
        self.height = height
        self.rows = rows
        self.columns = columns
        self.element_height = 20

        self.menu_items.append(input_box.InputBox(self.x, len(self.menu_items)*self.element_height, self.element_height, self.element_height, str(rows), "Rows"))
        self.menu_items.append(input_box.InputBox(self.x, len(self.menu_items)*self.element_height, self.element_height, self.element_height, str(columns), "Columns"))
        self.menu_items.append(print_button.PrintButton(self.x, len(self.menu_items)*self.element_height, self.element_height,self.width, LIGHT_GRAY, grid))


    def get_menu(self):
        return self.menu_items    

    def update_grid(self, new_grid):
        for item in self.menu_items:
            if isinstance(item, print_button.PrintButton):
                item.update_grid(new_grid)
        #self.menu_items[2]