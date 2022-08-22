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
round_total = 0

players={0:{"roundtotal":round_total,"gametotal":0,"name":""},
         1:{"roundtotal":round_total,"gametotal":0,"name":""},
         2:{"roundtotal":round_total,"gametotal":0,"name":""},
        }

roundNum = 0
round_winnings = 0
dictionary_list = []
turntext = ""
wheel_list = []
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
roundstatus = ""
finalroundtext = ""
player_list = []




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
    global roundstatus
    f = open('DATA TXT Files\\roundstatus.txt')
    roundstatus = f.read()
    f.close()
    # read the round status  the Config roundstatusloc file location 


def readWheelTxtFile():
    global wheel_list
    f = open('DATA TXT Files\wheeldata.txt')
    wheelvalue = f.read().split('\n')
    f.close()
    for value in range(0,len(wheelvalue)):
        wheel_list.append(wheelvalue[value])
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

def wofRoundSetup():
    global players
    global roundWord
    global blankWord
    global player_list
    global initPlayer
    global player_keys
    players.update({0:{"roundtotal":0,"gametotal":round_winnings}})
    players.update({1:{"roundtotal":0,"gametotal":round_winnings}})
    players.update({2:{"roundtotal":0,"gametotal":round_winnings}})
    player_list = list(players.keys())
    player_keys = random.choice(player_list)
    initPlayer = [x+1 for x in {player_keys}]
    getWord()
    return initPlayer
    # Set round total for each player = 0
    # Return the starting player number (random)
    # Use getWord function to retrieve the word and the underscore word (blankWord)

def spinWheel(playerNum):
    global wheel_list
    global players
    global vowels
    global spin_value
    global roundUnderscoreWord
    global round_total
    global consonant_value
    
    stillinTurn = True
    while stillinTurn is True:
        spin_value = random.choice(wheel_list)
        if spin_value == 'bankrupt':
            players.update({"roundtotal":0})
            stillinTurn = False
            print (spin_value)
            continue
        if spin_value == 'lose_a_turn':
            stillinTurn = False
            print(spin_value)
            continue
        else:
            consonant_value = int(spin_value)
            print(spin_value)
            guess = input('Guess your letter: ')
            if guess.isalpha() is False:
                print('Please guess a letter!')
                continue
            else:
                print(roundWord)
                if guess in roundWord:
                    pos = [i for i in range(len(roundWord)) if roundWord.startswith(guess,i)]
                    guess = list(guess)
                    for i in pos:
                        roundUnderscoreWord = roundUnderscoreWord[:i] + guess + roundUnderscoreWord[i + len(guess):]
                        print (f'The word: {roundUnderscoreWord}')
                        round_total = round_total+consonant_value
                        players.update({0:{"roundtotal":round_total, "gametotal":round_winnings}})
                        continue
                    if "_" not in roundUnderscoreWord:
                        print('The word has been guessed! The round is over!')
                        break
                else:
                    print (f'The word: {roundUnderscoreWord}')
                    stillinTurn = False
    
    # Get random value for wheellist
    # Check for bankrupcy, and take action.
    # Check for lose turn
    # Get amount from wheel if not lose turn or bankruptcy
    # Ask user for letter guess
    # Use guessletter function to see if guess is in word, and return count
    # Change player round total if they guess right. 
        
    return stillinTurn

gameSetup()
wofRoundSetup()
spinWheel(player_keys)
print(players)


# def guessletter(letter, playerNum): 
#     global players
#     global blankWord
#     # parameters:  take in a letter guess and player number
#     # Change position of found letter in blankWord to the letter instead of underscore 
#     # return goodGuess= true if it was a correct guess
#     # return count of letters in word. 
#     # ensure letter is a consonate.
    
#     return goodGuess, count

# def buyVowel(playerNum):
#     global players
#     global vowels
    
#     # Take in a player number
#     # Ensure player has 250 for buying a vowelcost
#     # Use guessLetter function to see if the letter is in the file
#     # Ensure letter is a vowel
#     # If letter is in the file let goodGuess = True
    
#     return goodGuess      
        
# def guessWord(playerNum):
#     global players
#     global blankWord
#     global roundWord
    
#     # Take in player number
#     # Ask for input of the word and check if it is the same as wordguess
#     # Fill in blankList with all letters, instead of underscores if correct 
#     # return False ( to indicate the turn will finish)  
    
#     return False
    
    
# def wofTurn(playerNum):  
#     global roundWord
#     global blankWord
#     global turntext
#     global players

#     # take in a player number. 
#     # use the string.format method to output your status for the round
#     # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
#     # Keep doing all turn activity for a player until they guess wrong
#     # Do all turn related activity including update roundtotal 
    
#     stillinTurn = True
#     while stillinTurn:
        
#         # use the string.format method to output your status for the round
#         # Get user input S for spin, B for buy a vowel, G for guess the word
                
#         if(choice.strip().upper() == "S"):
#             stillinTurn = spinWheel(playerNum)
#         elif(choice.strip().upper() == "B"):
#             stillinTurn = buyVowel(playerNum)
#         elif(choice.upper() == "G"):
#             stillinTurn = guessWord(playerNum)
#         else:
#             print("Not a correct option")        
    
#     # Check to see if the word is solved, and return false if it is,
#     # Or otherwise break the while loop of the turn.     


# def wofRound():
#     global players
#     global roundWord
#     global blankWord
#     global roundstatus
#     initPlayer = wofRoundSetup()
    
#     # Keep doing things in a round until the round is done ( word is solved)
#         # While still in the round keep rotating through players
#         # Use the wofTurn fuction to dive into each players turn until their turn is done.
    
#     # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.

# def wofFinalRound():
#     global roundWord
#     global blankWord
#     global finalroundtext
#     winplayer = 0
#     amount = 0
    
#     # Find highest gametotal player.  They are playing.
#     # Print out instructions for that player and who the player is.
#     # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
#     # Use the guessletter function to check for {'R','S','T','L','N','E'}
#     # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
#     # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
#     # Print out the current blankWord again
#     # Remember guessletter should fill in the letters with the positions in blankWord
#     # Get user to guess word
#     # If they do, add finalprize and gametotal and print out that the player won 


# def main():
#     gameSetup()    

#     for i in range(0,maxrounds):
#         if i in [0,1]:
#             wofRound()
#         else:
#             wofFinalRound()

# if __name__ == "__main__":
#     main()
    
    
