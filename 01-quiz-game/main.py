from techquestions import easy_tech
from geopoliticsquestions import easy_geopolitics
from musicandartquestions import easy_music_and_art
from cinemaquestions import easy_cinema

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
while True:
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
        easy_music_and_art()

    elif theme == 2:
        print("You choose 2")
        print("Let's talk about CINEMA AND THEATER!")
        easy_cinema()

    elif theme == 3:
        print("You choose 3")
        print("Let's talk about GEOPOLITICS AND RELATED!")
        easy_geopolitics()

    elif theme == 4:
        print("You choose 4")
        print("Let's talk about TECH!")
        easy_tech()

    else:
        print("Oops, I didn't understand")
        quit()

    play_again = input("Wanna play again? [Y or N] ")
    if play_again not in "Yy":
        print("Ok then, see ya!")
        break
