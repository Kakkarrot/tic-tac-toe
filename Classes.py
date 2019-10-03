import socket

class MyReferee:
    board = [];
    capacity = 0;

    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        capacity = 0;

    def drawBoard(self, player):
        player.sendall((self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + "\n").encode())
        player.sendall(b"--|---|--\n")
        player.sendall((self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + "\n").encode())
        player.sendall(b"--|---|--\n")
        player.sendall((self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + "\n").encode())

    def rowVictory (self):
        if (self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != " "):
            return True;
        if (self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != " "):
            return True;
        if (self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != " "):
            return True;

    def columnVictory(self):
        if (self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != " "):
            return True;
        if (self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != " "):
            return True;
        if (self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != " "):
            return True;

    def diagonalVictory(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]  and self.board[0][0] != " "):
            return True;
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]  and self.board[0][2] != " "):
            return True;

    def checkVictory(self):
        #calls the three checking functions and will return the mark if any evaluate to true
        if (self.rowVictory()):
            return True;
        if (self.columnVictory()):
            return True;
        if (self.diagonalVictory()):
            return True;
        return False;

    def fullBoard(self):
        if (self.capacity == 9):
            return True;
        return False;

    def empty(self, row, col):
        if (self.board[row][col] == " "):
            return True;
        return False;

    def fillBoard(self, row, col, mark):
        self.capacity = self.capacity + 1;
        self.board[row][col] = mark;

