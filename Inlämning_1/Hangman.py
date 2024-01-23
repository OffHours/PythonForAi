import random
import time

started = False
current_word = '' 
correct_guesses = []
hangman = ['H', 'A', 'N', 'G', 'M', 'A', 'N']
wrong_count = 0

#Starta nytt spel
def start():
    print('Do you want to play a game?')
    
    for i in range(5):
        print('.')
        time.sleep(1)   
    
def check(guess, wrong_count):
    started = True
    letter_count = 0
    
    for num, i in enumerate(current_word):
        if i == guess:
            print('You are correct, well done')
            correct_guesses[num] = i
            
            for num, item in enumerate(correct_guesses):
                if item == None:
                    correct_guesses[num] = ('_')
                    
            print(correct_guesses)
            
            letter_count += 1
    
    if letter_count == 0:
        wrong_count += 1  
        if wrong_count == 7:
            print(hangman)
            print('You lost a life, try harder next time!')
            started = False
        else:
            print('You are wrong, try again!')
            print(hangman[0:wrong_count:1])
            
    return started, wrong_count
            
                  
            
                
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
    num = random.randrange(1, 20, 1)
    
    return programming_words[num]

  
if __name__ == '__main__':

    
    while True:
        
        while started == True:   
            print(current_word) #For debugging
            
            guess = input('Guess a Letter: ').upper()
            
            if guess == 'break':
                break
                
            started, wrong_count = check(guess, 
                                         wrong_count)
            
        choice = input('Write "start" to start a new game of hangman! \nOr "stop" to be remembered as a coward!: ') 
           
        if choice == 'start':
            start()
            current_word = word()
            correct_guesses = [None] * len(current_word)
            started = True
            
        elif choice == 'stop' or 'break':
            print('Thanks for playing!')
            break
        
        
            
                