#start setup and backround ~~~~~~~~~~~~~~~~~~~~~~


#end setup and backround ~~~~~~~~~~~~~~~~~~~~~~~~
#starting variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

name = "Student"

def setupGame():

    #end starting variables ~~~~~~~~~~~~~~~~~~~~~~~~~
    #start game ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    print("Hello, you have been chosen to go to middle school at Indian Hills.")
    print("Goal? Survive.")
    print(" ")
    print("What is your name?")

    print(" ")
    print("[1] Lil Boi")
    print(" ")
    print("[2] Thing 1")
    print(" ")
    print("[3] Cool Boi")
    print(" ")
    print("[4] Henry")
    print(" ")

    choice = input("")


    if choice == "1":
        print("Got it. Lil Boi, you got this.")
        name = "Lil Boi"

    if choice == "2":
        print("Ok, Thing 1, gotime.")
        name = "Thing 1"

    if choice == "3":
        print("Cool Boi, good luck.")
        name = "Cool Boi"

    if choice == "4":
        print("The best name. Wise. I wish you the best of luck on your journey.")
        name = "Henry"

    print(name + ", what team are you on?")

    print(" ")
    print("[1] Inspire")
    print(" ")
    print("[2] Vision")
    print(" ")
    print("[3] Aloha")
    print(" ")

    choice = input("")

    if choice == "1":
        print("Cool, Inspire is the best team!")
        team = "Inspire"

    if choice == "2":
        print("Vision (L team)")
        team = "Vision"

    if choice == "3":
        print("LMAO imagine being on Aloha")
        team = "Aloha"

    print(" ")
    print("Does the following information look correct?")
    print(" ")
    print("Team:   " + team)
    print(" ")
    print("Name:   " + name)
    print(" ")
    print(" ")

    print("[y] Yes")
    print(" ")
    print("[n] No")
    print(" ")

    choice = input("")

    if choice == "y":
        return True
    else:
        return False


while True:
    isGameSetup = setupGame()
    if isGameSetup:
        break
print("Starting game!")