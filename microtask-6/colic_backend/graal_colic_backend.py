from graal.backends.core.colic import CoLic, CATEGORY_COLIC_NOMOS, CATEGORY_COLIC_SCANCODE
from pprint import pprint
import datetime

# URL for the git repo to analyze
REPOSITORY_URL = "http://github.com/inishchith/MeetInTheMiddle"

# directory where to mirror the repo
REPO_DIR = "MeetInTheMiddle"

# Range of commits to fetched
from_date = datetime.datetime(2018, 12, 10)
to_date = datetime.datetime(2018, 12, 12)

def fetch_license_info(executable_path, colic_category):
    # CoLic object initialization
    colic = CoLic(uri=REPOSITORY_URL, exec_path=executable_path, git_path=REPO_DIR)

    # fetch all commits within range from_date <= date <= to_date
    commits = list(colic.fetch(from_date=from_date, to_date=to_date, category=colic_category))

    n_commits = len(commits)
    print("Number of commits: ", n_commits)
    print()

    commit_with_license = commits[1]
    
    print(commit_with_license["data"]["Author"])
    print(commit_with_license["data"]["CommitDate"])
    print(commit_with_license["data"]["message"])
    pprint(commit_with_license["data"]["analysis"])

# nomos executable path
NOMOS_PATH = "/Users/Nishchith/GitHub/CHAOSS/chaoss-mts-init/microtask-6/executables/fossology/src/nomos/agent/nomossa"
fetch_license_info(executable_path=NOMOS_PATH, colic_category=CATEGORY_COLIC_NOMOS)

# scancode executable path
SCANCODE_PATH = "/Users/Nishchith/GitHub/CHAOSS/chaoss-mts-init/microtask-6/executables/scancode-toolkit-3.0.0/scancode"
fetch_license_info(executable_path=SCANCODE_PATH, colic_category=CATEGORY_COLIC_SCANCODE)