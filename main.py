import os
import utils

while True:
    os.system('cls')
    print('for new game............press 1')
    print('for new user............press 2')
    print('for rank plyers.........press 3')
    print('for percent of wins.....press 4')
    print('for exit................press 5')
    act = input('-> ')
    if act == utils.MenuAct.EXIT.value: break
    else: utils.newMenue(act)

    
