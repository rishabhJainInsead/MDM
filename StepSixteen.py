from ColoredPrints import print_red, print_green

def emotionalRecurring():
    print("""
After answering those questions, 
is the decision the best one you can make in alignment with your emotions? [yes/no]
        """)

    isEmotional = input()
    if isEmotional in ['No', 'no', 'It kills me inside']:
        print_red("Try listening to Pink Floyd and answer this again.")
        emotionalRecurring()
    elif isEmotional in ['Yes', 'yes', 'no problem', 'ethics?']:
        print_green("You've got it together. Go get whatever you're seeking. May the power be with you.")
    else:
        emotionalRecurring()
    return


def stepSixteen():
    print_red("----------------------------------------")
    print("""
Last Step:
Decisions are emotional experiences. Here are some important questions to ask yourself,

1. What are you feeling? 
2. How might emotions be influencing your decision?
3. Is it the right moment to make any decision?
4. Are you putting unnecessary time constraints on our thinking process which increase emotions?
5. Have you given ourselves enough time to consider all alternatives.
    """)
    emotionalRecurring()

    return
