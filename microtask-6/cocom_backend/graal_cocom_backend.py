
from graal.backends.core.cocom import CoCom, FileAnalyzer
from pprint import pprint
from datetime import datetime
import os

# URL for the git repo to analyze
REPOSITORY_URL = "http://github.com/inishchith/MeetInTheMiddle"

# directory where to mirror the repo
REPO_DIR = "MeetInTheMiddle"

# Cocom object initialization
cocom = CoCom(uri=REPOSITORY_URL, git_path=REPO_DIR)

from_date = datetime(2018, 12, 12)
to_date = datetime(2018, 12, 30)

# fetch all commits within range from_date <= date <= to_date
# uses perceval backend to fetch commits and performs analysis on the file present in worktreepath
commits = [commit for commit in cocom.fetch(from_date=from_date,
                                            to_date=to_date)]

n_commits = len(commits)
print("Number of commits: ", n_commits)

first_commit = commits[0]
pprint(first_commit)
print(first_commit['data']['Author'])
print(first_commit['data']['CommitDate'])
print(first_commit['data']['message'])


# Check analysis attribute i.e analysis produced by graal via lizard
print("-"*100)
for commit in commits:
    print("Commit Message:",commit['data']['message'])
    for change in commit['data']['analysis']:
        if change["ext"] in FileAnalyzer.ALLOWED_EXTENSIONS:
            print("File Name: ",change["file_path"])
            print("\tAverage Cyclomatic Complexity (ccn): ",change["avg_ccn"])
            print("\tAverage Lines of code: ",change["avg_loc"])
            print("\tAverage Tokens: ",change["avg_tokens"])
            print("\tBlanks: ",change["blanks"])
            print("\tCyclomatic Complexity (ccn): ",change["ccn"])
            print("\tNumber of Comments: ",change["comments"])
            print("\tExtension: ",change["ext"])
            print("\tLines of code: ",change["loc"])
            print("\tNumber of functions: ",change["num_funs"])
            print("\tTokens: ",change["tokens"])
        else:
            print("** Analysis cannot be performed for: ", change["file_path"])
        print()
    print("-"*100)