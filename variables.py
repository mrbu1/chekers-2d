
white_turn = True

from graphics_2d.choice import choose_mode
is2dmode = choose_mode()


if is2dmode:
    import pygame
    from graphics_2d.interface_2d_pygame import scale
    black = pygame.image.load("images/black.png")
    black = pygame.transform.smoothscale(black, (scale*95, scale*95))
    white = pygame.image.load("images/white.png")
    white = pygame.transform.smoothscale(white, (scale*95, scale*95))
    damka_black = pygame.image.load("images/damka black.png")
    damka_black = pygame.transform.smoothscale(damka_black, (scale*95, scale*95))
    damka_white = pygame.image.load("images/damka white.png")
    damka_white = pygame.transform.smoothscale(damka_white, (scale*95, scale*95))
    pos_arr = [black, white, None, damka_black, damka_white]
else:
    pos_arr = ["(---)", "(@@@)", "     ", "<--->", "<@@@>"]


pos_dict = {'A2': pos_arr[0], 'A4': pos_arr[0], 'A6': pos_arr[0], 'A8': pos_arr[0],
            'B1': pos_arr[0], 'B3': pos_arr[0], 'B5': pos_arr[0], 'B7': pos_arr[0],
            'C2': pos_arr[0], 'C4': pos_arr[0], 'C6': pos_arr[0], 'C8': pos_arr[0],
            'D1': pos_arr[2], 'D3': pos_arr[2], 'D5': pos_arr[2], 'D7': pos_arr[2],
            'E2': pos_arr[2], 'E4': pos_arr[2], 'E6': pos_arr[2], 'E8': pos_arr[2],
            'F1': pos_arr[1], 'F3': pos_arr[1], 'F5': pos_arr[1], 'F7': pos_arr[1],
            'G2': pos_arr[1], 'G4': pos_arr[1], 'G6': pos_arr[1], 'G8': pos_arr[1],
            'H1': pos_arr[1], 'H3': pos_arr[1], 'H5': pos_arr[1], 'H7': pos_arr[1]}