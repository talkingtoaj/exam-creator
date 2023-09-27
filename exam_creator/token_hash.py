import random

HEX_ENCODING1 = "aeiouAEIOU"
HEX_ENCODING2 = "bcdghjklmnprstvwxyz"
HEX_ENCODING3 = "BCDGHJKLMNPRSTVWXYZ-#$%&*+./0123456789:<=>?@^_~!'(){}[]|\\öäüÖÄÜßÖÄÜĞğİıŞşÇç"
HEX_ENCODINGS = [HEX_ENCODING1, HEX_ENCODING2, HEX_ENCODING3]
SEED = [0,2,1,3,0,1,2,0,3]

def value_to_char(value:int)->str:
    # each HEX_ENCODING substring is unique. We select an encoding string randomly, weighted towards the earlier strings. 
    # If the value is larger than the encoding string, we try the next encoding string
    encoding_len = 0
    for i, encoding in enumerate(HEX_ENCODINGS):
        if i == 0 and random.random() < 0.5:
            # occasionally skip vowels for consonants
            continue        
        encoding_len = len(encoding)
        if value < encoding_len:
            return encoding[value]
    else:
        raise Exception("Value is too large, no encoding found for value {value}, max length is {encoding_len}")

def to_hash(choices):
    """ 
    Hash codes help us to identify unique exams, 
    allowing a possible future feature of markers 
    to reverse the hash to retrieve an exact replica
    of the exam
    """
    output = ""
    # each choice has the corresponding seed index added to it, if the choice list is longer than the seed, the seed is repeated
    seeded_choices = [choice + SEED[i] for i, choice in enumerate(choices)]
    for value in seeded_choices:
        output += value_to_char(value)                    
    return output
   
def char_to_value(character:str)->int:
    """
    reverses the value_to_char function
    """
    for i, encoding in enumerate(HEX_ENCODINGS):
        if character in encoding:
            return encoding.index(character)
    else:
        raise Exception(f"Character {character} not found in any encoding")

def from_hash(hash:str):
    """
    reverses the to_hash function
    """
    value_list = [char_to_value(character) for character in hash]
    # remove the seed
    return [value - SEED[i] for i, value in enumerate(value_list)]
