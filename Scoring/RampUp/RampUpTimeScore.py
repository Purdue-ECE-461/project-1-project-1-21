#!/usr/bin/env python3x

# RampUpTimeScore.py
# Created by Charles Pisciotta
# September 15, 2021
# Written by Jason Lei
# September 28, 2021

from Scoring.ScoreBaseClass import ScoreBaseClass
from git import Repo
import os
import shutil


class RampUpTimeScore(ScoreBaseClass):
    def __init__(self, package):
        super().__init__(package)
        self.forks_count = package.forks_count
        self.has_wiki = package.has_wiki
        self.has_pages = package.has_pages
        self.package_name = package.name
        self.clone_url = package.clone_url

    def score(self):
        # Get readme.md score
        readme_score = self.getReadmeScore()

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
        scores = [fork_score, wiki_page_score, readme_score]

        
        return sum(scores) / len(scores)

    def getReadmeScore(self):
        # Clone and check repo for readme.md
        readme_score = 0
        repos_dir = "./Repos/"
        clone_dir = repos_dir + str(self.package_name)
        readme_names = ["/README.md", "/Readme.md", "/readme.md", "/ReadMe.md", "/ReadMe.markdown", "/README.markdown", "/Readme.markdown", "/readme.markdown","/readme", "/README", "/Readme", "/readme.txt",  "/README.txt", "/Readme.txt"]
        try:
            # Clones repo locally
            os.mkdir(repos_dir)
            os.mkdir(clone_dir)
            Repo.clone_from(self.clone_url, clone_dir)
            # Check directory for a readme.md file
            for name in readme_names:
                if os.path.isfile(clone_dir + name):
                    readme_score = 1
        except:
            pass

        # Remove cloned repo
        try:
            shutil.rmtree(repos_dir)
        except:
            pass

        return readme_score
