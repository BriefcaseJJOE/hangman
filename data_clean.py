

with open("string.txt") as f:
    words = f.read().split("\n")

print(words) 

f = open("hangman.txt","a")
for word in words:
    if len(word) > 4:
        f.write(word+"\n")
    print(words)
f.close()

