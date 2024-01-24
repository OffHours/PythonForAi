import random
import time

started = False
current_word = '' 
correct_guesses = []
hangman = ['H', 'A', 'N', 'G', 'M', 'A', 'N']
wrong_count = 0

# Start new game
def start():
    print('\nDo you want to play a game?')
    
    for i in range(5):
        print('.')
        time.sleep(1)   

# Check if the guessed letter is in the current word
def check(guess, wrong_count):
    started = True
    letter_count = 0
    
    # Iterate over the words to compare the letters
    for num, i in enumerate(current_word):
        
        # if letter is found, add letter to correct position in "correct_guesses"
        if i == guess:
            print('\nYou are correct, well done!')
            correct_guesses[num] = i
            
            for num, item in enumerate(correct_guesses):
                if item == None:
                    correct_guesses[num] = ('_')
                    
            print(correct_guesses)
            
            # Keep track if we have 1 or more correct letters
            letter_count += 1
    
    # Check if a guess was wrong
    if letter_count == 0:
        # Keep track of incorrect guessess
        wrong_count += 1  
        if wrong_count == 7:
            print(hangman)
            print('\nYou lost a life, try harder next time!')
            started = False
        else:
            print('\nYou are wrong, try again!')
            print(hangman[0:wrong_count:1])
            
    # Convert list to string to make comparison      
    correct_string = ''
    correct_string = correct_string.join(correct_guesses)
    
    # Compare "correct_guesses" with current word to see if the word is complete 
    if current_word == correct_string:
        print('\nCongratulations!\nYou won!\n\nThanks for playing!')
        started = False
        
    return started, wrong_count
            
# Choose a random word for the game          
def word():
    programming_words = ['VARIABLE', 
                         'ALGORITHM', 
                         'FUNCTION', 
                         'LOOP', 
                         'DATABASE', 
                         'SYNTAX', 
                         'DEBUGGING', 
                         'OBJECT', 
                         'CLASS', 
                         'INHERITANCE', 
                         'POLYMORPHISM', 
                         'ENCAPSULATION', 
                         'API', 
                         'FRAMEWORK', 
                         'GIT', 
                         'REPOSITORY', 
                         'COMPILER', 
                         'EXCEPTION', 
                         'RECURSION', 
                         'INTERFACE']
    
    num = random.randrange(0, 20, 1)
    
    # Create a temporary list to show length of word
    word_len = ['_'] * len(programming_words[num])
    
    print(f'The word I¨m looking for is {len(programming_words[num])} letters long.')
    print(word_len)
    
    return programming_words[num]

  
if __name__ == '__main__':

    # Two while loops to to be able to run the game over and over again
    while True:
        
        while started == True:   
            # Uncomment these lines for debugging________________________________________________________
            # print(f'current_word: {current_word}') 
            # print(f'correct_guesses: {correct_guesses}') 
            # print(f'correct_string: {correct_string}')

            # Guess a letter and convert it to upper case to simplify comparison
            guess = input('\nGuess a Letter: ').upper()
        
            started, wrong_count = check(guess,
                                         wrong_count)
            
            if guess == 'BREAK':
                print('\nThanks for playing!')
                started = False
            
        choice = input('\nWrite "start" to start a new game of hangman! \nOr "stop" to be remembered as a coward!: ') 
           
        if choice == 'start':
            start()
            current_word = word()
            correct_guesses = ['_'] * len(current_word)
            started = True
            
        elif choice == 'stop' or 'break':
            print('\nThanks for playing!')
            break
        
        
            
                