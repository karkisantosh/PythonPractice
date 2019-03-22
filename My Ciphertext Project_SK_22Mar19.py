# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:08:19 2019
edX Online course
Introduction to Computer Science and Programming Using Python
by MIT
@author: Santosh Karki
Caesar Cipher Project
cipher algorithm for performing encryption & decryption
pick an integer and shift every letter of your message by that integer.
"""
import string

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

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
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text


    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
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
        codedict = {}
        lower_letters = string.ascii_lowercase
        upper_letters = string.ascii_uppercase
        
        for e in lower_letters:
            pos = lower_letters.index(e) + shift
            if pos == 26:
                pos = 0
            if pos > 26:
                pos = (pos - 26)
            codedict[e] = lower_letters[pos]
        for e in upper_letters:
            pos = upper_letters.index(e)+shift
            if pos == 26:
                pos = 0
            if pos > 26:
                pos = (pos - 26)
            codedict[e] = upper_letters[pos]        
        return codedict
    
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
        mydict = self.build_shift_dict(shift)
        ciphertext = ""
        for alp in self.get_message_text():
            if alp in mydict:
                ciphertext += mydict[alp]
            else:
                ciphertext += alp
        return ciphertext

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
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.get_shift())

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        dict_copy = dict(self.encrypting_dict)
        return dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.apply_shift(self.get_shift())

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.get_shift())

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        encrypt_msg = self.get_message_text()
        guess_shift = 0
        valid_count = 0
        count_dict = {}
        while guess_shift <=26:
            count_dict[guess_shift] = 0 
            plain_message = self.apply_shift(guess_shift-26)
            msg_wordlist = plain_message.split()
            for msgword in msg_wordlist:
                if is_word(self.get_valid_words(), msgword):
                    valid_count += 1
                if valid_count == len(msg_wordlist):
                    return (guess_shift, plain_message)
                    break
            count_dict[guess_shift] = valid_count     
            guess_shift += 1
        mylist = []
        for k, v in count_dict.items():
            mylist.append(v)
        max_val = max(mylist)
        def get_key(val):
            for k, v in count_dict.items():
                if v == max_val:
                    return k
        s = get_key(max_val)
        return (s, self.apply_shift(s))

#%%