# This is a sample Python script.
from MDM import mdm
from pyfiglet import Figlet
from termcolor import colored

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = Figlet(font='doh')
    print(colored(f.renderText('Making Good Decisions'), 'red'))
    mdm()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
