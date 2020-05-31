#FriendlyFighters.py
#Akib Shamsuddin, Bansari Patel, Samantha Whan
#

from pygame import *
from random import *

def player_bars(screen,player_chosen,players,colours):
    draw.rect(screen,colours[0],(0,750,500,50))
    draw.rect(screen,colours[1],(500,750,500,50))
    if player_chosen == 0:
        draw.rect(screen,ALT_BLUE,(0,750,500,50),2)
    else:
        draw.rect(screen,ALT_BLUE,(500,750,500,50),2)

def player_switch(player_chosen):
    if player_chosen == 1:
        player_chosen = 0
    elif player_chosen == 0:
        player_chosen = 1
    return player_chosen

def turn(screen,players,player_chosen):
    draw.rect(screen,(255,255,255),(0,700,1000,50))
    turn_text = generalFont.render("It's the " + players[player_chosen] + " player's turn!", True, colours[player_chosen])
    screen.blit(turn_text,(0,700))

def game_change(screen,button,game_type,mb,mx,my,background):
    global win
    global tie
    screen.blit(button,(700,350))
    if mb[0] == 1 and Rect(700,350,300,100).collidepoint((mx,my)):
        game_type = "memory"
        screen.blit(background,(0,0))
        draw.rect(screen,(255,255,255),(0,700,1000,50))
        win = False
        tie = False
    return game_type
#------------------TIC-TAC-TOE-FUNCTIONS------------------
def tic_tac(screen,rects,tic_list,background):
    draw.rect(screen,PURPLE,(350,200,300,300))
    for y in range(3):
        for x in range(3):
            box_rect = rects[y][x]
            draw.rect(screen,ALT_BLUE,(box_rect[X],box_rect[Y],100,100),5)
            if tic_list[y][x] == REDPOS:
                screen.blit(icons[0],(rects[y][x][X], rects[y][x][Y]))
            if tic_list[y][x] == WHITEPOS:
                screen.blit(icons[1],(rects[y][x][X], rects[y][x][Y]))

def select_box(mx,my,rects):
    x_pos,y_pos = "",""
    for row in range(3):
        for box in range(3):
            if rects[row][box].collidepoint((mx,my)):
                x_pos,y_pos = box,row
    return y_pos,x_pos

def icon_blit(screen,tic_list,icons,mx,my,rects,player_chosen):
    cy,cx = select_box(mx,my,rects)
    try:
        if tic_list[cy][cx] == EMPTY:
            tic_list[cy][cx] = player_chosen + 1
            player_chosen = player_switch(player_chosen)
    except:
        return player_chosen,tic_list
    return player_chosen,tic_list

def win_check(screen,tic_list):
    for x in range(3):
        if tic_list[0][x] == tic_list[1][x] == tic_list[2][x] != 0:
            return True,tic_list[0][x]
    for y in range(3):
        if tic_list[y][0] == tic_list[y][1] == tic_list[y][2] != 0:
            return True,tic_list[y][0]
    if tic_list[0][0] == tic_list[1][1] == tic_list[2][2] != 0:
        return True,tic_list[0][0]
    if tic_list[2][0] == tic_list[1][1] == tic_list[0][2] != 0:
        return True,tic_list[1][1]
    return False,tic_list[1][1]

def tie_check(screen,tic_list):
    for y in range(3):
        for x in range(3):
            if tic_list[y][x] == 0:
                return False
    return True

#------------------MEMORY-FUNCTIONS------------------
"""
def card_shuffle(card_contents,card_c,card_types):
    for delete in range(3):
        del card_types[randint(0,len(card_types))]
    for y in range(4):
        for x in range(6):
    
def card_blit(screen,card_rects):
    for y in range(4):
        for x in range(6):
            draw.rect(screen,WHITE,card_rects[y][x])
            draw.rect(screen,ALT_BLUE,card_rects[y][x],2)
"""
turning = 0
points =  [0,0]
def cards(card_contents,card_r):
    for y in range(4):
        for x in range(6):
            rec = Rect(x*85+200,y*125+200,80,120)
            card_r.append(rec)
    return card_r

def check_match(picked, match, card_rects, matched_rec, card_contents,points):
    if len(picked) ==2:

        if picked[0] == picked[1]:
##            points[turning] +=1
            match += 1
            for picker in picked_rec:
                if picker not in matched_rec:
                    matched_rec.append(picker)
                    points[turning] +=.5
    points[0] = int(points[0])
    points[1] = int(points[1])

def organize(card_c,card_contents,card_r, card_rects):
    if len(card_c)>0:
        card_contents.append(list(card_c[:5]))
        del card_c[:5]
##    print(card_contents)
    if len (card_r)>0:
        card_rects.append(list(card_r[:5]))
        del card_r[:5]
    return card_rects

def pick(card_contents,card_rects, clicking, click, picked, picked_rec, matched_rec,match_status):
    mpos = mouse.get_pos()
    mb = mouse.get_pressed()



##    for i in range(4):
##        print(len(card_contents[i]))
    
    
    for layer in card_rects:
        for card in layer:

            pos_1 = card_rects.index(layer)
            pos_2 = layer.index(card)
            card_c = card.copy()
        
            if card.collidepoint(mpos):
                draw.rect(screen,(255,0,0),card,3)
                if clicking == True:
                    pic_pos = card[:2]
                    
                    if click == 1 and len(picked)<1 and card_c not in picked_rec:
                        picked.append(card_contents[pos_1][pos_2])
                        picked_rec.append(card_c)
                        #match_status = True
                        for p in picked:
                            screen.blit(p,(card[0]-4,card[1]+15))
                            print(points)
                            
                    if click == 2 and len(picked)<2 and card_c!= picked_rec[0]:
                        picked.append(card_contents[pos_1][pos_2])
                        picked_rec.append(card_c)
                        match_status = False
