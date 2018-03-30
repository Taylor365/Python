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

AIDictionary = []
listOfChars = []


def aiLearning(secretWord, listOfChars):
    secretWordLength = len(secretWord)
    listOfChars.clear()
    for element in AIDictionary:
        if len(element) == secretWordLength:
            for i in element:
                if i not in listOfChars:
                    listOfChars.append(i)


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


def computerGuess():
    firstTier = 'a e i o u'.split()
    secondTier = 'b m d h c l s'.split()
    thirdTier = 'y p w n k j r t f g h'.split()
    lastTier = 'z q x'.split()

    #time.sleep(3)
    if len(missedLetters) < 2:
        return firstTier[random.randint(0, len(firstTier) - 1)]
    elif len(missedLetters) < 4:
        return secondTier[random.randint(0, len(secondTier) - 1)]
    elif 4 <= len(missedLetters):
        return thirdTier[random.randint(0, len(thirdTier) - 1)]

    #return listOfChars[random.randint(0, len(listOfChars) - 1)]


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
            guess = computerGuess()
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
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


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

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            if player == '2':
                aiLearning(secretWord, listOfChars)
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            if secretWord not in AIDictionary:
                AIDictionary.append(secretWord)
            print(AIDictionary)
            print(listOfChars)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            if player == '2':
                aiLearning(secretWord, listOfChars)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
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

