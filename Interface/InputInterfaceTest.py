# InputInterfaceTest.py
# Created by Jason Lei
# October 1, 2021

from Interface.InputInterface import InputInterface
from Interface.Interface import Interface


# InputInterfaceTest serves to test the InputInterface class. Will return a list of form num_passed, num_tests
def test():
    ii = InputInterface()
    tests = [test1, test2, test3]
    num_tests = len(tests)
    num_passed = 0

    # Perform tests
    for t in tests:
        num_passed += t(ii)

    # Return results
    print(num_tests, num_passed)
    return num_passed, num_tests


# Tests the install mode input
def test1(interface):
    output = interface.determineMode('install')
    # Check for correct interface output, return 1 if passed, 0 if failed
    if output != 'install' or interface.mode != Interface.INSTALL_MODE:
        return 0
    else:
        return 1


# Tests the test mode input
def test2(interface):
    output = interface.determineMode('test')
    # Check for correct interface output, return 1 if passed, 0 if failed
    if output != 'test' or interface.mode != Interface.TEST_MODE:
        return 0
    else:
        return 1


# Tests the rank mode input
def test3(interface):
    output, urls = interface.determineMode('sample_url_file.txt')
    # Check for correct interface output, return 1 if passed, 0 if failed
    if output != 'rank' or interface.mode != Interface.RANK_MODE or urls is None:
        return 0
    else:
        return 1


if __name__ == '__main__':
    test()
