from ColoredPrints import print_red, print_green
from NotYes import notYes

# check 6: belief v reality
def stepSix():
    print_red("\n---------------------------------")
    print("""
\nYou made it to step 6! Sometimes our beliefs don't match reality, just ask any child who learns Santa is not real. Test your beliefs!""")
    dontKnow = input("\nAre you doing what will really work, not just what you believe will work?: [yes/no] ")
    while notYes(dontKnow):
        print_red("Journey's 'Don't Stop Believing' is a great song, but this is not the time or place. Check your reality.")
        dontKnow = input("Are you doing what will really work, not just what you believe will work?: [yes/no] ")

    print_green("\nIt's hard to test your own beliefs, but you did it!")
    return

# Are we doing what we believe works or what really works? 
# How can we test our ideas and beliefs with some quick experiments?