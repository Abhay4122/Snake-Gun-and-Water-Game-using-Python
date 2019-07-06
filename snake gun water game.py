# Welcome in Snake Gun Water game
# Rules:-
# 1. User select one number between 1-3
# 2. 1 for Snake, 2 for Gun, 3 for Water
# 3. if user select 1 and computer select random number 2, then Gun kill snake and computer winner
# 4. if user select 2 and computer select 3 then Gun drown in water and computer winner
# 5. if user select 3 and computer select 1 then Snake drink water and computer winner

from random import randint

print('\nWelcome in Snake Gun Water game\n')
print('Rules:-'.center(12, ' '))
print('\n1. User select one number between 1-3\n')
print('2. 1 for Snake\t2 for Gun\t3 for Water\n')
print('3. if user select 1 and computer select 2, then Gun kill snake and computer winner\n')
print('4. if user select 2 and computer select 3 then Gun drown in water and computer winner\n')
print('5. if user select 3 and computer select 1 then Snake drink water and computer winner\n\n')
print('Terms:-'.center(12, ' '))
print('1. There are 10 Rounds in this Game\n')
print('2. According to maximum number of winner win this Game')

def fun():
    comp_win = 0
    you_win = 0
    i = 1
    while 10 >= i:
        print(f'\nRound {i}\n'.center(12, ' '))
        num = int(input('Enter any Number between 1 - 3 : '))
        if num == 1:
            print('\nYour Object is Snake\n')
            while True:
                rand_num = randint(1, 3)
                if rand_num == 1:
                    continue
                elif rand_num == 2:
                    print('Computr\'s Object is Gun\n')
                    print('Computr is Winner\n')
                    comp_win += 1
                    i += 1
                    break
                elif rand_num == 3:
                    print('Computr\'s Object is Water\n')
                    print('You are Winner\n')
                    you_win += 1
                    i += 1
                    break
        elif num == 2:
            print('\nYour Object is Gun\n')
            while True:
                rand_num = randint(1, 3)
                if rand_num == 2:
                    continue
                elif rand_num == 1:
                    print('Computr\'s Object is Snake\n')
                    print('You are Winner\n')
                    comp_win += 1
                    i += 1
                    break
                elif rand_num == 3:
                    print('Computr\'s Object is Water\n')
                    print('Computer is Winner\n')
                    you_win += 1
                    i += 1
                    break
        elif num == 3:
            print('\nYour Object is Water\n')
            while True:
                rand_num = randint(1, 3)
                if rand_num == 3:
                    continue
                elif rand_num == 1:
                    print('Computr\'s Object is Snake\n')
                    print('Computer is Winner\n')
                    comp_win += 1
                    i += 1
                    break
                elif rand_num == 2:
                    print('Computr\'s Object is Gun\n')
                    print('You are Winner\n')
                    you_win += 1
                    i += 1
                    break
    if you_win > comp_win:
        print('Winner winner Chicken Dinner')
        print(f'\nCongratulations You Won the Match by {you_win} : {comp_win}')
        repet_num = int(input('Enter 5 if You want to Play the match Again : '))
        if repet_num == 5:
            fun()
        else:
            print('\nThank You See you again')
    else:
        print('Aww!!! You Lose the Match')
        print(f'\nComputer Won the Match by {you_win} : {comp_win}')
        repet_num = int(input('Enter 5 if You want to Play the match Again : '))
        if repet_num == 5:
            fun()
        else:
            print('\nThank You See you again')
fun()