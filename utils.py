import os
from player import Player
from game import Game
from enum import Enum

class MenuAct(Enum):
    BACK = '0'
    NEW_GAME = '1'
    NEW_USER = '2'
    RANK_USER = '3'
    WINS_PERCENT = '4'
    EXIT = '5'
    
def login():
    plyer = Player()
    username = input('username: ')
    password = input('password: ')
    while (not plyer.log(username,password)):
        print('---error! please try again---')
        username = input('username: ')
        password = input('password: ')
    return plyer

def  exist(ply_arr, ply):
    for pl in ply_arr:
        if pl.cha == ply.cha: return True
    return False

def getPlayersForNewGame(x):
    print('----New Game----\nlogin system of players')
    players = []
    looop = 0
    while looop < 2:
        print(f'Player {looop+1}')
        ply = login()
        if ply != None and not exist(players, ply): 
            players.append(ply)
            looop +=1
        else: print('you are already in the game....')
    plyerNum = 3 
    while plyerNum <= x:
        act = input('for add player press "y": ')
        if act == 'y':
            print(f'Player {plyerNum}')
            ply = login()
            if ply != None and not exist(players, ply): players.append(ply)
            else: print('you are already in the game....')
            plyerNum += 1
        else: break
    return players

def lineToPlayer(line):
    play = Player()
    line = line[:-1 if line[-1]=='\n' else None].split(',')
    return play.retrive(line[0],line[1],line[2],int(line[3]),int(line[4]),int(line[5]))

def rankPlayers():
    print('----Rank of wins all users----')
    f = open('players.csv')
    rank = {}
    for line in f.readlines():
        pla = lineToPlayer(line)
        rank[pla] = pla.vic

    rank = sorted(rank, key=rank.get, reverse=True)
    ra = 1
    for p in rank:
        print(f'{ra}) {p.rank()}')
        ra += 1
        
def registration():
    print('----Registration----')
    while True:
        plyer = Player()
        username = input('username: ')
        password = input('password: ')
        cha = input('char in the table: ')[0]
        if plyer.reg(cha,password,username): break
        else: 
            print('username or char exist, try somthing else...')
            bac = input('press "e" for exit slse to continue ')
            if bac == 'e': break

def getPercentOfWin(username):
    with open('players.csv') as f:
        line = f.readline()
        while line != '':
            line = line.split(',')
            if line[1] == username:
                return f'{(100 * int(line[3]))/(int(line[3]) + int(line[4]) + int(line[5]))}% of win'
            line = f.readline()
    return 'User has not found'
            
def winPercent():
    print('----Percent of wins----')
    username = ''
    while username != MenuAct.BACK.value:
        username = input('please insert usename to serach or "0" for back\n')
        if username != MenuAct.BACK.value: print(getPercentOfWin(username))

def newMenue(act):
    os.system('cls')
    if act == MenuAct.NEW_GAME.value:
        x = 0
        while x < 3:
            x = input('please innsert size of board (? => 3): ')
            try:
                x = int(x)
            except:
                x = 0
                print('please innsert size of board again (? => 3): ')
        players = getPlayersForNewGame(x)
        Game(x,players).start()
        while True:
            pe = input('for new game press "y"')
            if pe == 'y':
                Game(x,players).start()
            else: break
    elif act == MenuAct.NEW_USER.value:
        registration()
    elif act == MenuAct.RANK_USER.value:
        rankPlayers()
        input('press enter to back the menu')
    elif act == MenuAct.WINS_PERCENT.value:
        winPercent()

