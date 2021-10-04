# LicenseCompatibilityScore.py
# Created by Charles Pisciotta
# September 15, 2021
# Edited by Jason Lei
# October 3, 2021

from Scoring.ScoreBaseClass import ScoreBaseClass


class LicenseCompatibilityScore(ScoreBaseClass):

    def __init__(self, package):
        super().__init__(package)

    def score(self):
        # Pull license information from package
        license = self.package.license

        # If package has no license at all, give a score of 0.
        if license is None:
            return 0

        licenseName = str(license['name'])

        # List of licenses supported, i.e. GNU LGPLv2.1 or higher
        supported_licenses = ['GNU Lesser General Public License', 'Lesser General Public License', 'LGPL',
                              'General Public License', 'GPL']

        # Check if this package has any of the supported licenses. If yes, give license score of 1.
        for l in supported_licenses:
            if l.lower() in licenseName.lower():
                return 1

        # Return a score of 0.1 if there is a license, but just an unsupported one. (May need readjustment for use)
        return 0.5
