"""
This is a quiz game made from scratch.
The major objective here is to practice and improve it.
I'll start with the basics.
"""

# Welcoming the user
print(
    "Hi! Welcome to the place that is gonna try out your knolege about some silly things"
)
play_or_not = input("In the mood for some quiz? [Y or N] ")

if play_or_not in "Nn":
    print("Ok then, see ya!")
    quit()
elif play_or_not in "Yy":
    print("Ok, let's go!")
else:
    print("I don't know what u mean pal...")
