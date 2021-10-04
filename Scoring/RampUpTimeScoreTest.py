#!/usr/bin/env python3

# RampUpTimeScoreTest.py
# Created by Jason Lei
# October 1, 2021
import RampUpTimeScore


# Define temporary package class to test this function on
class RampUpTestPackage:
    def __init__(self, stargazers, watchers, forks):
        self.stargazers_count = stargazers
        self.watchers_count = watchers
        self.forks_count = forks


# RampUpTimeScore serves to test the functionality of the score function in RampUpScore
def test():
    tests = [test1, test2, test3, test4, test5]
    num_tests = len(tests)
    num_passed = 0

    # Perform tests
    for t in tests:
        num_passed += t()

    # Return results
    print(num_passed, num_tests)
    return num_passed, num_tests


# Tests score for a package with 0 stargazers, 0 watchers, and 0 forks
def test1():
    stargazers = 0
    watchers = 0
    forks = 0
    package = RampUpTestPackage(stargazers, watchers, forks)
    ruts = RampUpTimeScore.RampUpTimeScore(package)

    score = ruts.score()
    if score != 0:
        return 0
    else:
        return 1


# Tests score for a package with 50 stargazers, 50 watchers, and 50 forks
def test2():
    stargazers = 50
    watchers = 50
    forks = 50
    package = RampUpTestPackage(stargazers, watchers, forks)
    ruts = RampUpTimeScore.RampUpTimeScore(package)
    score = ruts.score()
    if score != 0.25:
        return 0
    else:
        return 1


# Tests score for a package with 500 stargazers, 300 watchers, and 500 forks
def test3():
    stargazers = 500
    watchers = 300
    forks = 500
    package = RampUpTestPackage(stargazers, watchers, forks)
    ruts = RampUpTimeScore.RampUpTimeScore(package)
    score = ruts.score()
    if score != 0.5:
        return 0
    else:
        return 1


# Tests score for a package with 5000 stargazers, 700 watchers, and 5000 forks
def test4():
    stargazers = 5000
    watchers = 700
    forks = 5000
    package = RampUpTestPackage(stargazers, watchers, forks)
    ruts = RampUpTimeScore.RampUpTimeScore(package)
    score = ruts.score()
    if score != 0.75:
        return 0
    else:
        return 1


# Tests score for a package with 10000 stargazers, 1000 watchers, and 10000 forks
def test5():
    stargazers = 10000
    watchers = 1000
    forks = 10000
    package = RampUpTestPackage(stargazers, watchers, forks)
    ruts = RampUpTimeScore.RampUpTimeScore(package)
    score = ruts.score()
    if score != 1:
        return 0
    else:
        return 1


if __name__ == '__main__':
    test()
