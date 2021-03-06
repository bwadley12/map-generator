import pygame, sys, math
import map 
from menu_components import menu as Menu, buttons

default_screen_height = 750
default_screen_width = 1000
menu_width = 200 # screen width does not include menu_width

rows = 50
columns = 50

select_multiple = False
pygame.init()

def setup_new_grid():
    _tile_size_x = math.floor(default_screen_width/columns)
    _tile_size_y = math.floor(default_screen_height/rows)
    _tile_size = min(_tile_size_x, _tile_size_y)

    _game_board_x = columns*_tile_size
    _screen_height = rows*_tile_size + 1

    _screen_width = _game_board_x + menu_width
    _display_screen = pygame.display.set_mode((_screen_width, _screen_height))
    _map = map.Map(rows, columns, _tile_size) 
    _menu = Menu.Menu(_game_board_x, menu_width, _screen_height, rows, columns, _map.get_tile_states(), _tile_size)

    return _display_screen, _map, _tile_size, _game_board_x, _screen_height, _screen_width, _menu

display_screen, active_map, tile_size, game_board_x, screen_height, screen_width, menu = setup_new_grid()

WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)

while True:
    
    # Handle events
    for event in pygame.event.get():
        for item in menu.get_menu():
            if isinstance(item, buttons.ResetButton):
                if item.handle_event(event):
                    rows, columns = menu.get_row_and_column_inputs()
                    display_screen, active_map, tile_size, game_board_x, screen_height, screen_width, menu = setup_new_grid()                    
            else:
                item.handle_event(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keys_pressed = pygame.key.get_pressed()
            
            if(keys_pressed[pygame.K_LSHIFT]):
                select_multiple = True

            if(keys_pressed[pygame.K_w]):
                active_map.change_active_tile_states(1)
                menu.update_grid(active_map.get_tile_states())
            elif(keys_pressed[pygame.K_s]):
                active_map.change_active_tile_states(-1)
                menu.update_grid(active_map.get_tile_states())
            elif(keys_pressed[pygame.K_RIGHT]):
                active_map.increment_active_tile(1,0, select_multiple)
            elif(keys_pressed[pygame.K_LEFT]):
                active_map.increment_active_tile(-1,0, select_multiple)
            elif(keys_pressed[pygame.K_UP]):
                active_map.increment_active_tile(0,-1, select_multiple)
            elif(keys_pressed[pygame.K_DOWN]):
                active_map.increment_active_tile(0,1, select_multiple)
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                select_multiple = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            x_grid = math.floor(x/tile_size)
            y_grid = math.floor(y/tile_size)
            
            if x_grid < columns: 
                active_map.set_active_tile(x_grid, y_grid, select_multiple)

            else:
                active_map.active_tiles.clear_list()

    # Update the display screen
    display_screen.fill(WHITE)

    # Draw grid
    for y_pos in range(rows):
        for x_pos in range(columns):
            display_screen.blit(active_map.tile_list[x_pos][y_pos].image, active_map.tile_list[x_pos][y_pos].rect)
    # Draw menu
    for item in menu.get_menu():
        item.draw(display_screen)

    # Highlight the selected grid - maybe make into drawing one rect
    for tile in active_map.active_tiles.get_tiles():
        pygame.draw.line(display_screen, BLACK, (tile.x_pos*tile_size, tile.y_pos*tile_size), ((tile.x_pos+1)*tile_size, tile.y_pos*tile_size))
        pygame.draw.line(display_screen, BLACK, (tile.x_pos*tile_size, (tile.y_pos+1)*tile_size), ((tile.x_pos+1)*tile_size, (tile.y_pos+1)*tile_size))
        pygame.draw.line(display_screen, BLACK, (tile.x_pos*tile_size, (tile.y_pos)*tile_size), (tile.x_pos*tile_size, (tile.y_pos+1)*tile_size))
        pygame.draw.line(display_screen, BLACK, ((tile.x_pos+1)*tile_size, tile.y_pos*tile_size), ((tile.x_pos+1)*tile_size, (tile.y_pos+1)*tile_size))

    pygame.display.update()
