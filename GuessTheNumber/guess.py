import random

guessesTaken = 0

number = random.randint(1, 20)

print('Guess a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed the number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Game Over. The number I was thinking of was ' + number)
