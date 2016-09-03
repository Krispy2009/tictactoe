print "Here we go"
import random
import time

class Board(object):
    def __init__(self):
        self.board = [[0]*3 for i in range(3)]
        self.marks = [' ','x','o']

    def __str__(self):
        s = ''
        for i in self.board:
            s += str([self.marks[x] for x in i]) + '\n'
        return s


    def check_board(self):

        return any([
            self.check_horizontal(),
            self.check_vertical(),
            self.check_diagonal()
        ])

    def check_horizontal(self):
        players = [1,2]
       # import pudb; pu.db
        for player in players:
            for row in self.board:
                player_won = True
                for x in row:
                    if x == player:
                        continue
                    else:
                        player_won=False
                        break
            if player_won:
                'Player %s WON' % player    
                return player
        return 0

    def check_vertical(self):
        players = [1,2]
        player_won = False
        for player in players:
            # A way to get the idx 0,1,2 without doing range(len(self.board))
            # which is what i mean.
            for x in range(3):
                player_won = True
                for row in self.board:
                    if row[x] == player:
                        continue
                    else:
                        player_won = False
                        break
                if player_won:
                    'Player %s WON' % player
                    return player
        return 0
                
    def check_diagonal(self):
        players = [1,2]
        player_won = False
        for player in players:
            # The forward diagonal
            for x in range(3):
                player_won = True
                if player == self.board[x][x]:
                    continue
                else:
                    player_won = False
                    break
            if player_won:
                'Player %s WON' % player
                return player

            #The backward diagonal
            for x in range(3):
                player_won = True
                if player == self.board[x][2-x]:
                    continue
                else:
                    player_won = False
                    break

            if player_won:
                'Player %s WON' % player
                return player
            return 0

                    

    

class Player(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __str__(self):
        return "%s is %s's"%(self.name, [' ', 'x', 'o'][self.id])

    def place_mark(self, board, x, y):
        if not board[x][y]:
            print "%s puts a mark at %s" % (self.name, (x,y))
            board[x][y] = self.id
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
            print "Round %s:" % rounds
            while True:
                placed = player.place_mark(board.board,random.choice([0,1,2]), random.choice([0,1,2]))
                if placed or rounds > 9:
                    rounds +=1
                    break
            
            won = board.check_board()
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

