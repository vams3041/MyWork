import random

class Game:
    def __init__(self, newPlayerName):
        self.playerName = newPlayerName
        self.playerHand = "NA"
        self.botHand = "NA"
        self.winner = "No Winner Yet"
        print("New instance of game class for " + self.playerName)

    def runGame(self, x, y):
        if x in range(0,4):
            if self.playerHand == self.botHand:
                print('you tie')
            elif self.playerHand > self.botHand:
                print('you lose')
            elif self.playerHand < self.botHand:
                print('you win')
        else:
            print("invalid input")


"""        
        elif (self.playerHand == 'paper') and self.botHand == 1:
            print('you win')
        elif (self.playerHand == 'paper') and self.botHand == 2:
            print("you tie")
        elif (self.playerHand == 'paper') and self.botHand == 3:
            print("you lose")
        elif (self.playerHand == 'scissors') and self.botHand == 1:
            print("you lose")
        elif (self.playerHand == 'scissors') and self.botHand == 2:
            print("you win")
        elif (self.playerHand == 'scissors') and self.botHand == 3:
            print("you tie")
"""


def main():
    a = ['vamshi', 'raja', 'james', 'zach']
    for i in a:
        x = int(input("what is your call? 'rock,Paper or Scissors?'"))
        y = random.randrange(1,4)
        print("Y = ", + y)
        print("X = ", + x)
        myGame = Game(i)

        print(myGame.playerName)
        print(myGame.playerHand)
        print(myGame.botHand)
        print(myGame.winner)

        myGame.playerHand = x
        myGame.botHand = y
        myGame.runGame(x, y)
        print("Y = ", + y)
        print("X = ", + x)
        print(myGame.winner)
# """
#         otherGame = Game('Raja')
#         otherGame.runGame(x, y)
#         print(otherGame.winner)
#         print("Y = ", + y)
#         print("X = ", + x)
# """
        print("**************************")

main()