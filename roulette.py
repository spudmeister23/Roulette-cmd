### This script will simulate a game of craps
### Multiple players can exist


class player:
    #Player class will have the following attributes
    #Name, Current bet amount, current bet location (these will come from a bet class)

    def __init__(self, name, purse):
        self.name = name
        self.purse = purse

    def placeBet(betLocation, betAmt):
        self.betLocation = betLocation
        self.betAmt = betAmt

    def showPurse():
        return self.purse

class bet:
    #bet location
    #bet amount



def main():

    playerCnt=raw_input("How many players are in the game? Enter X to end the program.")
    if playerCnt = "X":
        print "Game ended"
        return 0
   elseif not str.isdigit(playerCnt)

