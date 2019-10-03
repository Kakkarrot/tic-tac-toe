import socket

#setting up the player

#Some methods for better organization
class MyPlayer:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    def __init__(self):
        self.client.connect(('localhost', 8080))

    def myReadAll(self):
        final = b""
        while True:
            from_server = self.client.recv(1)  # Read Message
            if (from_server.decode('utf-8') == ';'):
                break;
            print(from_server.decode('utf-8'), end="")

    def checkInput(self, choice):
        if (choice == "0" or choice == "1" or choice == "2"):
            return True;
        print("Invalid input! Please try a number between 0 and 2. ")
        return False;

#Playing the game
player = MyPlayer();

try:
    while True:
        player.myReadAll();
        choice = '';
        while True:
            choice = input();
            if (player.checkInput(choice)):
                break;
        player.client.send(choice.encode());
except:
    print("You have disconnected. ");
