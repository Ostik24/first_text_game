'''
Guess the Right Room Game!
'''
from random import choice

def main():
    '''
    Main game function
    '''
    def startgame(strt: str):
        '''
        Selecting the difficulty and describing the rules of the game
        '''
        if strt == '0':
            print('\nUnfortunately!\nCome back!\n')
            exit()

        if strt == '1':
            print('\nGuess the Right Room Game!\n\nAt the beginning of the game you \
need to choose the difficulty.\n\
Depending on the difficulty of the game, you will be offered rooms to enter,\nand in which you will receive bonuses \
or anti-bonuses to your result\nBut be careful, because in one of the rooms you can expect an instant loss!\n\
Remember to exit the game, you can press "0" at any time,\nafter which you can choose the difficulty of the game again, \
there are 2 difficulties of the game: simple and hard.\nTo win the game on difficulty simple, you must to \
reach level 10.')
            print('\nTo leave the game you can type "0"')
            print('\nChoose the difficulty: simple or hard')
            while True:
                inputed = input('>>> ')
                if inputed == '0':
                    print('\nAre you sure you want to leave the game?')
                    while True:
                        ext_inp = input('>>> ')
                        if ext_inp.lower() == 'yes' or ext_inp.lower() == 'yep' or \
ext_inp.lower() == 'yeah' or ext_inp.strip() == '1':
                            print('\nUnfortunately!\nCome back!\n')
                            exit()
                        if ext_inp.lower() == 'no' or ext_inp.lower() == 'nope' or \
ext_inp.strip() == '0':
                            print('\nChoose the difficulty: simple or hard:')
                            break
                        else:
                            print('Try again! Type "yes" or "no"')
                elif inputed.lower() != 'hard' and inputed.lower() != 'simple':
                    print('Try again! You can only type "simple" or "hard"!')
                elif inputed.lower() == 'hard':
                    return 'hard'
                elif inputed.lower() == 'simple':
                    return 'simple'

    def simplegame():
        '''
        Starts a simple game
        '''
        result = 0
        level = 1
        while True:
            number_loose = choice([1, 2, 4, 5])
            add_number = choice([0, 1, 2, 4, 5])
            print(f'\nLevel: {level}')
            print('\n1 room | 2 room | 3 room | 4 room | 5 room\n')
            print('Enter the room:')
            simple_rooms = input('>>> ')
            if simple_rooms.strip() == '0':
                print('\nAre you sure to leave the game?')
                while True:
                    ext_inp = input('>>> ').strip()
                    if ext_inp.lower() == 'yes' or ext_inp.lower() == 'yep' or ext_inp.lower() == \
'yeah' or ext_inp.strip() == '1':
                        print('\nUnfortunately!\nCome back!\n')
                        exit()
                    if ext_inp.lower() == 'no' or ext_inp.lower() == 'nope' or \
ext_inp.strip() == '0':
                        break
                    else:
                        print('Try again! Type "yes" or "no"')
            elif simple_rooms == '1' or simple_rooms == '2' or simple_rooms == '3' \
or simple_rooms == '4' or simple_rooms == '5' \
or simple_rooms == '1 room' or simple_rooms == '2 room' or simple_rooms == '2 room' \
or simple_rooms == '3 room' or simple_rooms == '4 room' or simple_rooms == '5 room':
                if not str(number_loose) in simple_rooms:
                    result += add_number
                    if add_number == 0:
                        print("\nYou've got nothing")
                    if level == 10:
                        print(f'\nYou are the winner!\n\nYour result is {result}\n\nDo you want to play again?')
                        while True:
                            ext_inp = input('>>> ').strip()
                            if ext_inp.lower() == 'yes' or ext_inp.lower() == 'yep' or \
ext_inp.lower() == 'yeah' or ext_inp.strip() == '1':
                                level = 0
                                result = 0
                                startgame('1')
                                break
                            if ext_inp.lower() == 'no' or ext_inp.lower() == 'nope' or \
