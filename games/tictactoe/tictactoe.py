"""tictactoe game for 2 players
from blogpost: http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python by  BILLY REBECCHI,
slightly improved by Horst JENS"""
from __future__ import print_function

choices = []

for x in range (0, 9) :
    choices.append(str(x + 1))

playerOneTurn = True
winner = False
movenum = 0;
pre = 0;

def checkOver():
    for x in range(0,9):
        if choices[x] != 'X' and choices[x] != 'O':
            return False;
    return True;


def isDraw(board):
    for x in range(0,3):
        for y in range(0,3):
            if board[x][y] == "_":
                return False;
    return True;

def isXwin(board):
    for x in range(0,3):
        if board[x][0] == board[x][1] and board[x][1] == board[x][2] and board[x][0] == 'X':
            return True;
    for y in range(0,3):
        if board[0][y] == board[1][y] and board[1][y] == board[2][y] and board[0][y] == 'X':
            return True;
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == 'X':
        return True;
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == 'X':
        return True;
    return False;

def isOwin(board):
    for x in range(0,3):
        if board[x][0] == board[x][1] and board[x][1] == board[x][2] and board[x][0] == 'O':
            return True;
    for y in range(0,3):
        if board[0][y] == board[1][y] and board[1][y] == board[2][y] and board[0][y] == 'O':
            return True;
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == 'O':
        return True;
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == 'O':
        return True;
    return False;

 
def drawBoard(board):
    print("");
    for x in range(0,3):
        print(board[x]);


def moves(board , isXPlay):
    if isOwin(board):
        return [-10,0,0];

    if isXwin(board):
        return [10,0,0];

    if isDraw(board):
        return [0,0,0];
    
    if isXPlay:
        maxi = -float('inf');
        maxx = 0;
        maxy = 0;
        for x in range(0,3):
            for y in range(0,3):
                if board[x][y] == "_":
                    board[x][y] = 'X';
                    val = moves(board,not isXPlay);
                    board[x][y] = '_';
                    if val[0]>maxi:
                        maxi=val[0];
                        maxx=x;
                        maxy=y;
        return [maxi,maxx,maxy];

    else:
        maxi = float('inf');
        maxx = 0;
        maxy = 0;
        for x in range(0,3):
            for y in range(0,3):
                if board[x][y] == "_":
                    board[x][y] = 'O';
                    val = moves(board,not isXPlay);
                    board[x][y] = '_';

                    if val[0]<maxi:
                        maxi=val[0];
                        maxx=x;
                        maxy=y;
        return [maxi,maxx,maxy];


def printBoard() :
    board = [[convert(choices[0]),convert(choices[1]),convert(choices[2])],[convert(choices[3]),convert(choices[4]),convert(choices[5])],[convert(choices[6]),convert(choices[7]),convert(choices[8])]]
    drawBoard(board)

    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')

def convert(val):
    if val == 'X':
        return 'X';

    if val == 'O':
        return 'O';

    return '_';

while not winner :
    printBoard()

    if not playerOneTurn :
        print( "Player 2:")
        try:
            choice = int(input(">> "))
        except:
            print("please enter a valid field")
            continue
        if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
            print("illegal move, plase try again")
            continue

    else :
        print( "Player 1:")
        board = [[convert(choices[0]),convert(choices[1]),convert(choices[2])],[convert(choices[3]),convert(choices[4]),convert(choices[5])],[convert(choices[6]),convert(choices[7]),convert(choices[8])]]
        drawBoard(board);
        res = moves(board,True);
        print(res)
        choice = res[1]*3 + res[2] + 1 ;
        print(choice)


    if playerOneTurn :
        choices[choice - 1] = 'X'
        pre = choice -1;
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

    if checkOver():
        print("GAME IS A DRAW")
        winner = True

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")