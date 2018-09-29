#This is a guess the number game.\
import random
import time

# These are our global variables:
guessesTaken = 0
choice = 0
gameover = False
highorlow = ''
number = random.randint(1, 20) 

# This is the function for the AI:
def aiPlayer(guessesTaken, number, highorlow):
  aiguess = 0
  ailowestGuess = 0
  aihighestGuess = 21
  aiguess = int(aiguess)
  aiMidPoint = 0

  while guessesTaken < 6:
    guessesTaken = guessesTaken + 1
    
    aiguess = random.randint(ailowestGuess + 1, aihighestGuess - 1)
    if guessesTaken > 0 and ailowestGuess != 0:
      aiMidPoint = ailowestGuess + int(round(((aihighestGuess) - (ailowestGuess)) / 2))
      aiguess = aiMidPoint
      print("AI's MidPoint is " + str(aiMidPoint))

    print("")
    print("")
    print("AI's guess is " + str(aiguess))
    print("")

    if aiguess < int(number):
      print('You guess is too low.')
      highorlow = 'low'
    if aiguess > int(number):
      print('Your guess is too high')
      highorlow = 'high'
    if aiguess == number:
      break;

    if highorlow == 'low' and ailowestGuess < aiguess:
      ailowestGuess = aiguess
    if highorlow == 'high'  and aihighestGuess > aiguess:
      aihighestGuess = aiguess

    print("")
    print("AI's Lowest guess is " + str(ailowestGuess))
    print("AI's Highest guess is " + str(aihighestGuess))
    time.sleep(2)
    
  if aiguess == int(number):
    guessesTaken = str(guessesTaken)
    print('Good job, SkyNet! You guessed my number in ' + guessesTaken + ' guesses!')

  if aiguess != number:
    number = str(number)
    print('Nope. The number i was thinking of was ' + number)

# This is the function for the Human player:
def humanPlayer(guessesTaken, number):
  print ('Hello! What is your name')
  myName = input()

  number = random.randint(1, 20)
  print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

  while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
      print('You guess is too low.') 

    if guess > number:
      print('Your guess is too high')

    if guess == number:
      break

  if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
  if guess != number:
    number = str(number)
    print('Nope. The number i was thinking of was ' + number)

# This is where the game begins:
print('Choose who you want to play.')
print('1 - Computer')
print('2 - Player')
choice = input()

while(choice == '1' and gameover == False):
  aiPlayer(guessesTaken, number, highorlow)
  gameover = True

while(choice == '2' and gameover == False):
  humanPlayer(guessesTaken, number)
  gameover = True
