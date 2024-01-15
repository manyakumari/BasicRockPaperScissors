import random


print("Rock, Paper, Scissors!!!\n")
print("Rules: rock beats scissors. scissors beats paper. paper beats rock. ")
compscore = 0
playerscore = 0

while 0 == 0:
    p = str(input("Choooooooose Your Weaponnn (rock or paper or scissors) or type 'stop' to end game or 'score' to check score: "))
    c = random.randint(1,3) #1 = rock 2 = scissors 3 = paper
    if p == "stop":
        print("Thank you for playing. \nComputer: ", compscore, "Player: ", playerscore)
        if playerscore > compscore:
            print("\nYOU WON OVERALL")
        elif compscore > playerscore:
            print("\nCOMPUTER WON OVERALL")
        else:
            print("\nIT'S A DRAW. NO ONE WINS OVERALL")
    if p == "score":
        print("\nComputer: ", compscore, "Player: ", playerscore, "\n")

    
    elif p == "rock":
        if c == 2:
            print("Computer chose scissors! You get a point\n")
            playerscore = playerscore +1
        elif c == 3:
            print("Computer chose paper! Computer gets a point\n")
            compscore = compscore+1
        elif c == 1:
            print("Draw! no one gets a point\n")

    elif p == "paper":
        if c == 1:
            print("Computer chose rock! You get a point\n")
            playerscore = playerscore +1
        elif c == 2:
            print("Computer chose scissors! Computer gets a point\n")
            compscore = compscore+1
        elif c == 3:
            print("Draw! no one gets a point\n")
        
    elif p == "scissors":
            if c == 1:
                print("Computer chose rock! Computer gets a point\n")
                compscore = compscore+1
            elif c == 3:
                print("Computer chose paper! You get a point\n")
                playerscore = playerscore +1
            elif c == 2:
                 print("Draw! no one gets a point\n")
    