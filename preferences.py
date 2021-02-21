

class Preferences():
    def __init__(self):
        self.x_grid_enabled = True
        self.y_grid_enabled = True

    def get_x_grid_enabled(self):
        return self.x_grid_enabled
    
    def toggle_x_grid_enabled(self):
        self.x_grid_enabled = not self.x_grid_enabled

    def get_y_grid_enabled(self):
        return self.y_grid_enabled
    
    def toggle_y_grid_enabled(self):
        self.y_grid_enabled = not self.y_grid_enabled