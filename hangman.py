import random
from this import d

life = 10

exit = "x"
end = ""
with open ("hangman.txt") as f :
    words = f.read().split("\n")

answer = words[random.randint(0,len(words)+1)]

lower_answer = answer.lower()

words_use = []  

display = []

join_display = ""

for i in range(len(lower_answer)):
    display.append("_")


def check(letter,answer):
    answer = str(answer)
    for i in range(len(answer)):
        if letter == answer[i]:
            return True

def get_index(guess,answer):
    dex = []
    for i in range(len(answer)):
        if answer[i] == guess:
            dex.append (i)
            
    return dex


while end != exit: 
    print("WELCOME TO HANG MAN") 
    #print(lower_answer)#DEBUG
    while life > 1 :
        
        
        answer = words
        
        print("\n")
        print("Guess Word")
        print(display)
        print('letters used')
        print(words_use)
        guess = str(input("enter letter:"))
        
        
        
        #check if guessed letter is in answer
        verify = check(guess,lower_answer)
        if verify == True:

            # get index of the letters in answers
            index = (get_index(guess,lower_answer))

            # remove under score in display and insert guessed letters
            for i in range(len(index)):
                display.pop(index[i])
                display.insert(index[i],guess)

            join_display = "".join(display)

            words_use.append(guess)
            
            
            # check if word is completed
            if lower_answer == join_display:
                
                print("congratulation you won!!!")  
                
                break
        #minus one life if letter guessed is not in answer    
        else:
            life -= 1
            words_use.append(guess)
            print("wrong ",life, " life remaining")
            
    ### reset
    print("the answer is ",lower_answer," try again!")
    life = 10
    words_use = []  
    display = []
    answer = words[random.randint(0,1372)]
    lower_answer = answer.lower()
    for i in range(len(lower_answer)):
        display.append("_")
    answer = words[random.randint(0,1372)]
    
    ### reset

    end = input("enter 'x' to exit any other key to play again:")    
