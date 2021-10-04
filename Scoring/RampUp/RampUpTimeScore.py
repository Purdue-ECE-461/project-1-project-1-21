# RampUpTimeScore.py
# Created by Charles Pisciotta
# September 15, 2021
# Written by Jason Lei
# September 28, 2021

from Scoring.ScoreBaseClass import ScoreBaseClass


class RampUpTimeScore(ScoreBaseClass):
    def __init__(self, package):
        super().__init__(package)
        self.forks_count = package.forks_count
        self.has_wiki = package.has_wiki
        self.has_pages = package.has_pages

    def score(self):
        # Determine a sub-score for number of forks
        if self.forks_count > 10000:
            fork_score = 1
        elif self.forks_count > 1000:
            fork_score = 0.75
        elif self.forks_count > 100:
            fork_score = 0.5
        elif self.forks_count > 10:
            fork_score = 0.25
        else:
            fork_score = 0

        # Determine a sub-score for the presence of a wiki or pages
        if self.has_wiki:
            wiki_page_score = 1
        elif self.has_pages:
            wiki_page_score = 0.5
        else:
            wiki_page_score = 0

        # Final score is a weighted avereage of the two
        scores = [forks_score, wiki_page_score]
        return sum(scores) / len(scores)
