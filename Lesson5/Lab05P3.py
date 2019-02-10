_author_='Roxana Vasile'

player_1=input('Player 1 please enter R for rock, P for paper, or S for scissors:')
player_2=input('Player 2 please enter R for rock, P for paper, or S for scissors:')
player_1=player_1.upper()
player_2=player_2.upper()

if player_1 == 'R' and player_2=='R':
    print('It is a tie.')
elif player_1=='R'and player_2=='P':
    print( "Player two wins.")
elif player_1=='R'and player_2=='S':
    print('Player one wins.')
elif player_1=='P'and player_2=='R':
    print('Player one wins.')
elif player_1=='P'and player_2=='P':
    print('It is a tie.')
elif player_1=='P' and player_2=='S':
    print('Player two wins.')
elif player_1=='S' and player_2=='R':
    print('Player two wins.')
elif player_1=='S' and player_2=='P':
    print('Player one wins.')
elif player_1=='S' and player_2=='S':
    print('It is a tie.')
else:
    print('Game canceled because of invalid entry.')
