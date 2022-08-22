print('\n Welcome to Wheel of Fortune!')
print("\n Let's start the game!")

from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize
from config import finalRoundTextLoc

import random
import time
import datetime
round_total = 0

players={0:{"roundtotal":round_total,"gametotal":0,"name":""},
         1:{"roundtotal":round_total,"gametotal":0,"name":""},
         2:{"roundtotal":round_total,"gametotal":0,"name":""},
        }

roundNum = 0
round_winning = 0
round_winnings = 0
dictionary_list = []
turntext = ""
wheel_list = []
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
consonants = {"b", "c", "d", "f" "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}
round_status = ""
finalroundtext = ""
player_list = []
vowel_cost = 250


def readDictionaryFile():
    global dictionary
    f = open('DATA TXT Files\dictionary.txt')
    dictionary = f.read().split('\n')
    f.close()
    for word in range(0,len(dictionary)):
        dictionary_list.append(dictionary[word])
    # Read dictionary file in from dictionary file location
    # Store each word in a list.

  
def readTurnTxtFile():
    global turntext
    f = open('DATA TXT Files\\turntext.txt')
    turntext = f.read()
    f.close()      
    #read in turn intial turn status "message" from file

        
def readFinalRoundTxtFile():
    global finalroundtext  
    f = open('DATA TXT FILES\\finalround.txt')
    finalroundtext = f.read()
    f.close()
    #read in turn intial turn status "message" from file


def readRoundStatusTxtFile():
    global round_status
    f = open('DATA TXT Files\\roundstatus.txt')
    round_status = f.read()
    f.close()
    # read the round status  the Config roundstatusloc file location 


def readWheelTxtFile():
    global wheel_list
    f = open('DATA TXT Files\wheeldata.txt')
    wheel_value = f.read().split('\n')
    f.close()
    for value in range(0,len(wheel_value)):
        wheel_list.append(wheel_value[value])
    # read the Wheel name from input using the Config wheelloc file location 

    
def getPlayerInfo():
    global player_list
    for i in range(1,4):
        player_list.append([i])
    # read in player names from command prompt input


def gameSetup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turntext
    global dictionary
        
    readDictionaryFile()
    readTurnTxtFile()
    readWheelTxtFile()
    getPlayerInfo()
    readRoundStatusTxtFile()
    readFinalRoundTxtFile() 
    
def getWord():
    global dictionary
    global roundWord
    global roundUnderscoreWord
    roundWord = random.choice(dictionary_list)
    roundUnderscoreWord = '_ ' * len(roundWord)
    roundUnderscoreWord = roundUnderscoreWord.split(' ')
    return roundWord, roundUnderscoreWord
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


def wofRoundSetup():
    global players
    global roundWord
    global blankWord
    global player_list
    global initPlayer
    global player_keys
    global playerNum
    players.update({0:{"roundtotal":0,"gametotal":round_winnings}})
    players.update({1:{"roundtotal":0,"gametotal":round_winnings}})
    players.update({2:{"roundtotal":0,"gametotal":round_winnings}})
    player_list = list(players.keys())
    player_keys = random.choice(player_list)
    initPlayer = [x+1 for x in {player_keys}]
    getWord()
    playerNum = initPlayer
    return initPlayer
    # Set round total for each player = 0
    # Return the starting player number (random)
    # Use getWord function to retrieve the word and the underscore word (blankWord)


def spinWheel(player_keys):
    global wheel_list
    global players
    global vowels
    global spin_value
    global roundUnderscoreWord
    global round_total
    global consonant_value
    global round_winning
    round_total = 0
    gameSetup()
    wofRoundSetup()
    round_active = True
    while round_active is True:
        print("It's your turn Player!")
        print("================================")
        print("s: Spin the Wheel")
        print("b: Buy a vowel")
        print("g: guess the word")
        menu = input("What would you like to do? ")
        print(roundWord)
        stillinTurn = True
        if menu == "b":
            while stillinTurn is True:
                print('Vowels cost 250.')
                vowel_guess = input('What vowel would you like to buy? ')
                if vowel_guess not in vowels:
                    print('Please guess a vowel')
                else:
                    if vowel_guess in roundWord:
                        pos = [i for i in range(len(roundWord)) if roundWord.startswith(vowel_guess,i)]
                        vowel_guess = list(vowel_guess)
                        for i in pos:
                            roundUnderscoreWord = roundUnderscoreWord[:i] + vowel_guess + roundUnderscoreWord[i + len(vowel_guess):]
                            print (f'The word: {roundUnderscoreWord}')
                            round_total = round_total - vowelcost
                            players.update({0:{"roundtotal":round_total}})
                            print(players)
                            continue
                        if "_" not in roundUnderscoreWord:
                            print('The word has been guessed! The round is over!')
                            round_winnings = round_winnings + round_total + round_winning
                            players.update({0:{"roundtotal":0, "gametotal":round_winnings}})
                            print('The word has been guessed! The round is over!')
                            print(players)
                            round_active = False
                            stillinTurn = False
                            break
                        else:
                            print (f'The word: {roundUnderscoreWord}')
                            stillinTurn = False
                            break
                    if vowel_guess not in roundWord:
                        print('That guess is incorrect\n')
                        print (f'The word: {roundUnderscoreWord}')
                        round_total = round_total - vowelcost
                        players.update({1:{"roundtotal":round_total}})
                        print(players)
                        stillinTurn = False
                        break
            continue
        if menu == 's':
            while stillinTurn is True:
                spin_value = random.choice(wheel_list)
                if spin_value == 'bankrupt':
                    stillinTurn = False
                    players.update({0:{"roundtotal":0}})
                    print (f' Your spin is {spin_value}')
                    print(players)
                    continue
                if spin_value == 'lose_a_turn':
                    stillinTurn = False
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
                        if guess in roundWord:
                            pos = [i for i in range(len(roundWord)) if roundWord.startswith(guess,i)]
                            guess = list(guess)
                            for i in pos:
                                roundUnderscoreWord = roundUnderscoreWord[:i] + guess + roundUnderscoreWord[i + len(guess):]
                                print (f'The word: {roundUnderscoreWord}')
                                round_total = round_total+consonant_value
                                players.update({0:{"roundtotal":round_total}})
                                print(players)
                                stillinTurn = False
                                continue
                            if "_" not in roundUnderscoreWord:
                                print('The word has been guessed! The round is over!')
                                round_winnings = round_total + round_winning
                                players.update({0:{"roundtotal":0, "gametotal":round_winnings}})
                                print(players)
                                stillinTurn = False
                                round_active = False
                                break
                            else:
                                print (f'The word: {roundUnderscoreWord}')
                                print(players)
                                stillinTurn = False
                                break
                        if guess not in roundWord:
                            print('That guess is incorrect\n')
                            print(players)
                            stillinTurn = False
                            break           
            continue
        if menu == 'g':
            user_guess = input('Input your guess for the word: ')
            if user_guess == roundWord:
                print('Congratulations! You successfully guessed the word!')
                round_winnings = round_total + round_winning
                round_winning = round_winnings
                players.update({0:{"roundtotal":0, "gametotal":round_winnings}})
                print(players)
                stillinTurn = False
                round_active = False
                break
            if user_guess != roundWord:
                print('Sorry, that guess was incorrect...')
                stillinTurn = False
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
    global roundUnderscoreWord
    global round_total
    global consonant_value
    global round_winning
    round_total = 0
    gameSetup()
    wofRoundSetup()
    round_active = True
    print("Welcome to the Bonus Round!")
    print(roundWord)
    pre_fill = 'r'
    if pre_fill in roundWord:
        pos = [i for i in range(len(roundWord)) if roundWord.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            roundUnderscoreWord = roundUnderscoreWord[:i] + pre_fill + roundUnderscoreWord[i + len(pre_fill):]
            print (f'The word: {roundUnderscoreWord}')
    pre_fill = 's'
    if pre_fill in roundWord:
        pos = [i for i in range(len(roundWord)) if roundWord.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            roundUnderscoreWord = roundUnderscoreWord[:i] + pre_fill + roundUnderscoreWord[i + len(pre_fill):]
            print (f'The word: {roundUnderscoreWord}')
    pre_fill = 't'
    if pre_fill in roundWord:
        pos = [i for i in range(len(roundWord)) if roundWord.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            roundUnderscoreWord = roundUnderscoreWord[:i] + pre_fill + roundUnderscoreWord[i + len(pre_fill):]
            print (f'The word: {roundUnderscoreWord}')
    pre_fill = 'l'
    if pre_fill in roundWord:
        pos = [i for i in range(len(roundWord)) if roundWord.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            roundUnderscoreWord = roundUnderscoreWord[:i] + pre_fill + roundUnderscoreWord[i + len(pre_fill):]
            print (f'The word: {roundUnderscoreWord}')
    pre_fill = 'n'
    if pre_fill in roundWord:
        pos = [i for i in range(len(roundWord)) if roundWord.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            roundUnderscoreWord = roundUnderscoreWord[:i] + pre_fill + roundUnderscoreWord[i + len(pre_fill):]
            print (f'The word: {roundUnderscoreWord}')
    pre_fill = 'e'
    if pre_fill in roundWord:
        pos = [i for i in range(len(roundWord)) if roundWord.startswith(pre_fill,i)]
        pre_fill = list(pre_fill)
        for i in pos:
            roundUnderscoreWord = roundUnderscoreWord[:i] + pre_fill + roundUnderscoreWord[i + len(pre_fill):]
            print (f'The word: {roundUnderscoreWord}')
    while round_active is True:
        guess = input('Guess your 1st consonant: ')
        if guess.isalpha() is False:
            print('Please guess a letter!')
            continue
        if guess in vowels:
            print('Please guess a consonant.')
            continue
        else:
            if guess in roundWord:
                pos = [i for i in range(len(roundWord)) if roundWord.startswith(guess,i)]
                guess = list(guess)
                for i in pos:
                    roundUnderscoreWord = roundUnderscoreWord[:i] + guess + roundUnderscoreWord[i + len(guess):]
                    print (f'The word: {roundUnderscoreWord}')
                    break
        guess = input('Guess your 2nd consonant: ')
        if guess.isalpha() is False:
            print('Please guess a letter!')
            continue
        if guess in vowels:
            print('Please guess a consonant.')
            continue
        else:
            if guess in roundWord:
                pos = [i for i in range(len(roundWord)) if roundWord.startswith(guess,i)]
                guess = list(guess)
                for i in pos:
                    roundUnderscoreWord = roundUnderscoreWord[:i] + guess + roundUnderscoreWord[i + len(guess):]
                    print (f'The word: {roundUnderscoreWord}')
                    break
        guess = input('Guess your 3rd consonant: ')
        if guess.isalpha() is False:
            print('Please guess a letter!')
            continue
        if guess in vowels:
            print('Please guess a consonant.')
            continue
        else:
            if guess in roundWord:
                pos = [i for i in range(len(roundWord)) if roundWord.startswith(guess,i)]
                guess = list(guess)
                for i in pos:
                    roundUnderscoreWord = roundUnderscoreWord[:i] + guess + roundUnderscoreWord[i + len(guess):]
                    print (f'The word: {roundUnderscoreWord}')
                    break
        guess = input('Guess your vowel: ')
        if guess.isalpha() is False:
            print('Please guess a letter!')
            continue
        if guess not in vowels:
            print('Please guess a vowel.')
            continue
        else:
            if guess in roundWord:
                pos = [i for i in range(len(roundWord)) if roundWord.startswith(guess,i)]
                guess = list(guess)
                for i in pos:
                    roundUnderscoreWord = roundUnderscoreWord[:i] + guess + roundUnderscoreWord[i + len(guess):]
                    print (f'The word: {roundUnderscoreWord}')
                    continue
        break
    timer = True
    while timer is True:
        final_guess =input('You have 5 seconds. Make your final guess now: ')
        countdown(int(s))
        if final_guess == roundWord:
            print(f'Congratulations!! You\'ve won the game and your bonus prize is {finalprize}')
            print(f"You're grand total is: ${finalprize + round_winning}")
            timer = False
            break
        if final_guess != roundWord:
            print("Sorry. That was the wrong word.. Better luck next time!")
            timer = False
            break
        else:
            print("Sorry. Time's up... Better luck next time!")
    print('Thanks for playing!')



def wof_game():
    spinWheel(player_list)
    spinWheel(player_list)
    final_round(player_list)

wof_game()