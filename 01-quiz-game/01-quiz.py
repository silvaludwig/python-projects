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
    quit()

# Choosing the theme
print("=" * 50)
print("First, you need to choose the theme...")
print(
    """
    1 - MUSIC AND ART
    2 - CINEMA AND THEATER
    3 - GEOPOLITICS AND RELATED
    4 - TECH
"""
)
print("=" * 50)

theme = int(input("Wich one? "))
print()


if theme == 1:
    print("You choose 1")
    print("Let's talk about MUSIC AND ART!")

elif theme == 2:
    print("You choose 2")
    print("Let's talk about CINEMA AND THEATER!")


elif theme == 3:
    print("You choose 3")
    print("Let's talk about GEOPOLITICS AND RELATED!")


elif theme == 4:
    print("You choose 4")
    print("Let's talk about TECH!")


else:
    print("Oops, I didn't understand")
    quit()
