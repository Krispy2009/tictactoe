import random
import time

class Board(object):
    def __init__(self):
        self.board = [0]*9
        self.marks = [' ','x','o']
        self.win_positions = [
            (0,1,2), (3,4,5),(6,7,8), # horizontal
            (0,3,6),(1,4,7),(2,5,8),  # vertical
            (0,4,8),(2,4,6)           # diagonal
        ]

    def __str__(self):
        s = ''
        for idx, i in enumerate(self.board):
            s+= self.marks[i] + ' '
            if idx in (2,5,8):
                s+='\n'
        return s


    def is_winner(self, pl):
        for win in self.win_positions:
            if (pl == self.board[win[0]] and pl == self.board[win[1]]
                    and pl == self.board[win[2]]):
                return True
        return False


class Player(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return "%s is %s's"%(self.name, [' ', 'x', 'o'][self.id])

    def place_mark(self, board, pos):
        try:
            pos = int(pos)
        except:
            return False
        if pos in range(9) and not board[pos]:
            print "%s puts a mark at %s" % (self.name, pos)
            board[pos] = self.id
            return True
        else:
            #print "There's something at (%s,%s) try another position" % (x,y)
            return False


def play(board, player1, player2):
    print board.board
    print player1
    print player2
    rounds = 1
    while(rounds < 10):

        for player in (player1, player2):

            if rounds == 10 : break
            print "Round %s:" % rounds
            while True:
                choice = raw_input("%s please enter a position (0-8):" % player.name)
                #for testing
                #choice = random.choice(range(9))
                placed = player.place_mark(board.board,choice)
                if placed:
                    rounds +=1
                    break

            won = board.is_winner(player.id)
            print board
            if won:
                print 'WE HAVE A WINNER!'
                break
        if won: 
            print "%s has won" % player.name
            break
    if not won:
        print "Nobody won"

if __name__ == '__main__':
    board = Board()
    player1 = Player('Kristi',1)
    player2 = Player('Andy',2)
    play(board, player1,player2)

