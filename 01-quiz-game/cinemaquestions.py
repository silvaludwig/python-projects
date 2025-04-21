from time import sleep


def easy_cinema():
    counter = 0
    # first question
    print("Thats the easy ones...")
    print(
        """
Question 1 - Which 1997 movie about a sinking ship won 11 Oscars, including Best Picture?
    1 - Inception
    2 - Titanic
    3 - Pearl Harbor
"""
    )
    answer1 = int(input("Your answer: "))
    print("=" * 50)
    print("Checking...")
    print("=" * 50)
    sleep(2)
    if answer1 == 2:
        print("That's right mate! Congrats!")
        counter = counter + 1
    else:
        print("Oops... Not this time! :( ")

    # second question
    print(
        """
Question 2 - Who played the iconic role of Jack Sparrow in Pirates of the Caribbean?
    1 - Brad Pitt
    2 - Robert Downey Jr
    3 - Johnny Depp
"""
    )
    answer2 = int(input("Your answer: "))
    print("=" * 50)
    print("Checking...")
    print("=" * 50)
    sleep(2)
    if answer2 == 3:
        print("That's right mate! Congrats!")
        counter = counter + 1
    else:
        print("Oops... Not this time! :( ")

    # third question
    print(
        """
Question 3 -  In theater, what is the term for a funny play with a happy ending?
    1 - Drama
    2 - Comedy
    3 - Musical
"""
    )
    answer3 = int(input("Your answer: "))
    print("=" * 50)
    print("Checking...")
    print("=" * 50)
    sleep(2)
    if answer3 == 2:
        print("That's right mate! Congrats!")
        counter = counter + 1
    else:
        print("Oops... Not this time! :( ")

    # fourth question
    print(
        """
Question 4 - Which movie features the famous line, "May the Force be with you"?
    1 - Guardian of the Galaxy
    2 - Star Trek
    3 - Star Wars
"""
    )
    answer4 = int(input("Your answer: "))
    print("=" * 50)
    print("Checking...")
    print("=" * 50)
    sleep(2)
    if answer4 == 3:
        print("That's right mate! Congrats!")
        counter = counter + 1
    else:
        print("Oops... Not this time! :( ")

    print("=" * 50)
    print("Crunching the numbers...")
    print("=" * 50)
    sleep(2)
    print(f"You've made {counter} points in this section!")
