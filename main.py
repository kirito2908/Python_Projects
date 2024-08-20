import random

def result (turns, p1Guesses, p2Guesses, p1Score, p2Score, player1, player2):
    if (p2Guesses < p1Guesses):
        print("")
        print(f"Congratulations {player2} ! You've Won The Game With {p2Guesses} Guesses And Your Score Is {p2Score} Guesses")
        print("")
        print(f"Better Luck Next Time {player1}. Your Score Is {p1Score} With {p1Guesses} Guesses")
        print("")
    elif (p2Guesses > p1Guesses):
        print("")
        print(f"Congratulations {player1} ! You've Won The Game With {p1Guesses} Guesses And Your Score Is {p2Score}")
        print("")
        print(f"Better Luck Next Time {player2}. Your Score Is {p2Score} With {p2Guesses} Guesses")
        print("")
    elif (p2Guesses == p1Guesses):
        print("")
        print(f"Great Game {player1} & {player2}. The Game Has Ended In A Draw With Both Having Same Gussing Tries Of {p1Guesses}")
        print("")

player1 = input("Enter First Player Name : ")
player2 = input("Enter Second Player Name : ")
print("")
turns = 1
guesses = 0
p1Guesses = 0
p2Guesses = 0
p1Score = 0
p2Score = 0
theFlag = True
p1Turn = True
p2Turn = False

print("Please Enter A Number Between 1 to 10 Below\nType 'Stop' If You Want To Stop Playing")
print("")
computer = random.randint(1, 10)

while theFlag :
    if (p1Turn):
        playerInput = input(f"{player1} Enter Input : ")
        print("")
        if (playerInput.lower() != "stop"):
            try:
                if (int(playerInput) > 10):
                    print("Please Enter A Valid Number")
                    print("")
                else:
                    if (int(playerInput) == computer):
                        print(f"Congratulations ! Your Entered Number {playerInput} Is Correct")
                        print("")
                        turns += 1
                        p1Guesses += guesses + 1
                        p1Score += 1
                        p1Turn = False
                        p2Turn = True
                        guesses = 0
                        computer = random.randint(1, 10)
                    elif (int(playerInput) > computer):
                        print(f"The Number Is Less Than {playerInput}")
                        guesses += 1
                        if (guesses <= 5):
                            print(f"You Have {5 - guesses} Tries Left")
                            print("")
                        else:
                            theFlag = False
                    elif (int(playerInput) < computer):
                        print(f"The Number Is Greater Than {playerInput}")
                        guesses += 1
                        if (guesses <= 5):
                            print(f"You Have {5 - guesses} Tries Left")
                            print("")
                        else:
                            theFlag = False
                    elif (guesses > 5):
                        print("You've Exhausted Your Tries.\nBetter Luck Next Time")
                        result(turns, p1Guesses, p2Guesses, p1Score, p2Score, player1, player2)
                        theFlag = False
            except:
                print("Enter A Valid Input")
        else:
            result(turns, p1Guesses, p2Guesses, p1Score, p2Score, player1, player2)
            theFlag = False
    elif (p2Turn):
        playerInput = input(f"{player2}, Enter Input : ")
        print("")
        if (playerInput.lower() != "stop"):
            try:
                if (int(playerInput) > 10):
                    print("Please Enter A Valid Number")
                else:
                    if (int(playerInput) == computer):
                        print(f"Congratulations ! Your Entered Number {playerInput} Is Correct")
                        print("")
                        turns += 1
                        p2Guesses += guesses + 1
                        p2Score += 1
                        p1Turn = True
                        p2Turn = False
                        guesses = 0
                        computer = random.randint(1, 10)
                    elif (int(playerInput) > computer):
                        print(f"The Number Is Less Than {playerInput}")
                        guesses += 1
                        if (guesses <= 5):
                            print(f"You Have {5 - guesses} Tries Left")
                            print("")
                        else:
                            theFlag = False
                    elif (int(playerInput) < computer):
                        print(f"The Number Is Greater Than {playerInput}")
                        guesses += 1
                        if (guesses <= 5):
                            print(f"You Have {5 - guesses} Tries Left")
                            print("")
                        else:
                            theFlag = False
                    elif (guesses > 5):
                        print("You've Exhausted Your Tries.\nBetter Luck Next Time")
                        result(turns, p1Guesses, p2Guesses, p1Score, p2Score, player1, player2)
                        theFlag = False
            except:
                print("Enter A Valid Input")
        else:
            result(turns, p1Guesses, p2Guesses, p1Score, p2Score, player1, player2)
            theFlag = False