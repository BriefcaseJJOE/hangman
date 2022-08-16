'''
This module is in charge of displaying game board

gameboard includes:
    - blanks and guesses
    - attempted characters
    - lives graphics (the hanging man thing)

main thing here would be a func that accepts some stuff and does above job


useful shit:
- clear_screen()
- display_gameboard(answer, attempted)
    - clear_screen()
    - need to draw the blanks and "corrects"
    - draw the hanging man shit


'''
import os

def _load_graphics() -> dict:
    '''this function produces NUM_WRONG_TO_GRAPHICS_MAPPING dictionary'''
    results = {}

    for file in os.listdir(GRAPHICS_DIR):
        file = os.path.join(GRAPHICS_DIR, file)
        # get key (num_wrong_attempts)
        file_name_without_extension = file.rsplit('.', 1)[0]
        num_wrong_attempts = int(file_name_without_extension[-1])

        # get value (hanging man graphics)
        with open(file,'r') as f:
            graphics = f.read()
            
        # set key to value in results dict
        results[num_wrong_attempts] = graphics
    
    return results




GRAPHICS_DIR=os.path.join(os.path.dirname(__file__), './graphics')

# this dictionary stores the hanging man graphics to print, according to how many wrong attempts made
# KEY = NUMBER OF WRONG ATTEMPTS MADE
NUM_WRONG_TO_GRAPHICS_MAPPING = _load_graphics()







def clear_screen():
    # TODO: implement properly
    print('\n'*50)


def print_attempt_string(correct_answer:str, attempted:list) -> None:
    '''print attempt_string, censoring out blanks when needed
    - attempted must be a list of LOWERCASE ALPHABET CHARACTERS

    for each char in correct answer:
        check if char in attempted
            - if yes: print that char
            - if no: print _
    '''
    attempted = set(attempted)

    for character in correct_answer:
        if character in attempted:
            print(character, end='')
        else:
            print('_', end='')
        print(' ', end='')


def print_attempts(attempted:list):
    '''attempted must be a UNIQUE list of LOWERCASE CHARS'''
    print('Attempted:')
    print(' , '.join(attempted))


def print_graphics(correct_answer:str, attempted:list) -> None:
    '''
    - count lives
        - count wrong attempts
    - print hanging man
    '''
    num_wrong = len(set(attempted) - set(correct_answer))
    print(num_wrong)
    graphics = NUM_WRONG_TO_GRAPHICS_MAPPING[num_wrong]

    print(graphics)



def display_gameboard(correct_answer:str, attempted:list):
    '''
    - clear screen
    - print attempt-string
    - print attempted_chars
    - print graphics
    '''
    clear_screen()

    print_attempt_string(correct_answer, attempted)

    print_attempts(attempted)

    print_graphics(correct_answer, attempted)



if __name__ == '__main__':
    answer = 'import'
    attempts = ['t', 'a', 'b', 'x', 'c', 'r', 'w']

    display_gameboard(answer, attempts)