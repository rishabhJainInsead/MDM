from ColoredPrints import print_green, print_red, print_yellow

def twelveRecurring():
    print("If your commitment was a t-shirt size(XS, S, M, L, XL) what would the size be?  ")
    commitmentScale = input()
    if commitmentScale in ['S', 'M']:
        print_green("""
Some commitment is necessary to make sure you do due diligence. 
Please keep an eye out for changes in biases due to over-commitment.\n""")
        return
    elif commitmentScale in ['XS']:
        print_yellow("""
Over-committing is a problem but so is under-committing.
Get some skin in the game.
        """)
        twelveRecurring()
    elif commitmentScale in ['L', 'XL']:
        print_red("""
There is high likelihood that you are acting in over-committed to the decision.
Why don't you reassess the resources you've allocated and 
break the larger decision down to smaller ones to remove commitment bias.

If your friends jumped off a bridge, would you do it too .............. ?
        """)
        twelveRecurring()
    else:
        print("""
Please enter a valid t-shirt size in the range\n.
        """)
        twelveRecurring()



def stepTwelve():
    print_red("\n---------------------------------")
    print("""
Step 12:  Lets talk about commitment.
Many a times we make decisions out of over commitment.
Lets run a quick test to determine your commitment to this decision.
    """)

    twelveRecurring()
    return