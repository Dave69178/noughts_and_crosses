# Noughts and Crosses GUI

import PySimpleGUI as sg
import math
import random

sg.theme('BluePurple')

board_layout = [[sg.Button("-", key=(i,j),disabled=True) for i in range(0,3)] for j in range(0,3)]

layout = [[sg.Radio("1 Player", "RADIO1", key="-ONE_PLAYER-", enable_events=True), sg.Radio("2 Player", "RADIO1", key="-TWO_PLAYER-", enable_events=True), sg.Drop(["Noughts","Crosses"],default_value="X or O?",visible=False,enable_events=True,key="-DROP-")],
          [sg.Frame('',board_layout)],
          [sg.Button('Reset',key="-RESET-"), sg.Button('Change Settings',key="-SETTINGS-"), sg.Button('Exit')]]

window = sg.Window('Noughts and Crosses', layout)



# Define board as list

board = ["","","","","","","","",""]

# Define turn count to determine which players move it is

turn_count = 0

# Return array representing current board position

def get_board():
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            t = window[(j,i)].get_text()
            board[count] = 1 if t == "O" else (2 if t == "X" else 0)
            count += 1
    return board

# Update board

def update_button(player,event):
    if player == 1:
        window[event].update("O",disabled=True)
    else:
        window[event].update("X",disabled=True)

# Determine if the game has ended and the result

#Check win(board,player who has turn)

def check_win(b,p):
    return((b[0] == p and b[1] == p and b[2] == p) or
            (b[3] == p and b[4] == p and b[5] == p) or
            (b[6] == p and b[7] == p and b[8] == p) or
            (b[0] == p and b[3] == p and b[6] == p) or
            (b[1] == p and b[4] == p and b[7] == p) or
            (b[2] == p and b[5] == p and b[8] == p) or
            (b[0] == p and b[4] == p and b[8] == p) or
            (b[2] == p and b[4] == p and b[6] == p))

#check draw (true if draw):

def check_draw(b):
    return [elem != 0 for elem in b] == [True for elem in b] and not (check_win(b,1)) and not (check_win(b,2))

# End game

def check_end(b,p):
    if check_win(b,p) == True:
        return "W"
    if check_draw(b) == True:
        return "D"

# Reset environment 

def reset():
    global turn_count
    turn_count = 0
    for i in range(0,3):
        for j in range(0,3):
            window[(i,j)].update("-",disabled=False)


# Change game settings


def settings():
    global turn_count
    turn_count = 0
    for i in range(0,3):
        for j in range(0,3):
            window[(i,j)].update("-",disabled=True)
    window["-ONE_PLAYER-"].update(False,disabled=False)
    window["-TWO_PLAYER-"].update(False,disabled=False)
    window["-DROP-"].update(visible=False,disabled=False)
    



# Functions for AI

# Function to find available moves

def available_moves(b):
    available = []
    index = 0
    for elem in b:
        if elem == 0:
            available.append(index)
        index += 1
    return available

# Function to find best move to make (board, is computer noughts or crosses, player noughts/crosses):

def best_move(b,c,p):
    outcomes = []
    win = []
    draw = []
    loss = []
    available = available_moves(b)
    for elem in available:
        new_b = b.copy()
        new_b[elem] = c
        outcomes.append(minimax(new_b,False,c,p))
    for i in range(0,len(available)):
        if outcomes[i] > 0:
            win.append(available[i])
        elif outcomes[i] == 0:
            draw.append(available[i])
        else:
            loss.append(available[i])
    if win != []:
        return random.choice(win)
    elif draw != []:
        return random.choice(draw)
    else:
        return random.choice(loss)

# Minimax function (max_player = True if it is AI's turn)

def minimax(b,max_player,c,p):
    if game_outcome(b,c,p) != "Not finished":
        return game_outcome(b,c,p)
    if max_player:
        value = -math.inf
        for elem in available_moves(b):
            new_b = b.copy()
            new_b[elem] = c
            value = max(value,minimax(new_b,False,c,p))
        return value
    else:
        value = math.inf
        for elem in available_moves(b):
            new_b = b.copy()
            new_b[elem] = p
            value = min(value,minimax(new_b,True,c,p))
        return value