##                        for p in picked:
                        screen.blit(picked[1],(card[0]-4,card[1]+15))
                        print(points)
##                        print(p)

            else:
                draw.rect(screen,(255,255,255),card,3)
                
    for matching in matched_rec:
        draw.rect(screen,(0,255,0),matching,3)

    if len(matched_rec) == 24:
        if points[0]>points[1]:
            print("player 1 wins")
        elif points[0]<points[1]:
            print("player 2 wins")
        else:
            print('draw')


screen = display.set_mode((1000, 800))
screen.fill((255,255,255))

background = image.load("background.png")
menu = image.load("menu.png")
button = image.load("button.png")
#------------------TIC-TAC-TOE------------------
init()

BLUE = (125,125,255)
WHITE = (255,255,255)
RED = (255,125,125)

ALT_BLUE = (25,25,50)
PURPLE = (200,125,255)

tic_list = []

EMPTY = 0
REDPOS = 1
WHITEPOS = 2

rects = []
players = ["red", "blue"]
colours = [(255,125,125), (125,125,255)]
player_chosen = 0

icons = [image.load("X.png"), image.load("O.png")]

X = 0
Y = 1

for row in range(3):
    tic_list += [[0,0,0]]

for x in range(350,650,100):
    row = []
    for y in range(200,500,100):
        row.append(Rect(x,y,100,100))
    rects += [row]

#------------------MEMORY------------------
circ_1 = image.load("sprites/circle_blue.png")
circ_2 = image.load("sprites/circle_red.png")
circ_3 = image.load("sprites/circle_green.png")
penta_1 = image.load("sprites/penta_blue.png")
penta_2 = image.load("sprites/penta_red.png")
penta_3 = image.load("sprites/penta_green.png")
rect_1 = image.load("sprites/rect_blue.png")
rect_2 = image.load("sprites/rect_red.png")
rect_3 = image.load("sprites/rect_green.png")
star_1 = image.load("sprites/star_blue.png")
star_2 = image.load("sprites/star_red.png")
star_3 = image.load("sprites/star_green.png")
card_c = [circ_1,circ_2,circ_3,penta_1,penta_2,penta_3, rect_1,rect_2,rect_3,star_1,star_2,star_3,circ_1,circ_2,circ_3,penta_1,penta_2,penta_3, rect_1,rect_2,rect_3,star_1,star_2,star_3]
"""
card_types = [x for x in range(15)]
print(card_types)

card_rects = []
card_contents = []
chosen_cards = []

for y in range(4):
    row = []
    for x in range(6):
        rec = Rect(x*115+150,y*125+100,100,120)
        row.append(rec)
    card_rects += [row]

card_shuffle(card_contents,card_c,chosen_cards)
"""

card_r = []
card_rects = []

match = 0
matched_rec = []

player = [[0],[0]]

card_contents = []

shuffle(card_c)

click = 0
clicking = False
match_status = False

picked = []
picked_rec = []

f,s = 0,0

#----------------------------------

click = False
win = False
tie = False
winner = 0

game_type = "menu"

generalFont = font.Font("ARLRDBD.TTF",26)

screen.blit(background,(0,0))

draw.rect(screen,(255,255,255),(0,700,1000,50))
turn_text = generalFont.render("It's the " + players[player_chosen] + " player's turn!", True, colours[player_chosen])
screen.blit(turn_text,(0,700))

running = True
while running:
    
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

        if evnt.type == MOUSEBUTTONDOWN:
            if game_type == "menu":
                if Rect(40,405,300,100).collidepoint((mx,my)):
                    game_type = "tic tac"
                    screen.blit(background,(0,0))
                elif Rect(40,585,300,100).collidepoint((mx,my)):
                    running = False
            if game_type == "tic tac":
                if win == False:
                    player_chosen,tic_list = icon_blit(screen,tic_list,icons,mx,my,rects,player_chosen)
                    win,winner = win_check(screen,tic_list)
                    tie = tie_check(screen,tic_list)
                    turn(screen,players,player_chosen)
            elif game_type == "memory":
                clicking = True
                click+=1
        else:
            clicking = False
            
        if evnt.type == MOUSEBUTTONUP:
            if win:
                draw.rect(screen,(255,255,255),(0,700,1000,50))
                win_text = generalFont.render("The " + str(players[winner - 1]) + " player is the winner!", True, colours[winner - 1])
                screen.blit(win_text,(0,700))
            elif tie:
                draw.rect(screen,(255,255,255),(0,700,1000,50))
                win_text = generalFont.render("The game was a tie!", True, PURPLE)
                screen.blit(win_text,(0,700))
                
            if click > 1:
                
                click *= 0
                picked *= 0
                picked_rec *= 0
                if turn == 0:
                    turn = 1
                if turn == 1:
                    turn == 0
                    
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    
    if game_type == "menu":
        screen.blit(menu,(0,0))
        
    if game_type == "tic tac":
        tic_tac(screen,rects,tic_list,background)
        if win or tie:
            game_type = game_change(screen,button,game_type,mb,mx,my,background)
            
        
    elif game_type == "memory":
        #card_blit(screen,card_rects)
        pick(card_contents,card_rects,clicking, click, picked, picked_rec, matched_rec,match_status)
        organize(card_c,card_contents,card_r,card_rects)
        card_r = cards(card_contents,card_r)

        check_match(picked, match, card_rects, matched_rec, card_contents, points)
    if game_type != "menu":
        player_bars(screen,player_chosen,players,colours)
    
    display.flip()
    
quit()
