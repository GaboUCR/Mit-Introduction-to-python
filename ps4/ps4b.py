# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string


    
def list_to_string (word_list):
    new_list = ""
    
    for word in word_list:
        if (len(word_list) == 1) :
            return word
        
        new_list += word + " "
    
    return new_list    


def switch_dictionary (dictionary):
    '''
    Takes a dictionary and switches the keywords for the values
    '''
    switched_dictionary = {}
    
    for element in dictionary:
        
        switched_dictionary[dictionary[element]] = element
    
    return switched_dictionary    


def creates_dictionary(shift):
    '''
    Returns a list with two dictionarys, a shifted one and a regular 
    '''
    L_alphabet = "abcdefghijklmnopqrstuvwxyz" 
    Upp_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = shift
    L_shifted_dictionary = {}
    Upp_shifted_dictionary = {}
        
        #put in place the lower case chunk
    for letters in L_alphabet :
        L_shifted_dictionary[counter] = letters 
        if (counter == 26):
            counter = 0
        counter += 1    
        
        #put in place the upper case
    counter = shift + 26
    for letters in Upp_alphabet :
        Upp_shifted_dictionary[counter] = letters
        if (counter == 52):
            counter = 26
        counter += 1        
        #add the two dictionaries
    for element in Upp_shifted_dictionary:
        L_shifted_dictionary [element] = Upp_shifted_dictionary[element]    
        
                
    return L_shifted_dictionary    


def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

       
class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message = text
        self.valid_words = load_words("words.txt")
    

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        
        return self.message
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        new_valid_words = self.valid_words
        return new_valid_words
    
    def set_message_text(self, new_message) :
        self.message = new_message
    
    
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shifted_dictionary = switch_dictionary(creates_dictionary(shift +1))
        dictionary = creates_dictionary(1)
        ultimate_dictionary = {}
        
        for letters in shifted_dictionary:
           
            ultimate_dictionary[letters] = dictionary[shifted_dictionary[letters]]
                
        return ultimate_dictionary
    
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        shifted_message = ""
        message_text = self.get_message_text()
        shifted_dictionary = self.build_shift_dict(shift)
        
        
        for letters in message_text:
            
            if (letters == " " or letters == "," or letters == "."):
                shifted_message += letters
                continue
            
            shifted_message += shifted_dictionary[letters]  
            
        return shifted_message

    
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.encryption_dict  (string, created using shift)

        '''
        Message.__init__(self,text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.encrypted_text = self.apply_shift(shift)
    
   
   
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encryption_dict_copy = self.encryption_dict
        
        return encryption_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.encrypted_text

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        maxN_valid_words = 0
        final_decrypted_message =[]
        valid_shift = 0
        for shifts in range (1 ,26):
            n_valid_words = 0
            decripted_message = []
           
            for word in self.apply_shift(26 - shifts).split(" ") : 
                
                if(is_word( self.get_valid_words() , word)) :
                    n_valid_words += 1
                    decripted_message.append(word)
                                        
            if (n_valid_words > maxN_valid_words):
                valid_shift = shifts                
                final_decrypted_message = decripted_message
                maxN_valid_words = n_valid_words
                
        
        return (26 - valid_shift ,  list_to_string(final_decrypted_message))        


pepito = PlaintextMessage("they say the child was monstrous", 24)  

lalo = CiphertextMessage(get_story_string())

print(lalo.decrypt_message())

#print(lalo.apply_shift(4))

#print (pepito.get_message_text_encrypted(),lalo.decrypt_message())

#if __name__ == '__main__':

        
    

    
  
