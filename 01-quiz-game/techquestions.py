from time import sleep


def easy_tech():
    counter = 0
    # first question
    print("Thats the easy ones...")
    print(
        """
Question 1 - Who is the creator of World Wide Web (WWW)?
    1 - Tim Berners-Lee
    2 - Donald Trump
    3 - Elon Musk
"""
    )
    answer1 = int(input("Your answer: "))
    print("=" * 50)
    print("Checking...")
    print("=" * 50)
    sleep(2)
    if answer1 == 1:
        print("That's right mate! Congrats!")
        counter = counter + 1
    else:
        print("Oops... Not this time! :( ")

    # second question
    print(
        """
Question 2 - What Wi-Fi stands for?
    1 - Widget Fingers
    2 - Wireless Fields
    3 - Wireless Fidelity
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
Question 3 - Which is the principal component of a computer, responsible for data proccessing?
    1 - BPU (bipolar processing unit)
    2 - CPU (central proccessing unit)
    3 - GPU (graphic proccessing unit)
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
Question 4 - What's the name of the most popular OS in the world?
    1 - Fedora
    2 - MacOS
    3 - Windows
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
