import random #import library

secret = random.randint(1, 9) #selects a random integer from 1-9 inclusive

guess = int(input("Guess a number between 1 and 9: ")) #asks for user inpiut of their guess

while guess != secret: #until they guess correctly, prompt for new guess
    guess = int(input("Wrong guess. Try again: "))

print("Well guessed!")