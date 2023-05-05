import os
import re
from board import Board

class Game:
    def __init__(self, board_size, players):
        self.players_lst = players
        self.board_game = Board(board_size)
    
    def allIsEqLst(self, player, lst):
        for l in lst:
            if l != player:
                return False
        return True

    def check(self, player):
        pp = self.board_game.getSize()
        for i in range(pp):
            #lines:
            if self.allIsEqLst(player, self.board_game.get()[i]): 
                return True
            #columns:
            if self.allIsEqLst(player, [self.board_game.get()[m][i] for m in range(pp)]): 
                return True
            # Diagonals:
        return self.allIsEqLst(player, [self.board_game.get()[m][m] for m in range(pp)]) or self.allIsEqLst(player, [self.board_game.get()[pp-m-1][m] for m in range(pp)])
    
    def vaild(self,ans):
        ans = ans.split(',')
        if len(ans) == 2:
            if bool(re.match(r'^\d+$',ans[0])) and bool(re.match(r'^\d+$',ans[1])): 
                return self.board_game.isEmpty(int(ans[0]),int(ans[1])) 
        return False

    def start(self):
        os.system('cls')
        mo = 1 #Que counter
        print(self.board_game)
        while mo <= self.board_game.getSize() ** 2:
            indexPlayer = mo % len(self.players_lst)
            player = self.players_lst[indexPlayer].cha
            answer = input(f'{player} please insert x,y: ')
            while not self.vaild(answer):
                answer = input(f'{player} please insert x,y -again-: ')
            answer = answer.split(',')
            x, y = int(answer[0]), int(answer[1])
            self.board_game.setValue(player,x,y)
            os.system('cls')
            print(self.board_game)
            if self.check(player):
                print(f'{player} is the winner!')
                for pl in range(len(self.players_lst)):
                    if pl == indexPlayer: 
                        self.players_lst[pl].vic += 1
                    else: 
                        self.players_lst[pl].los += 1
                    self.players_lst[pl].updateData()
                break
            mo += 1
            if mo > self.board_game.getSize() ** 2: #save data of this game
                for pl in self.players_lst:
                    pl.eve += 1
                    pl.updateData()


