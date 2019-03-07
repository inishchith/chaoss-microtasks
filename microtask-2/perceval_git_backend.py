'''
source: https://perceval.readthedocs.io/en/latest/_modules/perceval/backends/core/git.html,
        https://perceval.readthedocs.io/en/latest/perceval.backends.core.html#module-perceval.backends.core.git
'''
from perceval.backends.core.git import Git
from datetime import datetime
from pprint import pprint

REPOSITORY_URL = "https://github.com/inishchith/MeetInTheMiddle.git"
REPO_DIR = "./tmp/MeetInTheMiddle"

# Initializing the Git backend
git_backend = Git(uri=REPOSITORY_URL, gitpath=REPO_DIR)

# Range of dates in which commits are to be fetched
from_date = datetime(2018, 10, 1)
to_date = datetime(2019, 2, 5)

# Repo Branches from which commits to be fetched [ 2/3 ]
repo_branches = ["master", "develop"]


# Calling fetch method
# The method retrieves from a Git repository or a log file a list of
# commits. Commits are returned in the same order they were obtained.
range_commits = git_backend.fetch(
    branches=repo_branches, from_date=from_date, to_date=to_date)
range_commits_list = list(range_commits)
n_commits = len(range_commits_list)
print("NUMBER OF COMMITS: ", n_commits)


last_commit = range_commits_list[n_commits - 1]
pprint(last_commit)
pprint(range_commits_list[n_commits - 1].keys())

for commit in range_commits_list:
    print("COMMIT DATE: {commit_date}\nAUTHOR: {author_name}\nCOMMIT MESSAGE: {commit_message}".format(commit_date=commit[
          "data"]["CommitDate"], author_name=commit["data"]["Author"], commit_message=commit["data"]["message"]))
    print()


for commit in range_commits_list[-5:]:
    print("COMMIT MESSAGE: {commit_message}\n".format(
        commit_message=commit["data"]["message"]))
    for change_file in commit['data']['files']:
        print("\tFILE NAME: {file_name}\n\tADDITIONS: +{additions}\n\tDELETIONS: -{deletions}\n".format(
            file_name=change_file['file'], additions=change_file['added'], deletions=change_file['removed']))
