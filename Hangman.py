import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses a word from the list 
    while '-' in words or ' ' in words:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letter in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # a place to keep track of geussed letters 

    lives = 6

    #getting user input 
    while len(word_letters) > 0 and lives >0:
        #letters used 
        #'.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        print('You Have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - O R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letters = input('guess a letter: ').upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
                print('')
            else:
                lives = lives - 1 # life lost for wrong guess 
                print("letter is not in word.")

        elif user_letters in used_letters:
            print("You have already used this character. Please try agian")

        else: 
            print("Invalid character. Please try again")
    
    if lives == 0: 
        print("You Died\n", word)
    else: 
        print('You guessed the word', word, '!!')


hangman()