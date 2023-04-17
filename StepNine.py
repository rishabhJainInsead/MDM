from ColoredPrints import print_red, print_green
from NotYes import notYes

# check 9: coconuts and black swans
def stepNine():
    print_red("\n---------------------------------")
    print("""
\nIt's time for step 9: We know that the ability for a swallow to carry a one-pound coconut depends on whether it is a European or an African swallow, but how many black swans are needed? Time for step 9: consider your coconuts and black swans.""")
    dontKnow = input("\nHave you identified  the main threats and opportunities associated with your decision problem?: [yes/no] ")
    while notYes(dontKnow):
        print_red("You might be missing a crucial element in your decision if you skip this!")
        dontKnow = input("Have you identified  the main threats and opportunities associated with your decision problem?: [yes/no] ")

    print_green("\nOutstanding!")
    return