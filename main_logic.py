import variables
from variables import pos_arr, is2dmode
if is2dmode:
    import graphics_2d.interface_2d_pygame
else:
    import terminal_interface



def malka(to, from1):
    if str(to[0]) == "A" and variables.pos_dict[from1] == pos_arr[1]:
        variables.pos_dict[to] = pos_arr[4]
    elif str(to[0]) == "H" and variables.pos_dict[from1] == pos_arr[0]:
        variables.pos_dict[to] = pos_arr[3]
    if not variables.pos_dict[to] == pos_arr[3] and not variables.pos_dict[to] == pos_arr[4]:
        if not variables.pos_dict[from1] == pos_arr[3] and not variables.pos_dict[from1] == pos_arr[4]:
            return False
    return True


def eat(from1, to, white_turn):
    pet_dist = ord(to[0]) - ord(from1[0])
    dumb_dist = int(to[1]) - int(from1[1])
    if not malka(to, from1):
        if pet_dist == -2 and white_turn:
            eat_let_dist = chr(ord(from1[0]) - 1)
        elif pet_dist == 2 and not white_turn:
            eat_let_dist = chr(ord(from1[0]) + 1)
        else:
            return False
        if not dumb_dist == -2:
            if not dumb_dist == 2:
                return False
            else:
                eat_numb_dist = int(from1[1]) + 1
        else:
            eat_numb_dist = int(from1[1]) - 1
        eatt = eat_let_dist + str(eat_numb_dist)
        if white_turn and variables.pos_dict[eatt] == pos_arr[0] or variables.pos_dict[eatt] == pos_arr[3]:
            variables.pos_dict[eatt] = pos_arr[2]
            return True
        if not white_turn and variables.pos_dict[eatt] == pos_arr[1] or variables.pos_dict[eatt] == pos_arr[4]:
            variables.pos_dict[eatt] = pos_arr[2]
            return True

    else:
        if pet_dist <= -2:
            eat_let_dist = chr(ord(to[0]) + 1)
        elif pet_dist >= 2:
            eat_let_dist = chr(ord(to[0]) - 1)
        else:
            return False
        if not dumb_dist <= -2:
            if not dumb_dist >= 2:
                return False
            else:
                eat_numb_dist = int(to[1]) - 1
        else:
            eat_numb_dist = int(to[1]) + 1
        eatt = eat_let_dist + str(eat_numb_dist)
        if variables.pos_dict[eatt] == pos_arr[0] and white_turn:
            if pet_dist == dumb_dist or pet_dist == -dumb_dist:
                variables.pos_dict[eatt] = pos_arr[2]
                return True
        if variables.pos_dict[eatt] == pos_arr[1] and not white_turn:
            if pet_dist == dumb_dist or pet_dist == -dumb_dist:
                variables.pos_dict[eatt] = pos_arr[2]
                return True


def rules(from1, to, white_turn):
    if not eat(from1, to, variables.white_turn):
        let_dist = ord(to[0]) - ord(from1[0])
        numb_dist = int(to[1]) - int(from1[1])
        if not malka(to, from1):
            if not numb_dist == -1:
                if not numb_dist == 1:
                    print("You can't do it")
                    return False
            if not let_dist == -1 and white_turn:
                print("You can't do it")
                return False
            if not let_dist == 1 and not white_turn:
                print("You can't do it")
                return False
            return True
        if not let_dist == numb_dist and not let_dist == -numb_dist:
            print("You can't do it")
            return False
    return True




def check(from1, to):
    if variables.pos_dict[from1] == pos_arr[2]:
        print("You haven't cheker there!")
        return False
    if not variables.pos_dict[to] == pos_arr[2]:
        print("You already have cheker there!")
        return False
    return True


def place(from1, to):
    if variables.white_turn and not variables.pos_dict[from1] == pos_arr[1] and not variables.pos_dict[from1] == pos_arr[4]:
        print("It is white turn, not black!")
        return False
    if not variables.white_turn and not variables.pos_dict[from1] == pos_arr[0] and not variables.pos_dict[from1] == pos_arr[3]:
        print("It is black turn, not white!")
        return False
    return True


