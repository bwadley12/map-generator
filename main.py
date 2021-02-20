import pygame, sys, math
import map

default_screen_height = 750
default_screen_width = 1000
menu_width = 200 # screen width does not include menu_width
standard_button_height = 40

rows = 50
columns = 75

tile_size_x = math.floor(default_screen_width/columns)
tile_size_y = math.floor(default_screen_height/rows)
tile_size = min(tile_size_x, tile_size_y)

game_board_x = columns*tile_size
screen_height = rows*tile_size + 1

screen_width = game_board_x + menu_width

pygame.init()

display_screen = pygame.display.set_mode((screen_width, screen_height))

map = map.Map(rows, columns, tile_size)

button = pygame.Rect(game_board_x, screen_height - standard_button_height, menu_width, standard_button_height)
font = pygame.font.SysFont("Verdana", 20)
print_display = font.render("Print",True, (0,0,0))

while True:
    pygame.draw.rect(display_screen, [255, 255, 255], button)
    display_screen.blit(print_display, (button.centerx - print_display.get_width()/2, button.centery - print_display.get_height()/2))

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
            else:
                x,y = pygame.mouse.get_pos()
                x_grid = math.floor(x/tile_size)
                y_grid = math.floor(y/tile_size)
                map.set_active_tile(x_grid, y_grid)

    for y_pos in range(rows):
        for x_pos in range(columns):
            display_screen.blit(map.tile_list[x_pos][y_pos].image, map.tile_list[x_pos][y_pos].rect)

    for x_pos in range(columns+1):
        pygame.draw.line(display_screen, (255,255,255), (x_pos*tile_size,0), (x_pos*tile_size, screen_height))

    for y_pos in range(rows+1):
        pygame.draw.line(display_screen, (255,255,255), (0,tile_size*y_pos), (game_board_x, tile_size*y_pos))

    pygame.draw.line(display_screen, (0,0,0), (map.active_tile_x*tile_size,map.active_tile_y*tile_size), ((map.active_tile_x+1)*tile_size,map.active_tile_y*tile_size))
    pygame.draw.line(display_screen, (0,0,0), (map.active_tile_x*tile_size,(map.active_tile_y+1)*tile_size), ((map.active_tile_x+1)*tile_size,(map.active_tile_y+1)*tile_size))

    pygame.draw.line(display_screen, (0,0,0), (map.active_tile_x*tile_size,map.active_tile_y*tile_size), (map.active_tile_x*tile_size,(map.active_tile_y+1)*tile_size))
    pygame.draw.line(display_screen, (0,0,0), ((map.active_tile_x+1)*tile_size,map.active_tile_y*tile_size), ((map.active_tile_x+1)*tile_size,(map.active_tile_y+1)*tile_size))

    pygame.display.update()
