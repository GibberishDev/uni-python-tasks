import random

print("Try to guess number between 1 and 10 in 3 tries")
number=random.randint(1,10)
for i in range(3):
    guess=int(input(f"Your guess [{i+1}/3]: "))
    if guess==number:
        print(f"You guessed right! The number indeed is {number}")
        break
    elif i!=2:
        print(f"No. Real number is {"lower" if guess>number else "higher"}")
    else:
        print(f"No. You failed to guess the number. The number was {number}")