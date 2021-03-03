import pygame, sys, math
import map, preferences, menu_items

default_screen_height = 750
default_screen_width = 1000
menu_width = 200 # screen width does not include menu_width
menu_padding = 15 
standard_button_height = 40

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
    _preferences = preferences.Preferences()
    _menu = menu_items.Menu(_game_board_x, menu_width, _screen_height, rows, columns)

    return _display_screen, _map, _preferences, _tile_size, _game_board_x, _screen_height, _screen_width, _menu

display_screen, active_map, active_preferences, tile_size, game_board_x, screen_height, screen_width, menu = setup_new_grid()

WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
LIGHT_GRAY = pygame.Color(200,200,200)
DARK_GRAY = pygame.Color(100,100,100)

font = pygame.font.SysFont("Calibri", 20)
font_small = pygame.font.SysFont("Calibri", 15)


"""button = pygame.Rect(game_board_x, screen_height - standard_button_height, menu_width, standard_button_height)
print_display = font.render("Print", True, BLACK)

preferences_display = font.render("Preferences", True, BLACK)
grid_x_toggle = pygame.Rect(game_board_x + menu_padding, 35, 15, 15)
grid_x_toggled_on_rect = pygame.Rect(game_board_x + menu_padding + 4, 39, 7, 7)
grid_x_label = font_small.render("Enable/Disable X grid",True, BLACK)

grid_y_toggle = pygame.Rect(game_board_x + menu_padding, 60, 15, 15)
grid_y_toggled_on_rect = pygame.Rect(game_board_x + menu_padding + 4, 64, 7, 7)
grid_y_label = font_small.render("Enable/Disable Y grid",True, BLACK)

input_box_1 = input_box.InputBox(game_board_x + menu_padding, 85, 30, 20, str(rows), "Rows")
input_box_2 = input_box.InputBox(game_board_x + menu_padding, 115, 30, 20, str(columns), "Columns")
submit_screensize_button = pygame.Rect(game_board_x, 145, menu_width, standard_button_height)
"""
while True:
    display_screen.fill(WHITE)

    # building menu

    for item in menu.get_menu():
        item.draw(display_screen)

    """
    pygame.draw.rect(display_screen, LIGHT_GRAY, button)
    display_screen.blit(print_display, (button.centerx - print_display.get_width()/2, button.centery - print_display.get_height()/2))

    display_screen.blit(preferences_display, (game_board_x + menu_width/2 - preferences_display.get_width()/2, 10))
    pygame.draw.rect(display_screen, BLACK, grid_x_toggle)
    if active_preferences.get_x_grid_enabled():
        pygame.draw.rect(display_screen, LIGHT_GRAY, grid_x_toggled_on_rect)
    
    pygame.draw.rect(display_screen, BLACK, grid_y_toggle)
    if active_preferences.get_y_grid_enabled():
        pygame.draw.rect(display_screen, LIGHT_GRAY, grid_y_toggled_on_rect)

    display_screen.blit(grid_x_label, (grid_x_toggle.right + 10, grid_x_toggle.top))
    display_screen.blit(grid_y_label, (grid_y_toggle.right + 10, grid_y_toggle.top))

    input_box_1.draw(display_screen)
    input_box_2.draw(display_screen)
    pygame.draw.rect(display_screen, LIGHT_GRAY, submit_screensize_button)
    """


    for event in pygame.event.get():

        for item in menu.get_menu():
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
            elif(keys_pressed[pygame.K_s]):
                active_map.change_active_tile_states(-1)
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
            #if button.collidepoint(event.pos):
            #    print(active_map.get_tile_states())
            #"""elif submit_screensize_button.collidepoint(event.pos):
            #    rows = input_box_1.get_input()
            #    columns = input_box_2.get_input()
            #    display_screen, active_map, active_preferences, tile_size, game_board_x, screen_height, screen_width = setup_new_grid()
            #elif grid_x_toggle.collidepoint(event.pos):
            #   active_preferences.toggle_x_grid_enabled()
            #elif grid_y_toggle.collidepoint(event.pos):
            #    active_preferences.toggle_y_grid_enabled()"""
            #else:
            x,y = pygame.mouse.get_pos()
            x_grid = math.floor(x/tile_size)
            y_grid = math.floor(y/tile_size)
            
            if x_grid < columns: 
                active_map.set_active_tile(x_grid, y_grid, select_multiple)

            else:
                active_map.active_tiles.clear_list()

        #input_box_1.handle_event(event)
        #input_box_2.handle_event(event)

    for y_pos in range(rows):
        for x_pos in range(columns):
            display_screen.blit(active_map.tile_list[x_pos][y_pos].image, active_map.tile_list[x_pos][y_pos].rect)

    if active_preferences.get_y_grid_enabled():
        for x_pos in range(columns+1):
            pygame.draw.line(display_screen, WHITE, (x_pos*tile_size,0), (x_pos*tile_size, screen_height))

    if active_preferences.get_x_grid_enabled():
        for y_pos in range(rows+1):
            pygame.draw.line(display_screen, WHITE, (0,tile_size*y_pos), (game_board_x, tile_size*y_pos))

    for tile in active_map.active_tiles.get_tiles():
        pygame.draw.line(display_screen, DARK_GRAY, (tile.x_pos*tile_size, tile.y_pos*tile_size), ((tile.x_pos+1)*tile_size, tile.y_pos*tile_size))
        pygame.draw.line(display_screen, DARK_GRAY, (tile.x_pos*tile_size, (tile.y_pos+1)*tile_size), ((tile.x_pos+1)*tile_size, (tile.y_pos+1)*tile_size))
        pygame.draw.line(display_screen, DARK_GRAY, (tile.x_pos*tile_size, (tile.y_pos)*tile_size), (tile.x_pos*tile_size, (tile.y_pos+1)*tile_size))
        pygame.draw.line(display_screen, DARK_GRAY, ((tile.x_pos+1)*tile_size, tile.y_pos*tile_size), ((tile.x_pos+1)*tile_size, (tile.y_pos+1)*tile_size))


    pygame.draw.line(display_screen, BLACK, (active_map.active_tile_x*tile_size,active_map.active_tile_y*tile_size), ((active_map.active_tile_x+1)*tile_size,active_map.active_tile_y*tile_size))
    pygame.draw.line(display_screen, BLACK, (active_map.active_tile_x*tile_size,(active_map.active_tile_y+1)*tile_size), ((active_map.active_tile_x+1)*tile_size,(active_map.active_tile_y+1)*tile_size))

    pygame.draw.line(display_screen, BLACK, (active_map.active_tile_x*tile_size,active_map.active_tile_y*tile_size), (active_map.active_tile_x*tile_size,(active_map.active_tile_y+1)*tile_size))
    pygame.draw.line(display_screen, BLACK, ((active_map.active_tile_x+1)*tile_size,active_map.active_tile_y*tile_size), ((active_map.active_tile_x+1)*tile_size,(active_map.active_tile_y+1)*tile_size))

    pygame.display.update()
