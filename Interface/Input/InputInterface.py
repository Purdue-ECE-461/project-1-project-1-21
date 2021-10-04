# InputInterface.py
# Created by Jason Lei
# September 23, 2021

import sys
from os import path

from Interface.Interface import Interface

INSTALL_COMMAND = 'install'
TEST_COMMAND = 'test'


# Accepts a given command line argument and determines what mode to activate as a result.
class InputInterface(Interface):

    def __init__(self, mode='idle'):
        super().__init__(mode)

    # Determines what mode to run based on CLI command inputs
    def determineMode(self, user_input):
        # Enter install mode if the string 'install' is given.
        if user_input == INSTALL_COMMAND:
            self.mode = Interface.INSTALL_MODE
            return 'install', None

        # Enter test mode if the string 'test' is given.
        if user_input == TEST_COMMAND:
            self.mode = Interface.TEST_MODE
            return 'test', None

        # Enter rank mode if a file is given. Extract the urls from the lines of the file.
        if path.isfile(user_input):
            self.mode = Interface.RANK_MODE
            packageUrlList = []
            with open(user_input, 'r') as fptr:
                lines = fptr.readlines()
                for line in lines:
                    from validators import url as is_valid_url

                    if is_valid_url(line):
                        packageUrlList.append(line)
                    else:
                        print("Input %s is not a valid URL" % line)
                        sys.exit(2)

                return 'rank', packageUrlList

        else:
            print('Please send a valid input.')
            print('./run <install, test, or a file containing URLs>')
            sys.exit(2)
