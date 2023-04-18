from ColoredPrints import print_red, print_green

def ethicalRecurring():
    print("""
After answering those questions, 
is the decision the best one you can make in alignment with your judgement and ethics? [yes/no]
    """)

    isEthical = input()
    if isEthical in ['No', 'no', 'It kills me inside']:
        print_red("Nope, absolutely not. We're not even going to talk about this.")
        ethicalRecurring()
    elif isEthical in ['Yes', 'yes', 'no problem', 'ethics?']:
        print_green("You've got it together. I'm moving onto the next step.")
    else:
        ethicalRecurring()
    return

# check 4: did you look for contradicting evidence?
def stepFifteen():
    print_red("\n---------------------------------")
    print("""
Step 15: I promise we are close. Just a little about ethics and values.
'Bear' with us. Ahem.

Have you thought about the following questions,
1. How does your decision align with your values and ethical considerations?
2. To which extent is this decision ethical? Unethical? 
3. Can you think of other options that would be more in line with our values?

Legal and ethical may not always be the same. Remember the Sadhu.

    """)

    ethicalRecurring()
    return