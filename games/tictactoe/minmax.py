from anytree import Node,RenderTree

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

	drawBoard(board);

	if isOwin(board):
		print("O wins");
		return [-10,0,0];

	if isXwin(board):
		print("X wins");
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

		board[maxx][maxy] = 'X';
		drawBoard(board);
		board[maxx][maxy] = '_';
		print("value passed up : " + str([maxi,maxx,maxy]));
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

		board[maxx][maxy] = 'O';
		drawBoard(board);
		board[maxx][maxy] = '_';
		print("value passed up : " + str([maxi,maxx,maxy]));
		return [maxi,maxx,maxy];


parent = [0,0,0,1,1,2,2,3,3,4,4,5,5,6,6];
data = [-100,100,100,-100,-100,-100,-100,3,5,2,9,12,5,23,23];
level = [0,1,1,2,2,2,2,3,3,3,3,3,3,3,3]

n = len(parent);

y =n-1;
i = parent[y];
isMax = True;
lvl=3;

for x in range(0,n):
	if lvl != level[y]:
		isMax = not isMax; 
		lvl= level[y];

	if isMax:
		if data[parent[y]]<data[y]:
			data[parent[y]] = data[y];
	else:
		if data[parent[y]]>data[y]:
			data[parent[y]] = data[y];

	print("i: " + str(y) + " data: " + str(data[parent[y]]));

	y = y-1;


print(data[0]);



moves([['X','X','_'],['_','_','_'],['O','_','_']] , False);