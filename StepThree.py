from ColoredPrints import print_red
from NotYes import notYes

# check 3: what's missing?
def stepThree():
    print_red("\n---------------------------------")
    print("""
\nIt's time for step 3!
Remember the shame of not asking for additional information during the Carter Racing case?
Now is the time to redeem yourself! Write down what you wish you knew.""")
    dontKnow = input("\nIs there something that you wish you knew about your problem? [yes/no] ")
    while not notYes(dontKnow):
        print_red("You have this beautiful tool called the Internet at your disposal. Use it. Don't be a fool.")
        dontKnow = input("Is there something that you wish you knew about your problem? [yes/no] ")

    return