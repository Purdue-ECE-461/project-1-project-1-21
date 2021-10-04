# OutputInterfaceTest.py
# Created by Jason Lei
# October 1, 2021

from Interface.Interface import Interface
from Interface.OutputInterface import OutputInterface
from ScoreCard.PackageScoreCard import PackageScoreCard


# OutputInterfaceTest serves to test the OutputInterface class. Will return a list of form num_passed, num_tests
def test():
    ii = OutputInterface()
    tests = [test1, test2, test3]
    num_tests = len(tests)
    num_passed = 0

    # Perform tests
    for t in tests:
        num_passed += t(ii)

    # Return results
    print(num_tests, num_passed)
    return num_passed, num_tests


# Tests the install mode output
def test1(interface):
    interface.mode = Interface.INSTALL_MODE
    output = interface.formatInstallResults(10)

    # Check for correct interface output, return 1 if passed, 0 if failed
    if output != """10 dependencies installed...""" or interface.mode != Interface.INSTALL_MODE:
        return 0
    else:
        return 1


# Tests the test mode input
def test2(interface):
    interface.mode = Interface.TEST_MODE
    output = interface.formatTestResults([5, 5])
    # Check for correct interface output, return 1 if passed, 0 if failed
    if output != """Total: 5\nPassed: 5\n5/5 test cases passed. 100% line coverage achieved.""" or interface.mode != Interface.TEST_MODE:
        return 0
    else:
        return 1


# Tests the rank mode input
def test3(interface):
    testScores = PackageScoreCard(url="fakeurl",
                                  total_score=0.5,
                                  bus_factor_score=0.5,
                                  correctness_score=0.5,
                                  license_score=0.5,
                                  ramp_up_score=0.5,
                                  responsiveness_score=0.5)
    output = interface.formatRankResults(testScores)

    # Check for correct interface output, return 1 if passed, 0 if failed
    if output != testScores.toString() or interface.mode != Interface.RANK_MODE:
        return 0
    else:
        return 1


if __name__ == '__main__':
    test()
