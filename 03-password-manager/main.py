from functions import add, view
from time import sleep

while True:
    print("=" * 50)
    print("Welcome to the Password Manager!")
    print("=" * 50)
    sleep(1)
    print("Here are the options:")
    sleep(1)
    mode = input(
        """Type <add> to add a new password,
Type <view> if you want to visualize the passwors,
Type <quit> to leave the application
What you wanna do? """
    )

    if mode == "quit":
        sleep(1)
        print("=" * 50)
        print("Exiting application. Bye.")
        print("=" * 50)
        break

    if mode == "add":
        sleep(1)
        add()

    elif mode == "view":
        sleep(1)
        view()

    else:
        sleep(1)
        print("Invalid mode...")
        continue
