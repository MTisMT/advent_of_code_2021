import numpy as np
import re

class board():
    def __init__(self,the_board):
        self.nums = the_board
        self.mark = np.zeros((5,5))
        
    def marked(self,called):
        for i in range(5):
            for j in range(5):
                if int(self.nums[i,j]) == called:
                    self.mark[i,j] = 1
                    
    def won(self):
        for n in range(5):
            if (np.sum(self.mark[n,:])==5 or np.sum(self.mark[:,n])==5):
                return True
        return False
    
    def score(self,called):
        return int(called) * (np.sum((1-self.mark)*self.nums))

with open("bingo.txt") as f:
    lines = [l.strip() for l in f]
randoms = [int(n) for n in lines[0].split(',')]
all_boards = []
for i in range(100):
    the_board = np.zeros((5,5))
    for j in range(5):
        row = lines[6*i+j+2]
        row = re.sub(' +',' ',row) # Equivalent code: row = row.replace('  ',' ')
        the_board[j,:] = [int(r) for r in row.split(' ')]
    all_boards.append(board(the_board))
def play1(randoms, all_boards):     
    for called_rand in randoms:
        for b in all_boards:
            b.marked(called_rand)
            if b.won():
                return b.score(called_rand),called_rand,b.mark,b.nums
def play2(randoms, all_boards):     
    for called_rand in randoms:
        for b in all_boards:
            if not b.won():
                b.marked(called_rand)
                if b.won():
                    score = b.score(called_rand)
    return score
score_1,called_rand, mark , num = play1(randoms, all_boards)
print("Answer of part 1: ", score_1)
score_2 = play2(randoms, all_boards)
print("Answer of part 2: ", score_2)
