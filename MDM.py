from ColoredPrints import print_green, print_red, print_navy

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
#from StepThirteen import stepThirteen
#from StepFourteen import stepFourteen
from StepFifteen import stepFifteen
from StepSixteen import stepSixteen

from pyfiglet import Figlet
from termcolor import colored


def conclude():
    print_navy("""
    You're now done at the end of the decision making framework.
    Healthy decision making is an exercise in self awareness and objectivity.
    
    If you want to know more about management decision making, its too late. P4 is over.
    However, if you'd like to sponsor us a coffee feel free to reach out to any of us,
    
    Lucile Feron
    Yash Nagpal
    Nana Yaw
    Nicolas Sdez
    Rishabh Jain
    
    You're welcome.
    """)

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

    print_red("""
    -----------------------------------------------------
    \nStep 13 and 14 are for groups. 
    
    Unfortunately, we haven't added the secret sauce for 
    getting groups/team decision making in this framework.
    
    Mario and Luigi can save the princess later when we get to it.
    
    Moving on .......  ¯\_(ツ)_/¯\n
    """)

    #stepThirteen()
    #stepFourteen()

    stepFifteen()
    stepSixteen()

    conclude()

