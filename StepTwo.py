from ColoredPrints import print_red
from NotYes import notYes

def getAlternativeAssociations():
    print("""
Now that you have forced connections, write out non-obvious alternatives.
Write down several alternatives beyond the most obvious ones. Enter 'yes' when done: """)

    wordList = [
        'table',
        'bottle',
        'backpack',
        'wall',
        'fooseball',
        'piano',
        'plant'
    ]
    nextAlt = ""
    count = 1
    while notYes(nextAlt):
        print("Alternative Association #" + str(count) + " :" + wordList.pop())
        print("Are you done? [Yes,No] ")
        nextAlt = input()
        count = count + 1

    return

def firstRecurring():
    firstWord = input("Ready for the first word? [yes/no] ")
    if not notYes(firstWord):
        print("Force a connection between your problem and the following word: apple\n")
    else:
        print_red("Rome wasn't built in a day.")
        firstRecurring()
    return

def firstWord():
    print_red("\n---------------------------------")
    print("""
Step 2: Let's expand your view!
Force a connection between your problem and the following word: flashlight
\nLet's do this 3 more times.""")

    firstRecurring()
    return

def secondRecurring():
    secondWord = input("Ready for the second word? [yes/no] ")
    if not notYes(secondWord):
        print("Force a connection between your problem and the following word: house\n")
    else:
        print_red("Can't give up now")
        secondRecurring()
    return
def secondWord():
    print("""
\nLet's do this 2 more times.
Here comes the second word!""")

    secondRecurring()
    return

def thirdRecurring():
    thirdWord = input("Ready for the third word? [yes/no] ")
    if not notYes(thirdWord):
        print("Force a connection between your problem and the following word: bee\n")
    else:
        print_red("Get them juices flowing. You're almost there!")
        thirdRecurring()
    return

def thirdWord():
    print("""
\nLet's do this 1 more time.
Last one. Here comes the third word!""")

    thirdRecurring()
    return


# check 2: expanded view
def stepTwo():
    firstWord()
    secondWord()
    thirdWord()

    getAlternativeAssociations()
    return



