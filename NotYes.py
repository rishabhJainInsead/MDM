import random

#Returns False when there is a Yes String
def notYes(inputString):
    yesList = ['yes', 'Yes', 'howdy', 'yaas']
    if inputString not in yesList:
        return True
    else:
        return False