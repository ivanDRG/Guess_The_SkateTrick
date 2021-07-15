dictionary = ["mamapinga", "heelflip", "kickflip", "treflip", "frontside", "backside", "fifty-fifty", "frontside-flip", "backside-flip", "varial-kickflip", "varial-heelflip", "hardflip", "ghetto-bird", "laser-flip", "inward-heelflip", "bigspin", "dolphin-flip", "pressure-flip", "shove-it", "dragon-flip", "gazelle-flip", "nollie-flip","crooked", "pivot", "salad", "smith", "feeble", "bluntslide", "lipslide", "noseslide", "suski", "tailslide", "boardslide"]
import random
num = random.randint(0, len(dictionary) - 1)
word = dictionary[num]
wlist = list(word)
finallist = []
win = False
for x in range(len(word)):
    finallist.append("_")
if "-" in wlist:
            indx = wlist.index("-")
            finallist[indx] = wlist[indx]
            wlist[indx] = "_"
print(""" 
 _______________________________________________________
|WELCOME TO THE ULTIMATE SKATE TRICK NAME GUESSING GAME |
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
A random skate trick name will be generated and you will have to guess it writting ONE word at a time.
If there is a space between the trick name it will be represented as a dash '-'.
underscores(_), numbers and ñ are not allowed.
Have fun, and there is a secret easter egg, let's see if you are lucky and you find it ;)
""")

while win == False:
    print("Can you guess the word?")
    print(" ".join(finallist))
    letter = input("What is your letter guess? ")
    if letter in wlist:
        print("Congrats! the letter was in the word.")
    else:
        print("Sorry, the letter wasn't in the word, try again.")
    for x in range(len(word)):
        if letter in wlist:
            indx = wlist.index(letter)
            finallist[indx] = wlist[indx]
            wlist[indx] = "_" 
    print("----------------------------------------------------------")
    if "".join(finallist) == word:
        print("_________________________________________________________________________")
        print("You guessed the word!!!, it was: " + word)  
        print("_________________________________________________________________________")   
        win = True
    