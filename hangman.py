import random

from helper_functions import load_vocab, check, get_index


# global variable for list of total vocab of possible answers
# (global variable means available in global namespace, ie any block of code can access this)
words = load_vocab()


def start_fresh_game(num_lives=10):
    '''
    This function does:
        1. sets a lowercase random word as answer
        2. sets display as a list of "_", with length equals to len(answer)
    and returns [ answer, display, num_lives, [] ]
    '''

    answer = random.choice(words).lower()
    display = ['_'] * len(answer)
    words_used = []

    return [answer, display, num_lives, words_used]


def run_game():
    user_game_choice = ''
    end_game_char = 'x'
    
    while user_game_choice != end_game_char: 
        print("WELCOME TO HANG MAN") 
        #print(answer)#DEBUG

        # start new game
        answer, display, life, words_used = start_fresh_game()

        while life > 1 :
            
            print("\n")
            print("Guess Word")
            print(display)
            print('letters used')
            print(words_used)
            guess = str(input("enter letter:"))
            
            
            #check if guessed letter is in answer
            verify = check(guess,answer)
            if verify == True:

                # get index of the letters in answers
                index = (get_index(guess,answer))

                # remove under score in display and insert guessed letters
                for i in range(len(index)):
                    display.pop(index[i])
                    display.insert(index[i],guess)

                join_display = "".join(display)

                words_used.append(guess)
                
                
                # check if word is completed
                if answer == join_display:
                    
                    print("congratulation you won!!!")  
                    
                    break
            #minus one life if letter guessed is not in answer    
            else:
                life -= 1
                words_used.append(guess)
                print("wrong ",life, " life remaining")
        
        # user fails - print correct answer and prompt retry
        print("the answer is ",answer," try again!")

        user_game_choice = input("enter 'x' to exit any other key to play again:")    


if __name__ == '__main__':
    run_game()