# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import string
import random
def put_char_on_string(sequence, last_char) :
    '''
    Gives a list of strings where each element is the string sequence with the 
    letter last_char between each letter, for example:
    Sequence = "ab"
    last_char = "c"
    Returns [cab,acb,abc...]          
    
    
    '''
    sequence_list = []
    for N_list in range(len(sequence)) :
        
        sequence_list_elements = ""
        
        for N_letter in range(len(sequence)) :
            if (N_list == N_letter):
                sequence_list_elements += last_char
            
            sequence_list_elements += sequence[N_letter]    
        sequence_list.append(sequence_list_elements)        
    
    sequence_list.append(sequence + last_char)          
    return sequence_list    



        
def del_last_char (sequence):
    new_sequence = ""
    
    for letter in range(len(sequence) - 1):
        new_sequence += sequence[letter]
         
    return new_sequence    
     
        
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    last_char = sequence[len(sequence) - 1]  
    
    if (len(sequence) == 1):
        return [sequence]
    
    for basic_permutation in get_permutations(del_last_char(sequence)):
        permutations.extend(put_char_on_string(basic_permutation, last_char))
    
    return permutations    

print (random.choice(get_permutations("aeiou")))
 
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

