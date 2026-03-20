import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
scr_res = (pygame.display.Info().current_w, pygame.display.Info().current_h) #screen setings pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(scr_res)
pygame.display.set_caption("Checkers 2D")
Wmax, Hmax = screen.get_size()
fldWmax = 1000
fldHmax = 1000
scale = min(Wmax / fldWmax, Hmax / fldHmax)
size = 100*scale

center_x, center_y = screen.get_rect().center
def positions(scale):
    CELL_TOP_LEFT = { 
        "A1": (center_x + (-400)*scale, center_y + (-400)*scale), "B1": (center_x + (-400)*scale, center_y + (-300)*scale), "C1": (center_x + (-400)*scale, center_y + (-200)*scale), "D1": (center_x + (-400)*scale, center_y + (-100)*scale), "E1": (center_x + (-400)*scale, center_y + (0)*scale), "F1": (center_x + (-400)*scale, center_y + (100)*scale), "G1": (center_x + (-400)*scale, center_y + (200)*scale), "H1": (center_x + (-400)*scale, center_y + (300)*scale),
        "A2": (center_x + (-300)*scale, center_y + (-400)*scale), "B2": (center_x + (-300)*scale, center_y + (-300)*scale), "C2": (center_x + (-300)*scale, center_y + (-200)*scale), "D2": (center_x + (-300)*scale, center_y + (-100)*scale), "E2": (center_x + (-300)*scale, center_y + (0)*scale), "F2": (center_x + (-300)*scale, center_y + (100)*scale), "G2": (center_x + (-300)*scale, center_y + (200)*scale), "H2": (center_x + (-300)*scale, center_y + (300)*scale),
        "A3": (center_x + (-200)*scale, center_y + (-400)*scale), "B3": (center_x + (-200)*scale, center_y + (-300)*scale), "C3": (center_x + (-200)*scale, center_y + (-200)*scale), "D3": (center_x + (-200)*scale, center_y + (-100)*scale), "E3": (center_x + (-200)*scale, center_y + (0)*scale), "F3": (center_x + (-200)*scale, center_y + (100)*scale), "G3": (center_x + (-200)*scale, center_y + (200)*scale), "H3": (center_x + (-200)*scale, center_y + (300)*scale),
        "A4": (center_x + (-100)*scale, center_y + (-400)*scale), "B4": (center_x + (-100)*scale, center_y + (-300)*scale), "C4": (center_x + (-100)*scale, center_y + (-200)*scale), "D4": (center_x + (-100)*scale, center_y + (-100)*scale), "E4": (center_x + (-100)*scale, center_y + (0)*scale), "F4": (center_x + (-100)*scale, center_y + (100)*scale), "G4": (center_x + (-100)*scale, center_y + (200)*scale), "H4": (center_x + (-100)*scale, center_y + (300)*scale),
        "A5": (center_x + (0)*scale, center_y + (-400)*scale), "B5": (center_x + (0)*scale, center_y + (-300)*scale), "C5": (center_x + (0)*scale, center_y + (-200)*scale), "D5": (center_x + (0)*scale, center_y + (-100)*scale), "E5": (center_x + (0)*scale, center_y + (0)*scale), "F5": (center_x + (0)*scale, center_y + (100)*scale), "G5": (center_x + (0)*scale, center_y + (200)*scale), "H5": (center_x + (0)*scale, center_y + (300)*scale),
        "A6": (center_x + (100)*scale, center_y + (-400)*scale), "B6": (center_x + (100)*scale, center_y + (-300)*scale), "C6": (center_x + (100)*scale, center_y + (-200)*scale), "D6": (center_x + (100)*scale, center_y + (-100)*scale), "E6": (center_x + (100)*scale, center_y + (0)*scale), "F6": (center_x + (100)*scale, center_y + (100)*scale), "G6": (center_x + (100)*scale, center_y + (200)*scale), "H6": (center_x + (100)*scale, center_y + (300)*scale),
        "A7": (center_x + (200)*scale, center_y + (-400)*scale), "B7": (center_x + (200)*scale, center_y + (-300)*scale), "C7": (center_x + (200)*scale, center_y + (-200)*scale), "D7": (center_x + (200)*scale, center_y + (-100)*scale), "E7": (center_x + (200)*scale, center_y + (0)*scale), "F7": (center_x + (200)*scale, center_y + (100)*scale), "G7": (center_x + (200)*scale, center_y + (200)*scale), "H7": (center_x + (200)*scale, center_y + (300)*scale),
        "A8": (center_x + (300)*scale, center_y + (-400)*scale), "B8": (center_x + (300)*scale, center_y + (-300)*scale), "C8": (center_x + (300)*scale, center_y + (-200)*scale), "D8": (center_x + (300)*scale, center_y + (-100)*scale), "E8": (center_x + (300)*scale, center_y + (0)*scale), "F8": (center_x + (300)*scale, center_y + (100)*scale), "G8": (center_x + (300)*scale, center_y + (200)*scale), "H8": (center_x + (300)*scale, center_y + (300)*scale),
    }
    return CELL_TOP_LEFT   


