#!/usr/bin/env python3

# RampUpTimeScoreTests.py
# Created by Jason Lei
# October 1, 2021
# Modified by Charles Pisciotta

import unittest
from RampUpTimeScore import RampUpTimeScore


# Define temporary package class to test this function on
class RampUpTestPackage:
    def __init__(self, stargazers, watchers, forks):
        self.stargazers_count = stargazers
        self.watchers_count = watchers
        self.forks_count = forks


class RampUpTimeScoreTests(unittest.TestCase):

    def test_0_correctness(self):
        mock = RampUpTestPackage(stargazers=0, watchers=0, forks=0)
        sut = RampUpTimeScore(mock)
        score = sut.score()
        self.assertEqual(score, 0)

    def test_0_25_correctness(self):
        mock = RampUpTestPackage(stargazers=50, watchers=50, forks=50)
        sut = RampUpTimeScore(mock)
        score = sut.score()
        self.assertEqual(score, 0.25)

    def test_0_5_correctness(self):
        mock = RampUpTestPackage(stargazers=500, watchers=300, forks=500)
        sut = RampUpTimeScore(mock)
        score = sut.score()
        self.assertEqual(score, 0.5)

    def test_0_75_correctness(self):
        mock = RampUpTestPackage(stargazers=5000, watchers=700, forks=5000)
        sut = RampUpTimeScore(mock)
        score = sut.score()
        self.assertEqual(score, 0.75)

    def test_1_correctness(self):
        mock = RampUpTestPackage(stargazers=10001, watchers=1001, forks=10001)
        sut = RampUpTimeScore(mock)
        score = sut.score()
        self.assertEqual(score, 1)



if __name__ == '__main__':
    unittest.main()