ext_inp.strip() == '0':
                                print('\nUnfortunately!\nCome back!\n')
                                exit()
                            else:
                                print('Try again! Type "yes" or "no"')
                    else:
                        print(f"\nYou've got +{add_number}")
                    print(f'Result = {result}')
                    level += 1
                if str(number_loose) in simple_rooms:
                    print(f'You entered the wrong room: {simple_rooms}, so you lose!')
                    print(f'\nYour final result is {round(result, 1)}')
                    print('\nIf you want to play again, type "1", if not, type "0"!')
                    while True:
                        looser = input('>>> ').strip()
                        if looser == '1' or looser == '"1"' or looser == "'1'":
                            choosedifficulty(startgame('1'))
                        elif looser == '0' or looser == '"0"' or looser == "'0'":
                            choosedifficulty(startgame('0'))
                        else:
                            print('Try again! You can type only "1" or "0"')

            else:
                print('Try again!')

    def hardgame():
        '''
        Starts a hard game
        '''
        result = 0
        level = 1
        already = 0
        print('\nTo leave the game you can type "0"')
        while True:
            number_loose = choice([1, 2, 4, 5])
            add_number = choice([0, 1, 2, 4, 5])
            divide_res = result / 2
            for_minus_out = choice([1, 4, 5])
            minus_res = result - for_minus_out
            rand = choice([add_number, minus_res, divide_res])
            print(f'\nLevel: {level}')
            if level <= 3:
                print('\n1 room | 2 room | 3 room | 4 room | 5 room\n')
            elif level <= 10:
                if already == 0:
                    print(f"\nCongratulations! You've reached level {level}, so it'll be harder.\n\
The next deleting of the room will be from the level 11.\nGood Luck!")
                    already += 1
                print('\n1 room | 2 room | 3 room | 4 room\n')
            elif level <= 20:
                if already == 1:
                    print(f"\nCongratulations! You've reached level {level}, so it'll be harder.\n\
The next deleting of the room will be from the level 21.\nGood Luck!")
                    already += 1
                print('\n1 room | 2 room | 3 room\n')
            elif level > 20:
                if already == 2:
                    print(f"\nCongratulations! You've reached level {level}, so it'll be harder.\n\
You can try to set a record of this game!\nGood Luck!")
                    already += 1
                print('\n1 room | 2 room\n')
            print('Enter the room:')
            hard_rooms = input('>>> ')
            hard_bool = hard_rooms == '1' or hard_rooms == '2' or hard_rooms == '3' \
or hard_rooms == '1 room' or hard_rooms == '2 room' or hard_rooms == '3 room'
            if hard_rooms == '0':
                print('\nAre you sure to leave the game?')
                while True:
                    ext_inp = input('>>> ').strip()
                    if ext_inp.lower() == 'yes' or ext_inp.lower() == 'yep' or ext_inp.lower() == \
'yeah' or ext_inp.strip() == '1':
                        print('\nUnfortunately!\nCome back!\n')
                        exit()
                    if ext_inp.lower() == 'no' or ext_inp.lower() == 'nope' or \
ext_inp.strip() == '0':
                        break
                    else:
                        print('Try again! Type "yes" or "no"')
            elif ((hard_bool or hard_rooms == '4' or hard_rooms == '5' or \
hard_rooms == '4 room' or hard_rooms == '5 room') and already == 0) or \
((hard_bool or hard_rooms == '4' or hard_rooms == '4 room') \
and already == 1) or (hard_bool and already == 2) \
or ((hard_rooms == '1' or hard_rooms == '2' or hard_rooms == '1 room' or \
hard_rooms == '2 room') and already == 3):
                if not str(number_loose) in hard_rooms:
                    if rand == add_number == 0 or add_number == 0:
                        print("\nYou've got nothing.")
                    elif (rand == divide_res and already == 2) or (rand == divide_res and \
already == 3):
                        print("\nYou've got antibonus: your result will be divided by 2.")
                        result = divide_res
                    elif (rand == minus_res and already == 1) or (rand == minus_res and \
already == 2) or (rand == minus_res and already == 3):
                        result = minus_res
                        print(f"\nYou've got antibonus: {for_minus_out} will be subtracted from \
your results.")
                        if result < 0:
                            print('\nUnfortunately, your result was smaller than 0, maybe next \
time luck will be with You!\nIf you want to play again, type "1", if not, type "0"!')
                            while True:
                                looser = input('>>> ').strip()
                                if looser == '1' or looser == '"1"' or looser == "'1'":
                                    choosedifficulty(startgame('1'))
                                elif looser == '0' or looser == '"0"' or looser == "'0'":
                                    choosedifficulty(startgame('0'))
                                else:
                                    print('Try again! You can type only "1" or "0"')
                    else:
                        print(f"\nYou've got +{add_number}")
                        result += add_number
                    print(f'Result = {round(result, 1)}')
                    level += 1
                if str(number_loose) in hard_rooms:
                    print(f'You entered the wrong room: {hard_rooms}, so you lose!')
                    print(f'\nYour final result is {result}.')
                    print('\nIf you want to play again, type "1", if not, type "0"!')
                    while True:
                        looser = input('>>> ').strip()
                        if looser == '1' or looser == '"1"' or looser == "'1'":
                            choosedifficulty(startgame('1'))
                        elif looser == '0' or looser == '"0"' or looser == "'0'":
                            choosedifficulty(startgame('0'))
                        else:
                            print('Try again! You can type only "1" or "0".')
            else:
                print('\nTry again!')

    def choosedifficulty(difficulty: (str)) -> str:
        '''
        Starts chosen difficulty
        '''
        if difficulty == 'simple':
            simplegame()
        elif difficulty == 'hard':
            hardgame()

    choosedifficulty(startgame('1'))

if __name__ == '__main__':
    main()
