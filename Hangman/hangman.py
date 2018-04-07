import operator
import random
import time

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========''']

words = 'ant baboon badger bat bear beaver camel cow cat clam cobra cougar coyote crow deer dog donkey ' \
        'duck eagle ferret fox frog goat goose hawk lion lizard monkey moose panda pelican turtle turkey weasel wolf ' \
        'wombat zebra'.split()

# Each letter is weighted and weight is increased by frequency they occur in the secret word
AIValuedLetters = {
                "A": 0,
                "B": 0,
                "C": 0,
                "D": 0,
                "E": 0,
                "F": 0,
                "G": 0,
                "H": 0,
                "I": 0,
                "J": 0,
                "K": 0,
                "L": 0,
                "M": 0,
                "N": 0,
                "O": 0,
                "P": 0,
                "Q": 0,
                "R": 0,
                "S": 0,
                "T": 0,
                "U": 0,
                "V": 0,
                "W": 0,
                "X": 0,
                "Y": 0,
                "Z": 0}

#weighting code
# foreach (char item in wokrds[0])
#             {
#                 if (item.ToString().ToLower().Equals("a"))
#                 {
#                     words["A"] = words["A"] + 1;
#                 }
#             }


AIDictionary = []
listOfChars = []
play = 0
win = 0
lose = 0


def aiGetChars(secretWord, listOfChars):
    secretWordLength = len(secretWord)
    listOfChars.clear()
    for element in AIDictionary:
        if len(element) == secretWordLength:
            for i in element:
                k = i.upper()
                if k not in listOfChars:
                    listOfChars.append(k)


def aiIncrementLetters(secretWord, AIValuedLetters):
    secretWordLength = len(secretWord)
    for j in range(secretWordLength):
        if secretWord[j].upper() in AIValuedLetters:
            AIValuedLetters[secretWord[j].upper()] = AIValuedLetters[secretWord[j].upper()] + 1


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def computerGuess(alreadyGuessed, AIValuedLetters, listOfChars, correctLetters, secretWord):
    alreadyGuessedBIG = alreadyGuessed.upper()
    secretWordLength = len(secretWord)

    AIValuedLetters = sorted(AIValuedLetters.items(), key=operator.itemgetter(1), reverse=True)
    print(AIValuedLetters)
    if len(correctLetters) > 2:
        for element in AIDictionary:
            if len(element) == secretWordLength:
                if correctLetters[0] in element and correctLetters[1] in element and correctLetters[2] in element:
                    for i in element:
                        if i not in alreadyGuessed:
                            return i

    if len(listOfChars) < 1:
        for key, value in AIValuedLetters:
            if key not in alreadyGuessedBIG:
                return key
    elif len(listOfChars) > 0:
        for key, value in AIValuedLetters:
            if key not in alreadyGuessedBIG and key in listOfChars:
                return key
        for key, value in AIValuedLetters:
            if key not in alreadyGuessedBIG:
                return key


    # OLD WAY OF RANDOM GUESSING
    # firstTier = 'a e i o u'.split()
    # secondTier = 'b m d h c l s'.split()
    # thirdTier = 'y p w n k j r t f g h'.split()
    # lastTier = 'z q x'.split()
    # if len(missedLetters) < 2:
    #   return firstTier[random.randint(0, len(firstTier) - 1)]
    # elif len(missedLetters) < 4:
    #   return secondTier[random.randint(0, len(secondTier) - 1)]
    # elif 4 <= len(missedLetters):
    #   return thirdTier[random.randint(0, len(thirdTier) - 1)]


def getGuess(alreadyGuessed):
    while True:
        if player == '1':
            print('Guess a letter.')
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return guess
        else:
            print('Guess a letter.')
            guess = computerGuess(alreadyGuessed, AIValuedLetters, listOfChars, correctLetters, secretWord)
            guess = guess.lower()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return guess


def playAgain():
    print('Wins =' + str(win))
    print('Losses =' + str(lose))
    print('Do you want to play again? (yes or no)')
    global play
    if play == 1:
        return input().lower().startswith('y')
    else:
        play += 1
        return 'y'


print('Would you like to play, or let the computer try?')
print('1 - player\n2 - Computer')
player = input()

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False


while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    if player == '2':
        aiGetChars(secretWord, listOfChars)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            win += 1
            if player == '2':
                aiIncrementLetters(secretWord, AIValuedLetters)
                if secretWord not in AIDictionary:
                    AIDictionary.append(secretWord)
                print(AIDictionary)
                print(listOfChars)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            lose += 1
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            if player == '2':
                aiIncrementLetters(secretWord, AIValuedLetters)
                if secretWord not in AIDictionary:
                    AIDictionary.append(secretWord)
                print(AIDictionary)
                print(listOfChars)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break

