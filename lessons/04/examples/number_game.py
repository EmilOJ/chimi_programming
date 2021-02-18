import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

attempts_left = 6
while attempts_left > 0:
    attempts_left = attempts_left - 1
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break   

if guess == secretNumber:
    print('Good job! You guessed my number')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))