# Return outcome of game, to be used in best_move
# Return 1 if AI (player 2 wins), 0 if draw, -1 if player 1 wins.

def game_outcome(b,c,p):
    if check_draw(b):
        return 0
    elif check_win(b,p):
        return -1
    elif check_win(b,c):
        return 1
    else:
        return "Not finished"

# Function to convert AI move (represented as a number from 0 to 8) to corresponding event (i,j)

def convert_move(move):
    if move == 0:
        return (0,0)
    elif move == 1:
        return (1,0)
    elif move == 2:
        return (2,0)
    elif move == 3:
        return (0,1)
    elif move == 4:
        return (1,1)
    elif move == 5:
        return (2,1)
    elif move == 6:
        return (0,2)
    elif move == 7:
        return (1,2)
    elif move == 8:
        return (2,2)


while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == "-RESET-":
        reset()
        if values["-DROP-"] == "Crosses":
            player = 2
            comp = 1
            comp_move = random.randint(0,8)
            cmove_ij = convert_move(comp_move)
            update_button(comp,cmove_ij)
            for i in range(0,3):
                for j in range(0,3):
                    if (i,j) == cmove_ij:
                        continue
                    window[(i,j)].update(disabled=False)
        continue
    
    if event == "-SETTINGS-":
        settings()
        continue
    
    if event == "-TWO_PLAYER-":
        window["-ONE_PLAYER-"].update(disabled=True)
        window["-TWO_PLAYER-"].update(disabled=True)
        for i in range(0,3):
            for j in range(0,3):
                window[(i,j)].update(disabled=False)

    if event == "-ONE_PLAYER-":
        window["-TWO_PLAYER-"].update(disabled=True)
        window["-ONE_PLAYER-"].update(disabled=True)
        window["-DROP-"].update(visible=True)

    if event == "-DROP-":
        window["-DROP-"].update(disabled=True)
        
    if event in [(i,j) for i in range(0,3) for j in range(0,3)] and values["-TWO_PLAYER-"] == True:
        turn_count += 1
        player = 1 if turn_count % 2 == 1 else 2
        update_button(player, event)
        board = get_board()
        print(board)
        result = check_end(board,player)
        if result not in ("W","D"):
            continue
        else:
            for b in [(i,j) for i in range(0,3) for j in range(0,3)]:
                window[b].update(disabled=True)
            if result == "W":
                sg.popup_ok(f"Player {player} wins!")
            else:
                sg.popup_ok(f"It's a draw.")


    if (event == "-DROP-") and (values["-DROP-"] == "Noughts"):
        player = 1
        comp = 2
        for i in range(0,3):
            for j in range(0,3):
                window[(i,j)].update(disabled=False)

    if (event == "-DROP-") and (values["-DROP-"] == "Crosses"):
        player = 2
        comp = 1
        comp_move = random.randint(0,8)
        cmove_ij = convert_move(comp_move)
        update_button(comp,cmove_ij)
        for i in range(0,3):
            for j in range(0,3):
                if (i,j) == cmove_ij:
                    continue
                window[(i,j)].update(disabled=False)

    if event in [(i,j) for i in range(0,3) for j in range(0,3)] and values["-ONE_PLAYER-"] == True:
        for i in range(0,3):
            for j in range(0,3):
                window[(i,j)].update(disabled=True)
        update_button(player,event)
        board = get_board()
        result = check_end(board,player)
        if result not in ("W","D"):
            board = get_board()
            print(board)
            comp_move = best_move(board,comp,player)
            print(comp_move)
            update_button(comp,convert_move(comp_move))
            board = get_board()
            result = check_end(board,comp)
            available = available_moves(board)
            available = [convert_move(available[i]) for i in range(0,len(available))]    
            if result not in ("W","D"):
                for i in available:
                    window[i].update(disabled=False)
                continue
            else:
                if result == "W":
                    sg.popup_ok(f"You lose.")
                else:
                    sg.popup_ok(f"It's a draw.")
        else:
            if result == "W":
                sg.popup_ok(f"You win!")
            else:
                sg.popup_ok(f"It's a draw.")    

window.close()
