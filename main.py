from random import randint
from imagescode2 import imagesbattle
import time
import random
gamestate = {"your_turn":1,"battle":1,"php":100,"pdmg":10,"display":"fish","ehp":100,"edmg":10,"ename":"Enemy","eHlike":3,"eHlim":3,"victory":0,"mass":0}
action = ["hit", "check"]

def img(pic):
    print(imagesbattle[pic])
def introsequence():
    print("\n\nI hereby sentence you to life in prison without the possibility of parole!")
    img("gavel")
    time.sleep(4)
    print("...")
    time.sleep(2)
    img("behindbars")
    print("Life sentence... I'm way too young!")
    time.sleep(2) 
    print("I have to get out of here, no way I'm wasting away in here!")
    time.sleep(2)

introsequence()
# X och Y motsvarar stoleken på spelbrädet
X = 11
Y = 10

# Possible direction
LEFT, RIGHT, FORWARD, BACKWARD = 1, 2, 3, 4


# Print the directions menu
def direction_meny():
    directions = {'1': 'left', '2': 'right', '3': 'farward', '4': 'backward'}

    print('\nYou have only 4 chices: ')
    for direction in directions:
        print(f'{direction}) {directions[direction]}')
    print()


# Create a 2-dimensional array
def gameBoard():
    board = [[0 for rad in range(X)] for kolumn in range(Y)]
    return board


# Draw the board of the game
def drawBoard(board):
    print("+---" * X + "+")
    for rad in board:
        for kolumn in rad:
            if kolumn == 1:
                print("| X ", end="")
            elif kolumn == 2:
                print("| P ", end="")
            else:
                print("|   ", end="")
        print(f"|   ")
        print("+---" * X + "+")


# Select a coordinate for a given X and Y value, 1 corresponds to user.
def select_coord(board, x, y):
    board[y][x] = 1
    return board


def cop(board):
    
    x_dir_list = list(range(0,5)) + list(range(6, X))
    x_dir = random.choice(x_dir_list)
    
    y_dir_list = list(range(0,9)) + list(range(10, Y))
    y_dir = random.choice(y_dir_list)
    
    board[y_dir][x_dir] = 2
    return board


# Unselect a coordinate for a given X and Y value, 0 corresponds to empty.
def unselect_coord(board, x, y):
    board[y][x] = 0
    return board


# move the user in the board of the game
def movments():
    board = gameBoard()
    gameover = False
    x_dir = 5
    y_dir = 9

    board = select_coord(board, x_dir, y_dir)
    cop(board)
    drawBoard(board)
    direction_meny()

    while not gameover:
        try:
            board = unselect_coord(board, x_dir, y_dir)

            direction = int(input('Chose your diraction: '))

            if direction == LEFT:
                x_dir -= 1
            elif direction == RIGHT:
                x_dir += 1
            elif direction == FORWARD:
                y_dir -= 1
            elif direction == BACKWARD:
                y_dir += 1
            else:
                print("You can't do that...")
            
            board = select_coord(board, x_dir, y_dir)
            
            drawBoard(board)
            direction_meny()
            
        except:
            break



menuoptions = ["start", "instructions", "help", "skipcutscene"]              
def mainmenu():
    print(imagesbattle["prison"])
    print(imagesbattle["menutext"])
    print("""Type one:
""")
    for x in menuoptions:
        if x != "help" and x != "skipcutscene":
            print(f"{x.capitalize()}")
    h = 1
    while h == 1:
        s = input().lower()
        if s in menuoptions:
            if s == menuoptions[0]:
                h = 0
                introsequence()
                
                #start and shit
            if s == menuoptions[1] or s == menuoptions[2]:
                instructions()
            if s == menuoptions[3]:
                walk(0,0,-1,0,0,1,1,2)
        else:
            print("You can't do that.")

def instructions():
    print("Here are the instructions:")
        
def battle(name, hp, dmg, image, eHlike, eHlim, yourturn):   
    gamestate["ehp"]= hp
    gamestate["edmg"] = dmg
    gamestate["display"] = image
    gamestate["your_turn"] = yourturn
    img(image)
    while gamestate["battle"] == 1:
        while gamestate["your_turn"] == 1:  #Din tur
            if gamestate["ehp"] > 0 and gamestate["php"] > 0 :
                s = input().lower()
                if s == action[0]:
                    hit()
                elif s == action[1]:
                    check(image)
                else:
                    print(f"You can't do that.")
            elif gamestate["ehp"] <= 0:
                print(f"{name} died!")
                gamestate["victory"] = 1
                gamestate["battle"] = 0
                gamestate["your_turn"] = 2
            else:
                print("You died!")
                gamestate["victory"] = 0
                gamestate["battle"] = 0
                gamestate["your_turn"] = 2
        while gamestate["your_turn"] == 0:  #Motståndarens tur
            if gamestate["php"] > 0 and gamestate["ehp"] > 0:
                ehit(name, eHlike, eHlim) 
            elif gamestate["ehp"] <= 0:
                print(f"{name} died!")
                gamestate["victory"] = 1
                gamestate["battle"] = 0
                gamestate["your_turn"] = 2
            else:
                print("You died!")
                gamestate["victory"] = 0
                gamestate["battle"] = 0
                gamestate["your_turn"] = 2
#Player actions below
def hpcheck():
    print ("You:", gamestate["php"], "hp")
    print (gamestate["display"], ":", gamestate["ehp"], "hp")
def check(image):
    img(image)
    hpcheck()
    if gamestate["display"] == "Medusa":
        print(f"Medusa turned you into stone!")
        gamestate["your_turn"] = 0
def hit():
    print(f"You hit")
    gamestate["ehp"] = gamestate["ehp"]- gamestate["pdmg"] * (randint(10,20) / randint(5,15))
    gamestate["your_turn"] = 0
#Enemy Actions Below:
def ehit(name, hitlikelihood, hitlimit): 
    hitattempt = randint(0,hitlikelihood)
    if hitattempt >= hitlimit:
        print(f"{name} missed!")
        gamestate["your_turn"] = 1
    else:
        gamestate["php"] = gamestate["php"] - (gamestate["edmg"] + randint(10,40))
        print(f"{name} swings!")
        gamestate["your_turn"] = 1
        



movment()
