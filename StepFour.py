from ColoredPrints import print_red, print_green

def contradictingRecurring():
    print("""
Are you happy living in a possible 
delusion with possibly dire consequences? [happy/sane]
    """)

    isContradicting = input()
    if isContradicting in ['happy', 'Happy', 'Mast', 'Gazab']:
        print_red("No you're not happy. Stop lying and do your homework.")
        contradictingRecurring()
    elif isContradicting in ['sane', 'Sane', 'INSEADer', 'Legend']:
        print_green("You've got it together. I'm moving onto the next step.")
    else:
        contradictingRecurring()
    return

# check 4: did you look for contradicting evidence?
def stepFour():
    print_red("\n---------------------------------")
    print("""
Step 4 is on a similar note to step 3, 
did you even bother looking for any 
contradicting evidence to your beliefs.
    """)

    contradictingRecurring()
    return
