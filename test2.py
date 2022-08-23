print('\n Welcome to Wheel of Fortune!')
print("\n Let's start the game!")

from config import vowel_cost
from config import final_prize
from itertools import cycle

import random
import time
import datetime
round_total = 0

players={1:{"round_total":round_total,"game_total":0},
         2:{"round_total":round_total,"game_total":0},
         3:{"round_total":round_total,"game_total":0},
        }

round_num = 0
round_winning = 0
round_winnings = 0
dictionary_list = []
turn_text = ""
wheel_list = []
round_word = ""
blank_word = []
vowels = {"a", "e", "i", "o", "u"}
consonants = {"b", "c", "d", "f" "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}
round_status = ""
final_round_text = ""
player_list = [1,2,3]
vowel_cost = 250
init_player = cycle(player_list)
random_player = random.choice(player_list)

def next_player():
    return next(init_player)

def read_dictionary_file():
    global dictionary
    f = open('DATA TXT Files\dictionary.txt')
    dictionary = f.read().split('\n')
    f.close()
    for word in range(0,len(dictionary)):
        dictionary_list.append(dictionary[word])

  
def read_turn_txt_file():
    global turn_text
    f = open('DATA TXT Files\\turntext.txt')
    turn_text = f.read()
    f.close()      


        
def read_final_round_txt_file():
    global final_round_text  
    f = open('DATA TXT FILES\\finalround.txt')
    final_round_text = f.read()
    f.close()


def read_round_status_txt_file():
    global round_status
    f = open('DATA TXT Files\\roundstatus.txt')
    round_status = f.read()
    f.close()



def read_wheel_txt_file():
    global wheel_list
    f = open('DATA TXT Files\wheeldata.txt')
    wheel_value = f.read().split('\n')
    f.close()
    for value in range(0,len(wheel_value)):
        wheel_list.append(wheel_value[value])


    
def get_player_info():
    global player_list
    for i in range(1,4):
        player_list.append([i])


def game_setup():
    global turn_text
    global dictionary
        
    read_dictionary_file()
    read_turn_txt_file()
    read_wheel_txt_file()
    get_player_info()
    read_round_status_txt_file()
    read_final_round_txt_file() 
    
def get_word():
    global dictionary
    global round_word
    global round_underscore_word
    round_word = random.choice(dictionary_list)
    round_underscore_word = '_ ' * len(round_word)
    round_underscore_word = round_underscore_word.split(' ')
    return round_word, round_underscore_word

def countdown(s):
    total_seconds = s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
s = 5


def wof_round_setup():
    global players
    global round_word
    global blank_word
    global player_list
    global random_player
    players.update({1:{"round_total":0,"game_total":round_winnings}})
    players.update({2:{"round_total":0,"game_total":round_winnings}})
    players.update({3:{"round_total":0,"game_total":round_winnings}})
    random_player = random.choice(player_list)
    get_word()


def wof_round_play(init_player):
    global wheel_list
    global players
    global vowels
    global spin_value
    global round_underscore_word
    global round_total
    global consonant_value
    global round_winning
    round_total = 0
    # game_setup()
    wof_round_setup()
    round_active = True
    while round_active is True:
        print(f"It's your turn Player {init_player}!")
        if init_player == [1]:
            player_list = next_player()
            init_player = player_list
        if init_player == [2]:
            player_list = next_player()
            init_player = player_list
        if init_player == [3]:
            player_list = next_player()
            init_player = player_list
        print("================================")
        print("s: Spin the Wheel")
        print("b: Buy a vowel")
        print("g: guess the word")
        menu = input("What would you like to do? ")
        print(round_word)
        still_in_turn = True
        if menu == "b":
            while still_in_turn is True:
                print('Vowels cost 250.')
                vowel_guess = input('What vowel would you like to buy? ')
                if vowel_guess not in vowels:
                    print('Please guess a vowel')
                else:
                    if vowel_guess in round_word:
                        pos = [i for i in range(len(round_word)) if round_word.startswith(vowel_guess,i)]
                        vowel_guess = list(vowel_guess)
                        for i in pos:
                            round_underscore_word = round_underscore_word[:i] + vowel_guess + round_underscore_word[i + len(vowel_guess):]
                            print (f'The word: {round_underscore_word}')
                            round_total = round_total - vowel_cost
                            # THIS WILL BE A BIG CHANGE! MARKING OUT TO SEE IF IT WILL WORK!!!!!!!
                            if init_player == 1:
                                players.update({1:{"round_total":round_total}})
                            if init_player == 2:
                                players.update({2:{"round_total":round_total}})
                            if init_player == 3:
                                players.update({3:{"round_total":round_total}})                             
                            print(players)
                            continue
                        if "_" not in round_underscore_word:
                            print('The word has been guessed! The round is over!')
                            round_winnings = round_total + round_winning
                            round_winning = round_winnings
                            # THIS WILL BE A BIG CHANGE! MARKING OUT TO SEE IF IT WILL WORK!!!!!!!
                            if init_player == 1:
                                players.update({1:{"round_total":0, "game_total":round_winnings}})
                            if init_player == 2:
                                players.update({1:{"round_total":0, "game_total":round_winnings}})
                            if init_player == 3:
                                players.update({3:{"round_total":0, "game_total":round_winnings}})
                            print('The word has been guessed! The round is over!')
                            print(players)
                            round_active = False
                            still_in_turn = False
                            break
                        else:
                            print (f'The word: {round_underscore_word}')
                            still_in_turn = False
                            break
                    if vowel_guess not in round_word:
                        print('That guess is incorrect\n')
                        print (f'The word: {round_underscore_word}')
                        round_total = round_total - vowel_cost
                        # THIS WILL BE A BIG CHANGE! MARKING OUT TO SEE IF IT WILL WORK!!!!!!!
                        if init_player == 1:
                            players.update({1:{"round_total":round_total}})
                        if init_player == 2:
                            players.update({2:{"round_total":round_total}})
                        if init_player == 3:
                            players.update({3:{"round_total":round_total}})       
                        print(players)
                        #TESTING FOR INIT PLAYER CYCLE
                        player_list = next_player()
                        init_player = player_list
                        if init_player == [1]:
                            player_list = next_player()
                            init_player = player_list
                        if init_player == [2]:
                            player_list = next_player()
                            init_player = player_list
                        if init_player == [3]:
                            player_list = next_player()
                            init_player = player_list
                        still_in_turn = False
                        break
            continue
        if menu == 's':
            while still_in_turn is True:
                spin_value = random.choice(wheel_list)
                if spin_value == 'bankrupt':
                    round_total = 0
                    still_in_turn = False
                    # THIS WILL BE A BIG CHANGE! MARKING OUT TO SEE IF IT WILL WORK!!!!!!!
                    if init_player == 1:
                        players.update({1:{"round_total":round_total}})
                    if init_player == 2:
                        players.update({2:{"round_total":round_total}})
                    if init_player == 3:
                        players.update({3:{"round_total":round_total}})   
                    print (f' Your spin is {spin_value}')
                    print(players)
                    #TESTING FOR INIT PLAYER CYCLE
                    player_list = next_player()
                    init_player = player_list
                    if init_player == [1]:
                        player_list = next_player()
                        init_player = player_list
                    if init_player == [2]:
                        player_list = next_player()
                        init_player = player_list
                    if init_player == [3]:
                        player_list = next_player()
                        init_player = player_list         
                    continue
                if spin_value == 'lose_a_turn':
                    still_in_turn = False
                    print(f' Your spin is {spin_value}')
                    print(players)
                    #TESTING FOR INIT PLAYER CYCLE
                    player_list = next_player()
                    init_player = player_list
                    if init_player == [1]:
                        player_list = next_player()
                        init_player = player_list
                    if init_player == [2]:
                        player_list = next_player()
                        init_player = player_list
                    if init_player == [3]:
                        player_list = next_player()
                        init_player = player_list                    
                    continue
                else:
                    consonant_value = int(spin_value)
                    print(f' Your spin is {spin_value}')
                    guess = input('Guess your letter: ')
                    if guess.isalpha() is False:
                        print('Please guess a letter!')
                    if guess in vowels:
                        print('Please guess a consonant.')
                        continue
                    else:
                        if guess in round_word:
                            pos = [i for i in range(len(round_word)) if round_word.startswith(guess,i)]
                            guess = list(guess)
                            for i in pos:
                                round_underscore_word = round_underscore_word[:i] + guess + round_underscore_word[i + len(guess):]
                                print (f'The word: {round_underscore_word}')
                                round_total = round_total+consonant_value
                                # THIS WILL BE A BIG CHANGE! MARKING OUT TO SEE IF IT WILL WORK!!!!!!!
                                if init_player == 1:
                                    players.update({1:{"round_total":round_total}})
                                if init_player == 2:
                                    players.update({2:{"round_total":round_total}})
                                if init_player == 3:
                                    players.update({3:{"round_total":round_total}})   
                                print(players)
                                still_in_turn = False
                                continue
                            if "_" not in round_underscore_word:
                                print('The word has been guessed! The round is over!')
                                round_winnings = round_total + round_winning
                                # THIS WILL BE A BIG CHANGE! MARKING OUT TO SEE IF IT WILL WORK!!!!!!!
                                if init_player == 1:
                                    players.update({1:{"round_total":0, "game_total":round_winnings}})
                                if init_player == 2:
                                    players.update({1:{"round_total":0, "game_total":round_winnings}})
                                if init_player == 3:
                                    players.update({3:{"round_total":0, "game_total":round_winnings}})
                                print(players)
                                still_in_turn = False
                                round_active = False
                                break
                            else:
                                print (f'The word: {round_underscore_word}')
                                print(players)
                                still_in_turn = False
                                break
                        if guess not in round_word:
                            print('That guess is incorrect\n')
                            print(players)
                            #TESTING FOR INIT PLAYER CYCLE
                            player_list = next_player()
                            init_player = player_list
                            if init_player == [1]:
                                player_list = next_player()
                                init_player = player_list
                            if init_player == [2]:
                                player_list = next_player()
                                init_player = player_list
                            if init_player == [3]:
                                player_list = next_player()
                                init_player = player_list
                            still_in_turn = False
                            break     
            continue
        if menu == 'g':
            user_guess = input('Input your guess for the word: ')
            if user_guess == round_word:
                print('Congratulations! You successfully guessed the word!')
                round_winnings = round_total + round_winning
                round_winning = round_winnings
                # THIS WILL BE A BIG CHANGE! MARKING OUT TO SEE IF IT WILL WORK!!!!!!!
                if init_player == 1:
                    players.update({1:{"round_total":0, "game_total":round_winnings}})
                if init_player == 2:
                    players.update({2:{"round_total":0, "game_total":round_winnings}})
                if init_player == 3:
                    players.update({3:{"round_total":0, "game_total":round_winnings}})
                print(players)
                still_in_turn = False
                round_active = False
                break
            if user_guess != round_word:
                print('Sorry, that guess was incorrect...')
                still_in_turn = False
                print(players)
                #TESTING FOR INIT PLAYER CYCLE
                player_list = next_player()
                init_player = player_list
                if init_player == [1]:
                    player_list = next_player()
                    init_player = player_list
                if init_player == [2]:
                    player_list = next_player()
                    init_player = player_list
                if init_player == [3]:
                    player_list = next_player()
                    init_player = player_list                
            continue
        else:
            print("Please select a valid menu option\n")
            continue          
    return round_winning

def final_round(init_player):
    global wheel_list
    global players
    global vowels
    global spin_value
    global round_underscore_word
    global round_total
    global consonant_value
    global round_winning
    round_total = 0
    game_setup()
    wof_round_setup()
    round_active = True
    print("Welcome to the Bonus Round!")
    print(round_word)
    pre_fill = 'r'
    if pre_fill in round_word:
        pos = [i for i in range(len(round_word)) if round_word.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            round_underscore_word = round_underscore_word[:i] + pre_fill + round_underscore_word[i + len(pre_fill):]
            print (f'The word: {round_underscore_word}')
    pre_fill = 's'
    if pre_fill in round_word:
        pos = [i for i in range(len(round_word)) if round_word.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            round_underscore_word = round_underscore_word[:i] + pre_fill + round_underscore_word[i + len(pre_fill):]
            print (f'The word: {round_underscore_word}')
    pre_fill = 't'
    if pre_fill in round_word:
        pos = [i for i in range(len(round_word)) if round_word.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            round_underscore_word = round_underscore_word[:i] + pre_fill + round_underscore_word[i + len(pre_fill):]
            print (f'The word: {round_underscore_word}')
    pre_fill = 'l'
    if pre_fill in round_word:
        pos = [i for i in range(len(round_word)) if round_word.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            round_underscore_word = round_underscore_word[:i] + pre_fill + round_underscore_word[i + len(pre_fill):]
            print (f'The word: {round_underscore_word}')
    pre_fill = 'n'
    if pre_fill in round_word:
        pos = [i for i in range(len(round_word)) if round_word.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            round_underscore_word = round_underscore_word[:i] + pre_fill + round_underscore_word[i + len(pre_fill):]
            print (f'The word: {round_underscore_word}')
    pre_fill = 'e'
    if pre_fill in round_word:
        pos = [i for i in range(len(round_word)) if round_word.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            round_underscore_word = round_underscore_word[:i] + pre_fill + round_underscore_word[i + len(pre_fill):]
            print (f'The word: {round_underscore_word}')
    while round_active is True:
        guess = input('Guess your 1st consonant: ')
        if guess.isalpha() is False:
            print('Please guess a letter!')
            continue
        if guess in vowels:
            print('Please guess a consonant.')
            continue
        else:
            if guess in round_word:
                pos = [i for i in range(len(round_word)) if round_word.startswith(guess,i)]
                guess = list(guess)
                for i in pos:
                    round_underscore_word = round_underscore_word[:i] + guess + round_underscore_word[i + len(guess):]
                    print (f'The word: {round_underscore_word}')
                    break
        guess = input('Guess your 2nd consonant: ')
        if guess.isalpha() is False:
            print('Please guess a letter!')
            continue
        if guess in vowels:
            print('Please guess a consonant.')
            continue
        else:
            if guess in round_word:
                pos = [i for i in range(len(round_word)) if round_word.startswith(guess,i)]
                guess = list(guess)
                for i in pos:
                    round_underscore_word = round_underscore_word[:i] + guess + round_underscore_word[i + len(guess):]
                    print (f'The word: {round_underscore_word}')
                    break
        guess = input('Guess your 3rd consonant: ')
        if guess.isalpha() is False:
            print('Please guess a letter!')
            continue
        if guess in vowels:
            print('Please guess a consonant.')
            continue
        else:
            if guess in round_word:
                pos = [i for i in range(len(round_word)) if round_word.startswith(guess,i)]
                guess = list(guess)
                for i in pos:
                    round_underscore_word = round_underscore_word[:i] + guess + round_underscore_word[i + len(guess):]
                    print (f'The word: {round_underscore_word}')
                    break
        guess = input('Guess your vowel: ')
        if guess.isalpha() is False:
            print('Please guess a letter!')
            continue
        if guess not in vowels:
            print('Please guess a vowel.')
            continue
        else:
            if guess in round_word:
                pos = [i for i in range(len(round_word)) if round_word.startswith(guess,i)]
                guess = list(guess)
                for i in pos:
                    round_underscore_word = round_underscore_word[:i] + guess + round_underscore_word[i + len(guess):]
                    print (f'The word: {round_underscore_word}')
                    continue
        break
    timer = True
    while timer is True:
        final_guess =input('You have 5 seconds. Make your final guess now: ')
        countdown(int(s))
        if final_guess == round_word:
            print(f'Congratulations!! You\'ve won the game and your bonus prize is {final_prize}')
            print(f"You're grand total is: ${final_prize + round_winning}")
            timer = False
            break
        if final_guess != round_word:
            print("Sorry. That was the wrong word.. Better luck next time!")
            timer = False
            break
        else:
            print("Sorry. Time's up... Better luck next time!")
    print('Thanks for playing!')



def wof_game():
    game_setup()
    wof_round_play(random_player)
    wof_round_play(random_player)
    final_round(random_player)

wof_game()
print(random_player)
print(type(init_player))