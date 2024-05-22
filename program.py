import random
from colorama import Fore
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

isFileSelected = False
isGuessSelected = False

words = []
remainingWords = []
definitions = []

fileName = 0

files = ["Common1.txt", "Common2.txt", "Common3.txt", "Common4.txt", "Common5.txt", "Common6.txt"]

while not isFileSelected:
    print()
    print("Welcome!")
    print()
    for i in enumerate(files):
        listNum = i[0] + 1
        print(str(listNum) + "." + Fore.BLUE, i[1], Fore.RESET)

    print()
    fileName = input("Select a group to begin game: ")
    print()

    if not fileName.isnumeric() or int(fileName) > len(files) or int(fileName) < 0:
        print(Fore.RED, "Please select numbers 1 through " + str(len(files)), Fore.RESET)
    else:
        isFileSelected = True

activeFile = open(files[int(fileName) - 1], "r")
for line in activeFile:
    splitStr = line.split('&')
    processedDefinition = splitStr[1].replace('\n', '')
    words.append(splitStr[0])
    remainingWords.append(splitStr[0])
    definitions.append(processedDefinition)

correctAnswers = 0
fullLengthList = len(words)

while len(remainingWords) > 0:
    randIndex = random.randrange(0, len(remainingWords))

    chosenWord = remainingWords[randIndex]
    chosenDef = definitions[randIndex]
    
    choices = []
    choices.append(chosenWord)

    count = 0
    while count <= 2:
        index = random.randrange(0, len(words))
        if words[index] not in choices:
            choices.append(words[index])
            count += 1

    
    random.shuffle(choices)
    cls()
    print()
    print("Correct Answers:" + Fore.BLUE, str(correctAnswers) + "/" + str(fullLengthList), Fore.RESET)
    print("Definition:" + Fore.BLUE, chosenDef, Fore.RESET)
    print()

    for i in enumerate(choices):
        listNum = i[0] + 1
        print(str(listNum) + "." + Fore.BLUE, i[1], Fore.RESET)

    while not isGuessSelected:
        print()
        userSelection = input("Selection number: ")
        print()

        if not userSelection.isnumeric() or int(userSelection) > 4 or int(userSelection) < 0:
            print(Fore.RED, "Please select numbers 1 through 4", Fore.RESET)
        else:
            isGuessSelected = True

    if choices[int(userSelection) - 1] == chosenWord:
        print(Fore.GREEN, "Correct!", Fore.RESET)
        print()
        correctAnswers += 1
        remainingWords.pop(randIndex)
        definitions.pop(randIndex)

    else:
        print(Fore.RED, "Incorrect.. Correct answer is: " + Fore.RESET, chosenWord)
        print()

    isGuessSelected = False
    _ = input("Press Enter to continue...")

print()
print(Fore.GREEN, "Congratulations! Game over", Fore.RESET)
_ = input("Press Enter to exit...")
