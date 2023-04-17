from ColoredPrints import print_red, print_green
from NotYes import notYes

# check 8: what about uncertainties?
def stepEight():
    print_red("\n---------------------------------")
    print("""
\nIt's time for step 8: 
Planning for improbable uncertainties is 
like carrying an umbrella in a desert, 
it may seem ridiculous, 
but you never know when a spontaneous rain dance party might break out.""")
    dontKnow = input("\nHave you considered all relevant uncertainties, not matter how improbable?: [yes/no] ")
    while notYes(dontKnow):
        print_red("Don't live with your head in the sand, consider everything!")
        dontKnow = input("Have you considered all relevant uncertainties, not matter how improbable?: [yes/no] ")

    print_green("\nGood, you're one step closer to making a mindful decision.")
    return