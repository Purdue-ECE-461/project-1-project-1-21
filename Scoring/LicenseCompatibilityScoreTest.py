#!/usr/bin/env python3

# LicenseCompatibilityScoreTest.py
# Created by Jason Lei
# October 3, 2021
import LicenseCompatibilityScore


# Define temporary package class to test this function on
class LicenseTestPackage:
    def __init__(self, license_name, isNotNone=True):
        if isNotNone:
            self.license = {'name': license_name}


# LicenseCompatibilityScoreTest serves to test the functionality of the score function in LicenseCompatibilityScore
def test():
    tests = [test1, test2, test3]
    num_tests = len(tests)
    num_passed = 0

    # Perform tests
    for t in tests:
        num_passed += t()

    # Return results
    print(num_passed, num_tests)
    return num_passed, num_tests


# Tests score for a package with a package with no license
def test1():
    package = LicenseTestPackage('', isNotNone=False)
    lcs = LicenseCompatibilityScore.LicenseCompatibilityScore(package)

    score = lcs.score()
    if score != 0:
        return 0
    else:
        return 1


# Tests score for a package with an unsupported license
def test2():
    package = LicenseTestPackage('MIT License')
    lcs = LicenseCompatibilityScore.LicenseCompatibilityScore(package)

    score = lcs.score()
    if score != 0:
        return 0
    else:
        return 1


# Tests score for a package with a supported license
def test3():
    package = LicenseTestPackage('GPLv3')
    lcs = LicenseCompatibilityScore.LicenseCompatibilityScore(package)

    score = lcs.score()
    if score != 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    test()
