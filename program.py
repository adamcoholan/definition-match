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

fileNumber = 0
incorrectGuesses = 0
previousScores = []

files = [
    "Common1.txt", "Common2.txt", "Common3.txt", "Common4.txt", "Common5.txt", "Common6.txt",
    "Basic1.txt", "Basic2.txt", "Basic3.txt", "Basic4.txt", "Basic5.txt", "Basic6.txt", "Basic7.txt",
    "Advanced1.txt", "Advanced2.txt", "Advanced3.txt", "Advanced4.txt", "Advanced5.txt", "Advanced6.txt", "Advanced7.txt",
    "Additional1.txt", "Additional2.txt"
    ]

scoreFile = open("PreviousScores.txt", "r")
for line in scoreFile:
    previousScores.append(line.replace('\n', ''))
scoreFile.close()

while not isFileSelected:
    print()
    print("Welcome!")
    print()
    for i in enumerate(files):
        listNum = i[0] + 1
        splitStr = previousScores[i[0]].split('/')
        if int(splitStr[1]) == 0:
            print(str(listNum) + ".\t" + Fore.BLUE + i[1] + Fore.WHITE + "\tPrevious Score: " + Fore.RED + str(previousScores[i[0]]) + "\t(00.0%)" + Fore.RESET)
        else:
            percentage = int(splitStr[0]) / int(splitStr[1]) * 100
            if percentage == 100.0:
                print(str(listNum) + ".\t" + Fore.BLUE + i[1] + Fore.WHITE + "\tPrevious Score: " + Fore.GREEN + str(previousScores[i[0]]) + "\t(" + str(round(percentage, 1)) +  "%)" + Fore.RESET)
            elif 90.0 <= percentage < 100.0:
                print(str(listNum) + ".\t" + Fore.BLUE + i[1] + Fore.WHITE + "\tPrevious Score: " + Fore.YELLOW + str(previousScores[i[0]]) + "\t(" + str(round(percentage, 1)) +  "%)" + Fore.RESET)
            elif 80.0 <= percentage < 90.0:
                print(str(listNum) + ".\t" + Fore.BLUE + i[1] + Fore.WHITE + "\tPrevious Score: " + Fore.LIGHTRED_EX + str(previousScores[i[0]]) + "\t(" + str(round(percentage, 1)) +  "%)" + Fore.RESET)
            
            else:
                print(str(listNum) + ".\t" + Fore.BLUE + i[1] + Fore.WHITE + "\tPrevious Score: " + Fore.RED + str(previousScores[i[0]]) + "\t(" + str(round(percentage, 1)) +  "%)" + Fore.RESET)

    print()
    fileNumber = input("Select a group to begin game: ")
    print()

    if not fileNumber.isnumeric() or int(fileNumber) > len(files) or int(fileNumber) < 0:
        print(Fore.RED, "Please select numbers 1 through " + str(len(files)), Fore.RESET)
    else:
        isFileSelected = True

activeFile = open(files[int(fileNumber) - 1], "r")
for line in activeFile:
    splitStr = line.split('&')
    processedDefinition = splitStr[1].replace('\n', '')
    words.append(splitStr[0])
    remainingWords.append(splitStr[0])
    definitions.append(processedDefinition)
    if processedDefinition.isnumeric():
        record = processedDefinition
activeFile.close()

correctAnswers = 0
fullLengthList = len(words)
overallScore = len(words)

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
    print("Level:" + Fore.BLUE, str(files[int(fileNumber) - 1].replace('.txt', '') + Fore.RESET))
    print("Previous Score:" + Fore.BLUE, str(previousScores[int(fileNumber) - 1]), Fore.RESET)
    print("Incorrect Guesses:" + Fore.BLUE, str(incorrectGuesses), Fore.RESET)
    print("Correct Guesses:" + Fore.BLUE, str(correctAnswers) + "/" + str(fullLengthList), Fore.RESET)
    print()
    print("Definition:" + Fore.BLUE, chosenDef, Fore.RESET)
    print()

    for i in enumerate(choices):
        listNum = i[0] + 1
        print(str(listNum) + "." + Fore.BLUE, i[1], Fore.RESET)

    while not isGuessSelected:
        print()
        userSelection = input("Guess: ")
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
        overallScore -= 1
        incorrectGuesses += 1
        print()

    isGuessSelected = False
    _ = input("Press Enter to continue...")
    choices = []

print()
print("Congratulations!" + Fore.BLUE + " Game over", Fore.RESET)
print("Overall score:", Fore.BLUE + str(overallScore) + "/" + str(fullLengthList) + Fore.RESET)

currentScores = previousScores

currentScores[int(fileNumber) - 1] = str(overallScore) + "/" + str(fullLengthList)

scoresFile = open("PreviousScores.txt", "w")
for score in currentScores:
    scoresFile.write(str(score) + "\n")
scoresFile.close()

print()
_ = input("Press Enter to exit...")
