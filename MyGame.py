import socket
from threading import Thread
from Classes import *

class myGame():
    def __init__(self):
        pass

    def askRow(self, player):
        player.sendall(b"Please enter a row number between 0 and 2. \n");
        player.sendall(b';');
        return player.recv(1).decode();

    def askColumn(self, player):
        player.sendall(b"Please enter a column number between 0 and 2. \n");
        player.sendall(b';');
        return player.recv(1).decode();

    def gameWinner(self, player1, player2, ref):
        ref.drawBoard(player1);
        ref.drawBoard(player2);
        player1.sendall(b"You Win! Please reconnect to play again. \n");
        player1.sendall(b';');
        player1.close();
        player2.sendall(b"You Lose! Please reconnect to play again. \n");
        player2.sendall(b';');
        player2.close();

    def tieGame(self, player1, player2, ref):
        ref.drawBoard(player1);
        ref.drawBoard(player2);
        player1.sendall(b"It's a tie! Please reconnect to play again. \n");
        player1.sendall(b';');
        player1.close();
        player2.sendall(b"It's a tie! Please reconnect to play again. \n");
        player2.sendall(b';');
        player2.close();

    def playerInput(self, player1, player2, ref, mark):
        ref.drawBoard(player1);
        ref.drawBoard(player2);
        player2.sendall(("Waiting on player " + mark + ". \n").encode());
        player1.sendall(b"It is your turn to play. ")
        row = int(self.askRow(player1))
        col = int(self.askColumn(player1))
        if (not (ref.empty(row, col))):
            player1.sendall(b"Please pick an empty space. \n");
            self.playerInput(player1, player2, ref, mark);
        else:
            ref.fillBoard(row, col, mark);

    def runGame(self, player1, player2, ref):
        try:
            while True:
                self.playerInput(player1, player2, ref, "X")
                if (ref.checkVictory()):
                    self.gameWinner(player1, player2, ref);
                    break;
                if (ref.fullBoard()):
                    self.tieGame(player1, player2, ref);
                    break;
                self.playerInput(player2, player1, ref, "O")
                if (ref.checkVictory()):
                    self.gameWinner(player2, player1, ref);
                    break;
        except:
            try:
                player1.sendall(b"Opponent disconnected. Please reconnect. \n")
            except:
                pass
            try:
                player2.sendall(b"Opponent disconnected. Please reconnect. \n")
            except:
                pass

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('localhost', 8080))
serv.listen()

while True:
    try:
        conn1, addr1 = serv.accept()
        conn1.sendall(b"You are Player X. Please wait for player O. \n")
        print('Game Setting Up. ')
        print('Player X Joined! ')
        conn2, addr2 = serv.accept()
        print('Player O Joined! ')
        print('Game Commencing! ')
        conn1.sendall(b"Player O connected. Game will begin. \n")
        conn2.sendall(b"You are Player O. Game will begin. \n")
        ref = MyReferee();
        game = myGame();
        t = Thread(target=game.runGame, args=(conn1, conn2, ref))
        t.start()
        #game.runGame(conn1, conn2, ref);
    except:
        conn2.sendall(b"Opponent disconnected. Please reconnect. \n")

