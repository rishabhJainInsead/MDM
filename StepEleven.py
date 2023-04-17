import random

from ColoredPrints import print_red, print_green

def elevenRecurring():
    confidenceScale = input()
    if confidenceScale in ['1', '2', '3', '4', '5', '6', '7']:
        print_green("""
Healthy optimism is important to understand the risks 
and keep an eye out for changes in the ecosystem.\n""")
        return False
    elif confidenceScale in ['8', '9', '10']:
        print_red("High confidence at this of decision making is a problem. Start again.")
        return True
    else:
        print("""
Please enter a valid number in the range\n.
        """)
        elevenRecurring()
def stepEleven():
    print_red("\n---------------------------------")
    print("""
We're at Step 11!
On a scale of 1 - 10, how confident or Optimistic are we in our assessment of our situation? [1-10]   
    """)

    return elevenRecurring()