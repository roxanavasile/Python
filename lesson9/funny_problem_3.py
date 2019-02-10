import random

def main():
    player=int(input('Please enter 1 for rock, 2 for paper, or 3 for scissors:'))
    computer=random.randint(1,3)
    find_winner(player,computer)

def find_winner(player,computer):

    if player == 1 and computer==1:
        print('You chose rock. The computer chose rock.It is a tie.')
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')
    elif player ==1 and computer==2:
        print( "You chose rock. The computer chose paper. Computer wins.")
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')
    elif player==1 and computer==3:
        print('You chose rock. The computer chose scissors.You won.')
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')
    elif player==2 and computer==1:
        print('You chose paper. The computer chose rock.You won.')
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')
    elif player==2 and computer==2:
        print('You chose paper. The computer chose paper.It is a tie.')
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')
    elif player==2 and computer==3:
        print('You chose paper. The computer chose scissors. The computer wins.')
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')
    elif player==3 and computer==1:
        print('You chose scissors. The computer chose rock.The computer wins wins.')
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')
    elif player==3 and computer==2:
        print('You chose scissors. The computer chose paper.You won.')
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')
    elif player==3 and computer==3:
        print('You chose scissors. The computer chose scissors.It is a tie.')
    else:
        print('Game canceled because of invalid entry.')
        try_again=input('Do you want to try again? [y/n]')
        if try_again == "y":
                main()
        else:
            print('Why not? Sorry to see you leave.')

main()
