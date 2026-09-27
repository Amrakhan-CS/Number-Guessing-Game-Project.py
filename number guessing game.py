import random
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("guess the number : (1-100) "))
    attempts += 1
    if(guess>number):
        print("you guess too high number ")
    elif(guess < number):
        print("you guess too low number")
    else:
        print("congrutulations! you guess right number ")
        print("attemps :", attempts)
        break