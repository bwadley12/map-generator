import pygame
import input_box

pygame.init()

class IMenuItem:

    def handle_event(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class Menu:
    def __init__(self, x, width, height, rows, columns):
        self.menu_items = []
        self.x = x
        self.width = width
        self.height = height
        self.rows = rows
        self.columns = columns
        self.element_height = 20

        self.menu_items.append(input_box.InputBox(self.x, len(self.menu_items)*self.element_height, self.element_height, self.element_height, str(rows), "Rows"))
        self.menu_items.append(input_box.InputBox(self.x, len(self.menu_items)*self.element_height, self.element_height, self.element_height, str(columns), "Columns"))
        

    def get_menu(self):
        return self.menu_items    
