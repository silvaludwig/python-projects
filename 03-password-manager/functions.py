from time import sleep


def add():
    name = input("Please insert the name or login: ")
    password = input("Please insert the password associated: ")
    sleep(1)
    print("adding new password...")
    with open("passwords.txt", "a") as file:
        file.write(name + "|" + password + "\n")
    sleep(2)
    print("Successfuly registered!")


def view():
    print("Here are all of the passwors saved")
    sleep(2)
    # with open will open the file, do whatever the code below and close the file after
    with open("passwords.txt", "r") as file:
        # readlines() will read all the lines in the file
        for line in file.readlines():
            # rstrip will remove the \n at the and of the line
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user} | Password: {passw}")
