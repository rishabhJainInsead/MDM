from ColoredPrints import print_red, print_green
from NotYes import notYes


def realityTestRecurring():
    print("""
Have you done a reality check to validate your assumptions? [Yes/No]
    """)

    hasValidated = input()
    if notYes(hasValidated):
        print_red("""
It is important to validate assumptions with real life testing.
We know it isn't easy to do so, but think of the risks if you don't.
Be creative and try again. You've got it.
        """)
        realityTestRecurring()
    else:
        print_green("""
Testing Assumptions can make or break the outcomes of your decisions.
Make sure you understand the you can still be wrong.
However, by testing you have minimized some risks.

Good job, beta.
        """)
    return


# check 5: testing-1-2-3
def stepFive():
    print_red("\n---------------------------------")

    print("""
You made it to step 5!
Time for the real brain twisting: testing 1-2-3.

Testing is like trying to fit a giraffe into a car - it may seem awkward and ridiculous, but it's better to discover it won't work in the testing phase than on the road.
""")

    realityTestRecurring()