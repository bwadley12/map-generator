import pygame, sys, math
import map, preferences

default_screen_height = 750
default_screen_width = 1000
menu_width = 200 # screen width does not include menu_width
menu_padding = 15 
standard_button_height = 40

rows = 50
columns = 50

tile_size_x = math.floor(default_screen_width/columns)
tile_size_y = math.floor(default_screen_height/rows)
tile_size = min(tile_size_x, tile_size_y)

game_board_x = columns*tile_size
screen_height = rows*tile_size + 1

screen_width = game_board_x + menu_width

pygame.init()

display_screen = pygame.display.set_mode((screen_width, screen_height))
map = map.Map(rows, columns, tile_size)
preferences = preferences.Preferences()

WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
LIGHT_GRAY = pygame.Color(200,200,200)

font = pygame.font.SysFont("Calibri", 20)
font_small = pygame.font.SysFont("Calibri", 15)

button = pygame.Rect(game_board_x, screen_height - standard_button_height, menu_width, standard_button_height)
print_display = font.render("Print", True, BLACK)

preferences_display = font.render("Preferences", True, BLACK)
grid_x_toggle = pygame.Rect(game_board_x + menu_padding, 35, 15, 15)
grid_x_toggled_on_rect = pygame.Rect(game_board_x + menu_padding + 4, 39, 7, 7)
grid_x_label = font_small.render("Enable/Disable X grid",True, BLACK)

grid_y_toggle = pygame.Rect(game_board_x + menu_padding, 60, 15, 15)
grid_y_toggled_on_rect = pygame.Rect(game_board_x + menu_padding + 4, 64, 7, 7)
grid_y_label = font_small.render("Enable/Disable Y grid",True, BLACK)

while True:
    display_screen.fill(WHITE)

    # building menu
    pygame.draw.rect(display_screen, LIGHT_GRAY, button)
    display_screen.blit(print_display, (button.centerx - print_display.get_width()/2, button.centery - print_display.get_height()/2))

    display_screen.blit(preferences_display, (game_board_x + menu_width/2 - preferences_display.get_width()/2, 10))
    pygame.draw.rect(display_screen, BLACK, grid_x_toggle)
    if preferences.get_x_grid_enabled():
        pygame.draw.rect(display_screen, LIGHT_GRAY, grid_x_toggled_on_rect)
    
    pygame.draw.rect(display_screen, BLACK, grid_y_toggle)
    if preferences.get_y_grid_enabled():
        pygame.draw.rect(display_screen, LIGHT_GRAY, grid_y_toggled_on_rect)

    display_screen.blit(grid_x_label, (grid_x_toggle.right + 10, grid_x_toggle.top))
    display_screen.blit(grid_y_label, (grid_y_toggle.right + 10, grid_y_toggle.top))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if(pygame.key.get_pressed()[pygame.K_w]):
                map.tile_list[map.active_tile_x][map.active_tile_y].change_state(1)
            elif(pygame.key.get_pressed()[pygame.K_s]):
                map.tile_list[map.active_tile_x][map.active_tile_y].change_state(-1)
            elif(pygame.key.get_pressed()[pygame.K_RIGHT]):
                map.increment_active_tile(1,0)
            elif(pygame.key.get_pressed()[pygame.K_LEFT]):
                map.increment_active_tile(-1,0)
            elif(pygame.key.get_pressed()[pygame.K_UP]):
                map.increment_active_tile(0,-1)
            elif(pygame.key.get_pressed()[pygame.K_DOWN]):
                map.increment_active_tile(0,1)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                print(map.get_tile_states())
            elif grid_x_toggle.collidepoint(event.pos):
                preferences.toggle_x_grid_enabled()
            elif grid_y_toggle.collidepoint(event.pos):
                preferences.toggle_y_grid_enabled()
            else:
                x,y = pygame.mouse.get_pos()
                x_grid = math.floor(x/tile_size)
                y_grid = math.floor(y/tile_size)
                map.set_active_tile(x_grid, y_grid)

    for y_pos in range(rows):
        for x_pos in range(columns):
            display_screen.blit(map.tile_list[x_pos][y_pos].image, map.tile_list[x_pos][y_pos].rect)

    if preferences.get_y_grid_enabled():
        for x_pos in range(columns+1):
            pygame.draw.line(display_screen, WHITE, (x_pos*tile_size,0), (x_pos*tile_size, screen_height))

    if preferences.get_x_grid_enabled():
        for y_pos in range(rows+1):
            pygame.draw.line(display_screen, WHITE, (0,tile_size*y_pos), (game_board_x, tile_size*y_pos))

    pygame.draw.line(display_screen, BLACK, (map.active_tile_x*tile_size,map.active_tile_y*tile_size), ((map.active_tile_x+1)*tile_size,map.active_tile_y*tile_size))
    pygame.draw.line(display_screen, BLACK, (map.active_tile_x*tile_size,(map.active_tile_y+1)*tile_size), ((map.active_tile_x+1)*tile_size,(map.active_tile_y+1)*tile_size))

    pygame.draw.line(display_screen, BLACK, (map.active_tile_x*tile_size,map.active_tile_y*tile_size), (map.active_tile_x*tile_size,(map.active_tile_y+1)*tile_size))
    pygame.draw.line(display_screen, BLACK, ((map.active_tile_x+1)*tile_size,map.active_tile_y*tile_size), ((map.active_tile_x+1)*tile_size,(map.active_tile_y+1)*tile_size))

    pygame.display.update()
