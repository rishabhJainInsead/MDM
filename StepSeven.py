from ColoredPrints import print_red, print_green
from NotYes import notYes

# check 7: patterns!
def stepSeven():
    print_red("\n---------------------------------")
    print("""
\nIt's time for step 7: pattern-checking. Sometimes patterns are real, and sometimes a cinnamon roll is just a cinnamon roll, not matter how much you see Mother Theresa's likeness in it.""")
    dontKnow = input("\nIf your decision is affected by a pattern, is it a real pattern?: [yes/no] ")
    while notYes(dontKnow):
        print_red("Disregard non-patterns! They're only distractions.")
        dontKnow = input("If your decision is affected by a pattern, is it a real pattern?: [yes/no] ")

    print_green("\nYour self-awareness increases with each check, young padawan. You may proceed to step 8.")
    return