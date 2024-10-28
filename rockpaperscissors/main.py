import random


choice = ["rock", "papper", "scissors"]


def choiceChecker(userinput):
    if userinput == 1:
        return choice[0]
    elif userinput == 2:
        return choice[1]
    elif userinput == 3:
        return choice[2]
    else:
        print("enter valid number")


def checker(player1, player2):
    if player1 == choice[0] and player2 == choice[2]:
        print("\nyou won\n")
        return
    elif player1 == choice[1] and player2 == choice[2]:
        print("\nyou won\n")
        return
    if player2 == choice[0] and player1 == choice[2]:
        print("\nyou lost\n")
        return
    elif player2 == choice[1] and player1 == choice[2]:
        print("\nyou lost\n")
        return
    else:
        return 1


while True:
    userinput = input("\t1, Rock\n\t2, Papper\n\t3, Scissors\n))")
    try:
        if int(userinput) > len(choice):
            print("invalid input")
            break
    except ValueError:
        break
    user = choiceChecker(int(userinput))
    computer_choice = choiceChecker(random.randrange(1, 4))
    print("{} vs {}".format(user, computer_choice))
    check = checker(user, computer_choice)
    if check is None:
        break
    if check == 1:
        print("\ndrew\n")
    elif check is None:
        break
