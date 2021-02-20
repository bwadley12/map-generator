import pygame, sys, math
import map

tile_size = 80
rows = 8
columns = 8

screen_height = tile_size*rows
screen_width = tile_size*columns

pygame.init()

display_screen = pygame.display.set_mode((tile_size*columns,tile_size*rows + 50))

map = map.Map(rows, columns, tile_size)

button = pygame.Surface((100,30))
button.fill((255,255,255))
button_rect = button.get_rect(x=300, y = screen_height+10)


while True:
    display_screen.blit(button, button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if(pygame.key.get_pressed()[pygame.K_UP]):
                map.tile_list[map.active_tile_x][map.active_tile_y].change_state(1)
            elif(pygame.key.get_pressed()[pygame.K_DOWN]):
                map.tile_list[map.active_tile_x][map.active_tile_y].change_state(-1)
            elif(pygame.key.get_pressed()[pygame.K_d]):
                map.increment_active_tile(1,0)
            elif(pygame.key.get_pressed()[pygame.K_a]):
                map.increment_active_tile(-1,0)
            elif(pygame.key.get_pressed()[pygame.K_w]):
                map.increment_active_tile(0,-1)
            elif(pygame.key.get_pressed()[pygame.K_s]):
                map.increment_active_tile(0,1)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

            x_grid = math.floor(x/tile_size)
            y_grid = math.floor(y/tile_size)

            map.set_active_tile(x_grid, y_grid)

    for y_pos in range(rows):
        for x_pos in range(columns):
            display_screen.blit(map.tile_list[x_pos][y_pos].image, map.tile_list[x_pos][y_pos].rect)

    for x_pos in range(columns):
        pygame.draw.line(display_screen, (255,255,255), (x_pos*tile_size,0), (x_pos*tile_size, screen_height))

    for y_pos in range(rows):
        pygame.draw.line(display_screen, (255,255,255), (0,tile_size*y_pos), (screen_width, tile_size*y_pos))

    pygame.draw.line(display_screen, (0,0,0), (map.active_tile_x*tile_size,map.active_tile_y*tile_size), ((map.active_tile_x+1)*tile_size,map.active_tile_y*tile_size))
    pygame.draw.line(display_screen, (0,0,0), (map.active_tile_x*tile_size,(map.active_tile_y+1)*tile_size), ((map.active_tile_x+1)*tile_size,(map.active_tile_y+1)*tile_size))

    pygame.draw.line(display_screen, (0,0,0), (map.active_tile_x*tile_size,map.active_tile_y*tile_size), (map.active_tile_x*tile_size,(map.active_tile_y+1)*tile_size))
    pygame.draw.line(display_screen, (0,0,0), ((map.active_tile_x+1)*tile_size,map.active_tile_y*tile_size), ((map.active_tile_x+1)*tile_size,(map.active_tile_y+1)*tile_size))

    pygame.display.update()
