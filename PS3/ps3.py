# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1,'*':0, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist
word_list = load_words()
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    points_letters = 0
    word = word.lower()
    
    for letter in word :
        points_letters += SCRABBLE_LETTER_VALUES[letter]
    
    if ((7 * len(word) - 3 * ( n- len(word))) > 1):
        return points_letters * (7 * len(word) - 3 * ( n- len(word)))
    else :
        return points_letters

#print(get_word_score("it", 7))        
    
    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#


#display_hand({"h":4, "g" :8 , "o":4})

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={"*":1,}
    num_vowels = int(math.ceil(n / 3)-1 )

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n-1):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand


# Problem #2: Update a hand by removing letters

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    new_hand = {}
    letters = get_frequency_dict(word)
    for keys in hand :
                            
        new_hand [keys] = hand[keys]
        
            
    for letter in letters :        
           
        if (letter in new_hand):
            new_hand[letter]-=letters[letter] 
           
            if (new_hand[letter] <= 0)  :  
                del(new_hand[letter])
    return new_hand


              
def put_ast (word,position):
    ast_word = ""
    counter = 0
    for letter in word:
        if (counter == position):
            ast_word += "*"
        else :
            ast_word += letter
        counter += 1    
    return ast_word

#print (put_ast("banano" , 17))            

def is_word_in (word , hand):
    
    new_hand = {}
    letters = get_frequency_dict(word)
    for keys in hand :
                            
        new_hand [keys] = hand[keys]
        
            
    for letter in new_hand :        
           
        if (letter in letters):
            letters[letter] -= new_hand[letter] 
            
            if (letters[letter] <= 0)  :                  
                del(letters[letter])
                
    if (letters == {}):            
        return True
    
    return False
    
 




#print (is_word_in("e", hand))     
    
    
#print (wild_cards("a" , "o"))
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    
    
    if (not is_word_in(word, hand)):
        return False
    
    if ("*" in word):
                                                 
        for wind in word_list:
            if (len(wind) == len(word) and wind[word.find("*")] in VOWELS):    
                ast_wind = put_ast(wind,word.find("*"))
                
                if (word == ast_wind):                                         
                    return True
                                        
    for words in word_list:
        if (word == words):
            return True
    return False             
        
  
#word_list = load_words()

#print (is_valid_word(word, hand, word_list))
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0
    for long in hand.values():
        length += long
    
    return length


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        display_hand(hand)
        # Ask user for input
        word = input("Enter word, or !! to indicate that you are finished:")
        # If the input is two exclamation points:
        if (word == "!!"):
            break
            # End the game (break out of the loop)
        
            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:
        if (is_valid_word(word, hand, word_list)):            
                # Tell the user how many points the word earned,
                total_score += get_word_score(word, calculate_handlen(hand))
                print(word, "earned ",get_word_score(word, calculate_handlen(hand))," points. Total: ", total_score , " points")    
                # and the updated total score
                
            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
        else :
            print ("That is not a valid word. Please choose another word.")
            # update the user's hand by removing the letters of their inputted word
        hand = update_hand(hand, word)
        

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print("hand is over. total hand score: ", total_score)        
    # Return the total score as result of function

    return total_score
#play_hand( deal_hand(7) , word_list)
#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_hand = {}
    
    for keys in hand :
                            
        new_hand [keys] = hand[keys]
   
    for letters in new_hand:
        if letter == letters :
            random_letter = random.choice(VOWELS + CONSONANTS)
            while random_letter in new_hand :
                 random_letter = random.choice(VOWELS + CONSONANTS)    
            
            new_hand[random_letter] = new_hand[letters]
            del(new_hand[letters])
             
    return new_hand 

#hand = {'e': 1, 'v': 1, 'n': 1, 'i': 1, 'l': 2000}
 
#letter = "l"       
#print (substitute_hand(hand, letter))       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    number_hands = int(input("How many hands do you want to play"))
    total_score = 0
    first_score = 0
    second_score = 0
    hand = deal_hand(7)
    unique_letter_change = 0
    unique_replay_hand = 0
    for n_hands in range(number_hands):
        if unique_letter_change == 0:        
            yes_no = input("Do you want to subtitute a letter from your hand answer with yes or no")
            if (yes_no == "yes"):
                unique_letter_change = 420
                hand = substitute_hand(hand, input("which letter do you want to change"))
        first_score += play_hand(hand, word_list) 
        if unique_replay_hand == 0 :
            
            
            yes_no2 = input("would you like to replay the hand? You will keep the higher score")    
            if yes_no2 == "yes":
                unique_replay_hand = 420
                second_score += play_hand(hand, word_list)    
            if first_score >= second_score :
                total_score += first_score
            else :
                total_score += second_score
            
        else :
            total_score += first_score
        
        print (total_score)
    
    return total_score
    



#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
