import random
from ColoredPrints import print_green

from StepOne import stepOne
from StepTwo import stepTwo
from StepThree import stepThree
from StepFour import stepFour
from StepFive import stepFive
from StepSix import stepSix
from StepSeven import stepSeven
from StepEight import stepEight
from StepEleven import stepEleven


def FirstTen():
    stepOne()
    stepTwo()
    stepThree()
    stepFour()
    stepFive()
    stepSix()
    stepSeven()
    stepEight()
def MDM():
    print_green("""-------------------------------------------------
Welcome to your computer-aided decision making toolkit!""")

    FirstTen()
    while stepEleven():
        FirstTen()

    #stepTwelve()
