'''
Snake Water Gun Game
Stone Paper Siccor Game
Guess The Number Game
            Developed, Coded & Tested by Krishna.
                From: GamesON Game Team - Future of Gaming India
'''
def SWG_Game():
    '''This function is for Snake Water Gun game You just have to write 'SWG_Game()' to run it.'''
    from random import randint
    print('It is a (Snake, Water, Gun) Game; Enjoy it!')
    chanceno = int(input('How many turns you want to play? : '))
    user_score=0
    cpu_score=0
    i = 1
    while i<(chanceno+1):
        lst = ['Snake','Water','Gun']
        cpu = lst[randint(0,2)]
        print(f'\nTurn no. {i}')
        a = input('Type your choice (Snake/Water/Gun) : ')
        i+=1
        if  a.upper()=='SNAKE' and cpu=='Snake':
            print(f'CPU choose {cpu}')
            print('Its a tie')
        elif  a.upper()=='SNAKE' and cpu=='Water':
            print(f'CPU choose {cpu}')
            print('You score 10 point')
            user_score+=10
        elif  a.upper()=='SNAKE' and cpu=='Gun':
            print(f'CPU choose {cpu}')
            print('CPU score 10 point')
            cpu_score+=10
        elif  a.upper()=='WATER' and cpu=='Snake':
            print(f'CPU choose {cpu}')
            print('CPU score 10 point')
            cpu_score+=10
        elif  a.upper()=='WATER' and cpu=='Water':
            print(f'CPU choose {cpu}')
            print('Its a tie')
        elif  a.upper()=='WATER' and cpu=='Gun':
            print(f'CPU choose {cpu}')
            print('You score 10 point')
            user_score+=10
        elif  a.upper()=='GUN' and cpu=='Snake':
            print(f'CPU choose {cpu}')
            print('You score 10 point')
            user_score+=10
        elif  a.upper()=='GUN' and cpu=='Water':
            print(f'CPU choose {cpu}')
            print('CPU score 10 point')
            cpu_score+=10
        elif  a.upper()=='GUN' and cpu=='Gun':
            print(f'CPU choose {cpu}')
            print('Its a tie')
        else:
            print('Spelling mistake or Wrong input, CPU will given 5 points')
            cpu_score+=5
    print(f'\n\n G A M E  O V E R \n\nYour score : {user_score}\nCPU score : {cpu_score}')
    if user_score < cpu_score:
        print('!! You Loss the Game !!')
    elif user_score > cpu_score:
        print('!! You Win the Game !!')
    else:
        print('!! Game tie !!')











def SPS_Game():
    '''This function is for Stone Paper Siccor game You just have to write 'SPS_Game()' to run it.'''
    from random import randint
    print('It is a (Stone, Paper, Siccor) Game; Enjoy it!')
    chanceno = int(input('How many turns you want to play? : '))
    user_score=0
    cpu_score=0
    i = 1
    while i<(chanceno+1):
        lst = ['Stone','Paper','Siccor']
        cpu = lst[randint(0,2)]
        print(f'\nTurn no. {i}')
        a = input('Type your choice (Stone/Paper/Siccor) : ')
        i+=1
        if  a.upper()=='STONE' and cpu=='Stone':
            print(f'CPU choose {cpu}')
            print('Its a tie')
        elif  a.upper()=='STONE' and cpu=='Paper':
            print(f'CPU choose {cpu}')
            print('CPU score 10 point')
            cpu_score+=10
        elif  a.upper()=='STONE' and cpu=='Siccor':
            print(f'CPU choose {cpu}')
            print('You score 10 point')
            user_score+=10
        elif  a.upper()=='PAPER' and cpu=='Stone':
            print(f'CPU choose {cpu}')
            print('You score 10 point')
            user_score+=10
        elif  a.upper()=='PAPER' and cpu=='Paper':
            print(f'CPU choose {cpu}')
            print('Its a tie')
        elif  a.upper()=='PAPER' and cpu=='Siccor':
            print(f'CPU choose {cpu}')
            print('CPU score 10 point')
            cpu_score+=10
        elif  a.upper()=='SICCOR' and cpu=='Stone':
            print(f'CPU choose {cpu}')
            print('CPU score 10 point')
            cpu_score+=10
        elif  a.upper()=='SICCOR' and cpu=='Paper':
            print(f'CPU choose {cpu}')
            print('You score 10 point')
            user_score+=10
        elif  a.upper()=='SICCOR' and cpu=='Siccor':
            print(f'CPU choose {cpu}')
            print('Its a tie')
        else:
            print('Spelling mistake or Wrong input, CPU will given 5 points')
            cpu_score+=5
    print(f'\n\n G A M E  O V E R \n\nYour score : {user_score}\nCPU score : {cpu_score}')
    if user_score < cpu_score:
        print('!! You Loss the Game !!')
    elif user_score > cpu_score:
        print('!! You Win the Game !!')
    else:
        print('!! Game tie !!')












def Number_Guessing_Game():
    '''This function is for Number Guessing Game You just have to write 'Number_Guessing_Game()' to run it.'''
    from random import randint
    num =randint(0, 100)
    gnum = 0
    print('This is a two player game\nIts time for first player!\n')
    p1 = input(('Enter your name :  '))

    print(f'Let\'s play {p1}')

    guess = int(input('Guess a number between 0 to 100 : '))
    game_over = False
    while not game_over:
        if guess:
            if num == guess :
                print(f'You WIN !! after {gnum} wrong guesses.\n')
                gnum += 1
                game_over= True
            elif num < guess :
                gnum += 1
                print('You guess too high')
                guess = int(input('Guess again : '))
            elif num > guess:
                gnum += 1
                print('You guess too low')
                guess = int(input('Guess again : '))
            else:
                pass
        else:
            gnum2 += 1
            print('You didn\'t type anything.')
            guess2 = int(input('Guess again : '))
    print('Its time for second player !\n')
    p2 = input(('Enter your name :  '))
    import random
    num2 = random.randint(0, 100)
    gnum2 = 0

    print(f'Let\'s play {p2}')

    guess2 = int(input('Guess a number between 0 to 100 : '))
    game_over2 = False
    while not game_over2:
        if num2 == guess2 :
            print(f'You WIN !! after {gnum2} wrond guesses.')
            gnum2 += 1
            game_over2= True
        elif num2 < guess2:
            gnum2 += 1
            print('You guess too high')
            guess2 = int(input('Guess again : '))
        elif num2 > guess2:
            gnum2 += 1
            print('You guess too low')
            guess2 = int(input('Guess again : '))
        else:
            gnum2 += 1
            print('You didn\'t type anything.')
            guess2 = int(input('Guess again : '))
    if gnum < gnum2:
        print(f'{p1} (Player 1) wins!!')
    elif gnum > gnum2:
        print(f'{p2} (Player 2) wins!!')
    else:
        print('Its a tie ~~ No wins, No loose')









print('1 for Snake,Water,Gun Game\n2 for Stone,Paper,Siccor Game\n3 for Number Guessing Game')
i = int(input('What game do you want to play? : '))
if i==1:  SWG_Game()
elif i==2: SPS_Game()
elif i==3: Number_Guessing_Game()
else: print('Wrong input, Run again')