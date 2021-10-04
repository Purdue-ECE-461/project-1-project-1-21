import unittest
from Scoring.LicenseCompatibility.LicenseCompatibilityScore import LicenseCompatibilityScore

class LicenseTestPackage:
    def __init__(self, license):
        self.license = license


class LicenseCompatibilityTests(unittest.TestCase):

    def test_no_license(self):
        mock = LicenseTestPackage(None)
        sut = LicenseCompatibilityScore(mock)
        score = sut.score()
        self.assertEqual(score, 0)

    def test_no_license(self):
        mock = LicenseTestPackage('{\"license\":{\"name\":\"MIT License\"}')
        sut = LicenseCompatibilityScore(mock)
        score = sut.score()
        self.assertEqual(score, 1)

    def test_no_license(self):
        mock = LicenseTestPackage('{\"license\":{\"name\":\"GPLv3\"}')
        sut = LicenseCompatibilityScore(mock)
        score = sut.score()
        self.assertEqual(score, 1)

if __name__ == '__main__':
    unittest.main()
