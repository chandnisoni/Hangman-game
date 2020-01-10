import string

words = "CHANDANI"
length = len(words)
MAX_TRIES = 8
result = ['_' for i in range(len(words))]

tries=0
while tries < MAX_TRIES:
    inp = input("Guess an alphabet: ")
    count = 0
    # Did the character that the user guessed exists in the word?
    if inp in words:
        pass
    else:
        tries += 1

    for x in words:
        if(x.casefold() == inp.casefold()):
            result[count] = inp.upper()
        count = count+1
    print(result)
    print(tries)

print("this is it: ", result)
