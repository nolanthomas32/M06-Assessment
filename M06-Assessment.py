print('\n Welcome to Wheel of Fortune!')
print("\n Let's start the game!")

from config import vowel_cost
from config import final_prize

import random
import time
import datetime
round_total = 0

players={0:{"round_total":round_total,"game_total":0,"name":""},
         1:{"round_total":round_total,"game_total":0,"name":""},
         2:{"round_total":round_total,"game_total":0,"name":""},
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
player_list = []
vowel_cost = 250


def read_dictionary_file():
    global dictionary
    f = open('DATA TXT Files\dictionary.txt')
    dictionary = f.read().split('\n')
    f.close()
    for word in range(0,len(dictionary)):
        dictionary_list.append(dictionary[word])
    # Read dictionary file in from dictionary file location
    # Store each word in a list.

  
def read_turn_txt_file():
    global turn_text
    f = open('DATA TXT Files\\turntext.txt')
    turn_text = f.read()
    f.close()      
    #read in turn intial turn status "message" from file

        
def read_final_round_txt_file():
    global final_round_text  
    f = open('DATA TXT FILES\\finalround.txt')
    final_round_text = f.read()
    f.close()
    #read in turn intial turn status "message" from file


def read_round_status_txt_file():
    global round_status
    f = open('DATA TXT Files\\roundstatus.txt')
    round_status = f.read()
    f.close()
    # read the round status  the Config roundstatusloc file location 


def read_wheel_txt_file():
    global wheel_list
    f = open('DATA TXT Files\wheeldata.txt')
    wheel_value = f.read().split('\n')
    f.close()
    for value in range(0,len(wheel_value)):
        wheel_list.append(wheel_value[value])
    # read the Wheel name from input using the Config wheelloc file location 

    
def get_player_info():
    global player_list
    for i in range(1,4):
        player_list.append([i])
    # read in player names from command prompt input


def game_setup():
    # Read in File dictionary
    # Read in Turn Text Files
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
    #choose random word from dictionary
    #make a list of the word with underscores instead of letters.

def countdown(s):
 
    # Calculate the total number of seconds
    total_seconds = s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
s = 5


def wof_round_setup():
    global players
    global round_word
    global blank_word
    global player_list
    global init_player
    global player_keys
    global player_num
    players.update({0:{"round_total":0,"game_total":round_winnings}})
    players.update({1:{"round_total":0,"game_total":round_winnings}})
    players.update({2:{"round_total":0,"game_total":round_winnings}})
    player_list = list(players.keys())
    player_keys = random.choice(player_list)
    init_player = [x+1 for x in {player_keys}]
    get_word()
    player_num = init_player
    return init_player
    # Set round total for each player = 0
    # Return the starting player number (random)
    # Use get_word function to retrieve the word and the underscore word (blank_word)


def wof_round_play(player_keys):
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
    while round_active is True:
        print("It's your turn Player!")
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
                            players.update({0:{"round_total":round_total}})
                            print(players)
                            continue
                        if "_" not in round_underscore_word:
                            print('The word has been guessed! The round is over!')
                            round_winnings = round_winnings + round_total + round_winning
                            players.update({0:{"round_total":0, "game_total":round_winnings}})
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
                        players.update({1:{"round_total":round_total}})
                        print(players)
                        still_in_turn = False
                        break
            continue
        if menu == 's':
            while still_in_turn is True:
                spin_value = random.choice(wheel_list)
                if spin_value == 'bankrupt':
                    round_total = 0
                    still_in_turn = False
                    players.update({0:{"round_total":{round_total}}})
                    print (f' Your spin is {spin_value}')
                    print(players)
                    continue
                if spin_value == 'lose_a_turn':
                    still_in_turn = False
                    print(f' Your spin is {spin_value}')
                    print(players)
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
                    # if guess in vowels:
                    #     print('Please guess a consonant.')
                        # continue
                    else:
                        if guess in round_word:
                            pos = [i for i in range(len(round_word)) if round_word.startswith(guess,i)]
                            guess = list(guess)
                            for i in pos:
                                round_underscore_word = round_underscore_word[:i] + guess + round_underscore_word[i + len(guess):]
                                print (f'The word: {round_underscore_word}')
                                round_total = round_total+consonant_value
                                players.update({0:{"round_total":round_total}})
                                print(players)
                                still_in_turn = False
                                continue
                            if "_" not in round_underscore_word:
                                print('The word has been guessed! The round is over!')
                                round_winnings = round_total + round_winning
                                players.update({0:{"round_total":0, "game_total":round_winnings}})
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
                            still_in_turn = False
                            break           
            continue
        if menu == 'g':
            user_guess = input('Input your guess for the word: ')
            if user_guess == round_word:
                print('Congratulations! You successfully guessed the word!')
                round_winnings = round_total + round_winning
                round_winning = round_winnings
                players.update({0:{"round_total":0, "game_total":round_winnings}})
                print(players)
                still_in_turn = False
                round_active = False
                break
            if user_guess != round_word:
                print('Sorry, that guess was incorrect...')
                still_in_turn = False
            continue
        else:
            print("Please select a valid menu option\n")
            continue
        
        # Get random value for wheellist
        # Check for bankrupcy, and take action.
        # Check for lose turn
        # Get amount from wheel if not lose turn or bankruptcy
        # Ask user for letter guess
        # Use guessletter function to see if guess is in word, and return count
        # Change player round total if they guess right. 
            
    return round_winning

def final_round(player_keys):
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
    wof_round_play(player_list)
    wof_round_play(player_list)
    final_round(player_list)

wof_game()