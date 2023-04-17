from ColoredPrints import print_green

from StepOne import stepOne
from StepTwo import stepTwo
from StepThree import stepThree
from StepFour import stepFour
from StepFive import stepFive
from StepSix import stepSix
from StepSeven import stepSeven
from StepEight import stepEight
from StepNine import stepNine
from StepTen import stepTen
from StepEleven import stepEleven
from StepTwelve import stepTwelve
from StepThirteen import stepThirteen
from StepFourteen import stepFourteen
from StepFifteen import stepFifteen
from StepSixteen import stepSixteen


def firstTen():
    stepOne()
    stepTwo()
    stepThree()
    stepFour()
    stepFive()
    stepSix()
    stepSeven()
    stepEight()
    stepNine()
    stepTen()


def mdm():
    print_green("""-------------------------------------------------
Welcome to your computer-aided decision making toolkit!""")

    firstTen()
    while stepEleven():
        firstTen()

    stepTwelve()
    stepThirteen()
    stepFourteen()
    stepFifteen()
    stepSixteen()

