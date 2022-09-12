import random
import string

from words import words
print(words)

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in words or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        #' '.join(['a', 'b', 'ab']) --> 'a b ab'
        print('You have ', lives, 'You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word : ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # take away a life if wrong word
                print("Letter is not in word.")
        elif user_letter in used_letters:
            print("You have already used that character. please try again.")
        else:
            print("Invalid character! please try again.")
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You die, sorry. The word was: ", word)
    else:
        print("Congrats! you have guessed the right word: ", word)
    print("You have guessed the word ", word, "!!")

user_input = input("Type something: ")
print(user_input)