def cheker(from1, to, white_turn):
    if check(from1, to) and place(from1, to) and rules(from1, to, white_turn):
        return True
    else:
        return False


def whitewin():
    for i in range(65, 73):
        letter = chr(i)
        for i in range(2, 9, 2):
            if ord(letter) % 2 == 0:
                second = i - 1
            else:
                second = i
            seclet = letter + str(second)
            if variables.pos_dict[seclet] == pos_arr[0] or variables.pos_dict[seclet] == pos_arr[3]:
                return False
    print("Congratulations! The white player won!")
    return True


def blackwin():
    for i in range(65, 73):
        letter = chr(i)
        for i in range(2, 9, 2):
            if ord(letter) % 2 == 0:
                second = i - 1
            else:
                second = i
            seclet = letter + str(second)
            if variables.pos_dict[seclet] == pos_arr[1] or variables.pos_dict[seclet] == pos_arr[4]:
                return False
    print("Congratulations! The black player won!")
    return True


def turn(white_turn):
    if white_turn:
        print("It is white turn")
    else:
        print("It is black turn")


def move():
    from1 = input("From where? ")
    oldfrom = from1
    from1 = from1.upper()
    if not from1 in variables.pos_dict:
        print("I don't know what is '", oldfrom, "'")
        return False
    to = input("To there? ")
    oldto = to
    to = to.upper()
    if not to in variables.pos_dict:
        print("I don't know what is '", oldto, "'")
        return False
    variables.white_turn
    if cheker(from1, to, variables.white_turn):
        variables.pos_dict[to] = variables.pos_dict[from1]
        malka(to, from1)
        variables.pos_dict[from1] = pos_arr[2]
        variables.white_turn = not variables.white_turn
        return True

is_from = True
from1 = None
to = None
def move_2d(tile):
    global is_from, from1, to, white_turn
    if is_from:
        if variables.pos_dict.get(tile) == pos_arr[1] and variables.white_turn or variables.pos_dict.get(tile) == pos_arr[4] and variables.white_turn or variables.pos_dict.get(tile) == pos_arr[0] and not variables.white_turn or variables.pos_dict.get(tile) == pos_arr[3] and not variables.white_turn:
            from1 = tile
            if not from1 in variables.pos_dict:
                print("I don't know what is '"+from1+"'")
                return False
            to = None
            is_from = False
    else:
        to = tile
        if not to in variables.pos_dict:
            print("I don't know what is '" + to + "'")
            return False
        is_from = True
    if from1 != None and to != None:
        if cheker(from1, to, variables.white_turn):
            variables.pos_dict[to] = variables.pos_dict[from1]
            malka(to, from1)
            variables.pos_dict[from1] = pos_arr[2]
            variables.white_turn = not variables.white_turn
            return True


if not is2dmode:
    while True:
        turn(variables.white_turn)
        terminal_interface.move_board()
        move()
        if whitewin() or blackwin():
            want = input('You want to play again?(yes/no) ')
            if not want.upper() == 'YES':
                break
            else:
                variables.pos_dict = {'A2': pos_arr[0], 'A4': pos_arr[0], 'A6': pos_arr[0], 'A1': pos_arr[0],
                            'B1': pos_arr[0], 'B3': pos_arr[0], 'B5': pos_arr[0], 'B7': pos_arr[0],
                            'C2': pos_arr[0], 'C4': pos_arr[0], 'C6': pos_arr[0], 'C1': pos_arr[0],
                            'D1': pos_arr[2], 'D3': pos_arr[2], 'D5': pos_arr[2], 'D7': pos_arr[2],
                            'E2': pos_arr[2], 'E4': pos_arr[2], 'E6': pos_arr[2], 'E1': pos_arr[2],
                            'F1': pos_arr[1], 'F3': pos_arr[1], 'F5': pos_arr[1], 'F7': pos_arr[1],
                            'G2': pos_arr[1], 'G4': pos_arr[1], 'G6': pos_arr[1], 'G1': pos_arr[1],
                            'H1': pos_arr[1], 'H3': pos_arr[1], 'H5': pos_arr[1], 'H7': pos_arr[1]}
                terminal_interface.move_board()
                white_turn = True

else:
    graphics_2d.interface_2d_pygame.interface()