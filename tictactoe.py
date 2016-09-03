import sys
import random
import time


MARKS = [' ','\033[34mx\033[37m','\033[33mo\033[37m']


class Board(object):
    def __init__(self):
        self.board = [0]*9
        self.marks = MARKS
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
        return "%s is %s"%(self.name, MARKS[self.id])


    def place_mark(self, board, pos):
        try:
            pos = int(pos)
        except:
            return False

        if pos in range(9) and not board[pos]:
            print "\033[K%s puts a mark at %s" % (self.name, pos)
            board[pos] = self.id
            return True
        else:
            return False


def play(board, player1, player2):
    players_banner = str(player1) + ' | ' + str(player2)
    print players_banner
    print '-' * len(players_banner)
    rounds = 1
    won = 0
    while(rounds < 10):
        for player in (player1, player2):

            if rounds == 10 :
                print '\033[8B';
                break

            print "\nRound %s" % rounds
            while True:
                #choice = raw_input("%s please enter a position (0-8):" % player.name)
                #for testing
                choice = random.choice(range(9))
                placed = player.place_mark(board.board,choice)
                if placed:
                    rounds +=1
                    break

            print board

            # No need to check if anybody won if we are at the start of the game
            if rounds > 3:
                won = board.is_winner(player.id)
                if won:
                    print 'WE HAVE A WINNER!'
                    break

            print '\033[8A'
            time.sleep(1)

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

