import random
from time import sleep

print("Welcome! We're gonna play some guess the number game...")
range = input("Type a number please: ")

if range.isdigit():
    range = int(range)

    if range <= 0:
        print("You typed a number equal or smaller than 0.")
        quit()

else:
    print("You didn't typed a number. Bye.")
    quit()

print(
    f"Thanks! Now I'll generate a number between 0 and {range} and you'll guess it..."
)
print("Generating...")
sleep(2)
random_number = random.randint(1, range)
print("Done!")

user_guess = input("Guess the number: ")

if user_guess.isdigit():
    user_guess = int(user_guess)

    if user_guess <= 0:
        print("You typed a number smaller than 0.")
        quit()

else:
    print("You didn't typed a number. Bye.")
    quit()

print("Matching your guess with my generated number...")
sleep(2)
if user_guess == random_number:
    print("You nailed it!")
    print(f"You guessed: {user_guess} and I've generated: {random_number}")
    print("Congrats!")
else:
    print("Sorry friend, not this time!")
    print(f"You guessed: {user_guess} and I've generated: {random_number}")
