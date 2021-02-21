

class SelectedTiles():
    def __init__(self):
        self.selected_tiles = []

    def add_tile(self, tile_to_add):
        if not tile_to_add in self.selected_tiles:
            self.selected_tiles.append(tile_to_add)
    
    def remove(self, tile):
        self.selected_tiles.remove(tile)
    
    def clear_list(self):
        self.selected_tiles.clear()

    def get_tiles(self):
        return self.selected_tiles
