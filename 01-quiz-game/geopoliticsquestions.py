from time import sleep


def easy_geopolitics():
    counter = 0
    # first question
    print("Thats the easy ones...")
    print(
        """
Question 1 - Which country is the largest by land area in the world?
    1 - China
    2 - Russia
    3 - Canada
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
Question 2 - What is the capital of the European Union's main institutions?
    1 - Paris
    2 - Berlin
    3 - Brussels
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
Question 3 -  Which continent has the most countries?
    1 - South America
    2 - Africa
    3 - Europe
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
Question 4 - The United Nations (UN) headquarters is located in which city?
    1 - Geneva
    2 - London
    3 - New York City
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