def check_which(size, CELL_TOP_LEFT, pos: tuple[int, int], ):
    mx, my = pos
    fx, fy = CELL_TOP_LEFT.get("A1")
    if fx < mx < fx + size*8 and fy < my < fy + size*8: 
        letter = chr(int((my-fy)/(size))+65)
        number = int((mx-fx)/(size))+1
        return letter+str(number)



def tiles_painting(size, CELL_TOP_LEFT, screen):
    white = True
    for place in CELL_TOP_LEFT.keys():
        x, y = CELL_TOP_LEFT.get(place)
        if white:
            pygame.draw.rect(screen, (254, 250, 245), (x, y, size, size))
        else: 
            pygame.draw.rect(screen, (40, 3, 1), (x, y, size, size))
        
        if place[0] != "H":
            white = not white




def tile_light(size, CELL_TOP_LEFT, screen):
    tile = check_which(size, CELL_TOP_LEFT, pygame.mouse.get_pos())
    if tile != None:
        x, y = CELL_TOP_LEFT.get(tile)
        color = screen.get_at((int(x+size/2), int(y+size/2)))[:3]
        if color == (254, 250, 245):
            color = tuple(int(c*0.7) for c in color)
        else:
            color = tuple(max(0, min(255, int(c * 1.6))) for c in color)

        pygame.draw.rect(screen, (color), (x, y, size, size))


def pyprint(size, screen, text, font, x, y, is_right):
    oset_x = font.size(text)[0]/2

    try:
        text = int(text)
    except ValueError:
        text = text
    

    if type(text) == int:
        x = x - oset_x
        if is_right:
            x = x + size /2
            y = y - size /1.3
            
        else:
            x = x + size /2
            y = y + size
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            screen.blit(font.render(str(text), True, (255, 255, 255)), (x+dx, y+dy))
        screen.blit(font.render(str(text), True, (0, 0, 0)), (x, y))

    else:
        y = y + size*0.1
        if is_right:
            x = x + size*1.2
        else:
            x = x - size*0.6
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            screen.blit(font.render(text, True, (0, 0, 0)), (x+dx, y+dy))
        screen.blit(font.render(text, True, (255, 255, 255)), (x, y))
    
def turn(white_turn, screen):
    if white_turn:
        screen.fill((255, 253, 208))
    else:
        screen.fill((50, 50, 50))


        

def interface():
    clock = pygame.time.Clock() #FPS setting
    FPS = 60

    import variables
    from main_logic import move_2d

    pygame.init()


    CELL_TOP_LEFT = positions(scale)

    font = pygame.font.SysFont("arial", int(70*scale))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 or event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                tile = check_which(size, CELL_TOP_LEFT, event.pos)
                move_2d(tile)
                

        turn(variables.white_turn, screen)
        tiles_painting(size, CELL_TOP_LEFT, screen)
        tile_light(size, CELL_TOP_LEFT, screen)
        
        for position in CELL_TOP_LEFT.keys():
            if variables.pos_dict.get(position) != None:
                screen.blit(variables.pos_dict.get(position), (CELL_TOP_LEFT.get(position)[0]+size*0.025, CELL_TOP_LEFT.get(position)[1]+size*0.025))
            offset_x, offset_y = CELL_TOP_LEFT.get(position)[0], CELL_TOP_LEFT.get(position)[1]
            if position[0] == "A":
                pyprint(size, screen, position[1], font, offset_x, offset_y, True)
            elif position[0] == "H":
                pyprint(size, screen, position[1], font, offset_x, offset_y, False)
            if position[1] == "1":
                pyprint(size, screen, position[0], font, offset_x, offset_y, False)
            elif position[1] == "8":
                pyprint(size, screen, position[0], font, offset_x, offset_y, True)

            
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit() 
    sys.exit()