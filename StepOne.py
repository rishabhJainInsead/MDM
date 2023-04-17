from ColoredPrints import print_red
from NotYes import notYes

# check 1: fundamental objectives
def stepOne():
    print_red("\n---------------------------------")
    print("""\n
Step 1: 
Let's start with something easy.
Write down your fundamental objective.""")
    objectiveInput = input("Done? [yes/no] : ")

    while notYes(objectiveInput):
        print_red("""\n
You have to consider your fundamental objectives! Write them down now!
Done? [yes/no] :""")
        objectiveInput = input()

    return