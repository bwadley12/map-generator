
class SelectedTiles():
    def __init__(self):
        self.selected_tiles = []

    def add_tile(self, tile):
        self.selected_tiles.append(tile)
    
    def remove(self, tile):
        self.selected_tiles.remove(tile)
