from time import sleep


def easy_music_and_art():
    counter = 0
    # first question
    print("Thats the easy ones...")
    print(
        """
Question 1 - Who painted the famous artwork Mona Lisa?
    1 - Vincent van Gogh
    2 - Leonardo da Vinci
    3 - Michelangelo
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
Question 2 - Which instrument has 88 keys?
    1 - Violin
    2 - Marimba
    3 - Piano
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
Question 3 -  What is the name of the famous Beatles song that
starts with the lyrics "Yesterday, all my troubles seemed so far away..."?
    1 - Let it Be
    2 - Yesterday
    3 - Hey Jude
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
Question 4 - Which art movement is known for its dream-like,
surreal imagery (like Salvador Dalí's melting clocks)?
    1 - Impressionism
    2 - Cubism
    3 - Surrealism
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
