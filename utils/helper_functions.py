import os
VOCAB_DATA_FILEPATH=os.path.join(os.path.dirname(__file__),'./hangman.txt')



def load_vocab(data_filepath=VOCAB_DATA_FILEPATH):
    with open(data_filepath) as f:
        return f.read().split('\n')


def check(letter,answer):
    '''returns a boolean saying if letter is found in answer'''
    answer = str(answer)
    for i in range(len(answer)):
        if letter == answer[i]:
            return True

def get_index(guess,answer):
    '''returns a list of all indexes of answer, that is equal to guess character'''
    dex = []
    for i in range(len(answer)):
        if answer[i] == guess:
            dex.append (i)
            
    return dex