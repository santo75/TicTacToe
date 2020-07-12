import time

# in every print statement first five sapce is printed.

gridBox = [[" "," "," "], [" "," "," "], [" "," "," "]]#
sampleGrid = [[1,2,3], [4,5,6], [7,8,9]]
cc = []
coordinates = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
def drawGrid(grid=gridBox):
    i = 0
    for row in grid:
        i += 1
        print(" "*5, f"{row[0]} | {row[1]} | {row[2]}")
        if i!=3:
            print(" "*5, "-"*9)
    print("\n")

def drawHeader():
    print("\n"*2)
    print(" "*5, "-"*24)
    print(" "*5, "{:^25}".format("Let's Play Tic Tac Toe"))
    print(" "*5, "-"*24, "\n"*2)

class Player:
    def __init__(self):
        self.player1 = str(input(f"{' '*5}Player1, Enter your name: "))
        self.player2 = str(input(f"{' '*5}Player2, Enter your name: "))
        self.p1char = ""
        self.p2char = ""
        self.active_player = None
        print("\n")
        
    def choose(self):
        self.p1char = input("     Hey {}, choose your Tac (X/O): ".format(self.player1)).upper()
        if self.p1char == 'X':
            self.p2char = 'O'
        else:
            self.p2char = 'X'
        print(' '*4, f"Hey {self.player2}, your Tac is: {self.p2char}", "\n")

    @property
    def place_player1(self):
        self.active_player = self.player1
        active = True
        print(" "*4, "Hey {}, choose your place: ".format(self.player1), end="")
        while active:
            try:
                boxNum = int(input())
                i, j = coordinates[boxNum][0], coordinates[boxNum][1]
                if gridBox[i][j] == " ":
                    gridBox[i][j] = self.p1char
                    cc.append(i)
                    cc.append(j)
                    active = False
                else:
                    print(' '*4, "This place is already occupied, choose another: ", end="")
            except Exception as e:
                print(" "*4, "Not a valid entry, Enter again: ", end="")
        print("\n")
        drawGrid()

    @property
    def place_player2(self):
        self.active_player = self.player2
        active = True
        print(" "*4, "Hey {}, choose your place: ".format(self.player2), end="")
        while active:
            try:
                boxNum = int(input())
                i, j = coordinates[boxNum][0], coordinates[boxNum][1]
                if gridBox[i][j] == " ":
                    gridBox[i][j] = self.p2char
                    cc.append(i)
                    cc.append(j)
                    active = False
                else:
                    print(" "*4, "This place is already occupied, choose another: ", end="")
            except Exception as e:
                print(" "*4, "Not a valid entry, Enter again: ", end="")
        print('\n')
        drawGrid()
def check_for_win():
    char = gridBox[cc[0]][cc[1]]
    cc.pop()
    cc.pop()
    for i in range(3):
        if gridBox[i][0]==char and gridBox[i][1]==char and gridBox[i][2]==char:
            return True
        elif gridBox[0][i]==char and gridBox[1][i]==char and gridBox[2][i]==char:
            return True
    if gridBox[0][0] == char and gridBox[1][1]==char and gridBox[2][2]==char:
        return True
    if gridBox[0][2]==char and gridBox[1][1]==char and gridBox[2][0]==char:
        return True
    return False

def grid_has_empty_cells():
    for row in gridBox:
        for cell in row:
            if cell == ' ':
                return True
    return False

def Restart():
    for i in range(3):
        for j in range(3):
            gridBox[i][j] = " "
    start_game()

def start_game():
    drawHeader()
    player = Player()
    print(' '*4, "Boxes are numberd as: ", "\n")
    drawGrid(sampleGrid)
    player.choose()
    while True:
        player.place_player1
        if check_for_win():
            print(" "*4, f"{player.active_player} won!", "\n")
            break
        if not grid_has_empty_cells():
            print(" "*4, "Game Over!", "\n")
            break
        player.place_player2
        if check_for_win():
            print(" "*4, f"{player.active_player} has won!", "\n")
            break
        if not grid_has_empty_cells():
            print(" "*4, "Game Over!", "\n")
            break
if __name__ == "__main__":
    start_game()
    play_again = True
    while True:
        print(' '*4, "Play again? y/n: ", end="")
        while True:
            restart = input().upper()
            if restart == 'Y':
                Restart()
                break
            elif restart == 'N':
                play_again = False
                break
            else:
                print(' '*4, "Enter only y/n: ", end="")
        if not play_again:
            break
    time.sleep(5)
        
        
