from ColoredPrints import print_red, print_green
from NotYes import notYes

# check 10: unknown unknowns
def stepTen():
    print_red("\n---------------------------------")
    print("""
\nIt's time for step 10: It's hard to know what we don't know, but better to assume that you do not know what you don't know than to think you know everything.""")
    dontKnow = input("\nHave you included any redundancy in your system to account for (un)known unknowns?: [yes/no] ")
    while notYes(dontKnow):
        print_red("A safety belt is redundant to an airbag, but in case of a car accident, you'll be happy to have both. Look for ways to make your system redundant to any unknowns!")
        dontKnow = input("Have you included any redundancy in your system to account for (un)known unknowns?: [yes/no] ")

    print_green("\nGood work, better safe than sorry!")
    return