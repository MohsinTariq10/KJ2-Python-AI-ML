def check_if_already_filled(inp, locations):
    if(locations[inp] is "X" or locations[inp] is "O"):
        return True
    return False

def check_win(l):
    if ((l[2] is "X" and l[4] is "X" and l[6] is "X") or 
        (l[2] is "O" and l[4] is "O" and l[6] is "O") or
        (l[0] is "X" and l[4] is "X" and l[8] is "X") or
        (l[0] is "O" and l[4] is "O" and l[8] is "O") or
        (l[0] is "X" and l[1] is "X" and l[2] is "X") or
        (l[0] is "O" and l[1] is "O" and l[2] is "O") or
        (l[3] is "X" and l[4] is "X" and l[5] is "X") or
        (l[3] is "O" and l[4] is "O" and l[5] is "O") or
        (l[6] is "X" and l[7] is "X" and l[8] is "X") or
        (l[6] is "O" and l[7] is "O" and l[8] is "O") or
        (l[0] is "X" and l[3] is "X" and l[6] is "X") or
        (l[0] is "O" and l[3] is "O" and l[6] is "O") or
        (l[1] is "X" and l[4] is "X" and l[7] is "X") or
        (l[1] is "O" and l[4] is "O" and l[7] is "O") or
        (l[2] is "X" and l[5] is "X" and l[8] is "X") or
        (l[2] is "O" and l[5] is "O" and l[8] is "O")
        ):
        return True
    return False

def check_draw(l):
    for loc in l:
        if(loc is "-"):
            return False
    return True
def print_board(l):
    print("{} | {} | {}".format(l[0], l[1], l[2]))
    print("_____________")
    print("{} | {} | {}".format(l[3], l[4], l[5]))
    print("_____________")
    print("{} | {} | {}".format(l[6], l[7], l[8]))
    
    
locations = ["-", "-", "-","-", "-", "-","-", "-", "-"]
take=True # True is player 1 and False Player 2
win_or_draw = ""
while(True):
    print_board(locations)
    input_string = "Enter for Player 1 : "
    if(take is False):
        input_string = "Enter for Player 2 : "
    inp = int(input(input_string))
    if check_if_already_filled(inp, locations):
        continue
    if(take is True):
        locations[inp] = "X"
    else:
        locations[inp] = "O"
    if check_win(locations):
        win_or_draw = "win"
        break
    if check_draw(locations):
        win_or_draw = "draw"
        break
    take = not take
    
if(win_or_draw is "win"):
    if(take is True):
        print("Hurrah!!Player 1 is the Winner!")
    else:
        print("Hurrah!!Player 2 is the Winner!")
else:
    print ("Sorry!! Game Drawn")
        
        
        
        
        
        
        
    