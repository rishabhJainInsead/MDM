from ColoredPrints import print_red, print_green, print_yellow

def elevenRecurring():
    confidenceScale = input()
    if confidenceScale in ['1', '2', '3', '4', '5', '6']:
        print_green("""
Healthy optimism is important to understand the risks 
and keep an eye out for changes in the ecosystem.\n""")
        return False
    elif confidenceScale in ['7', '8']:
        print_yellow("""
Listen sport, you're walking on threads and needles.
Back in our times we used to keep our eyes open for over confidence.
You should do the same.
        """)
    elif confidenceScale in ['9', '10']:
        print_red("High confidence at this of decision making is a problem. Start again.")
        return True
    else:
        print("""
Please enter a valid number in the range.\n
        """)
        elevenRecurring()

def stepEleven():
    print_red("\n---------------------------------")
    print("""
We're at Step 11!
On a scale of 1 - 10, how confident or Optimistic are we in our assessment of our situation? [1-10]   
    """)

    return elevenRecurring()
