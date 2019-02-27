'''
source: https://perceval.readthedocs.io/en/latest/_modules/perceval/backends/core/github.html, 
        https://perceval.readthedocs.io/en/latest/perceval.backends.core.html#module-perceval.backends.core.github
'''

from perceval.backends.core.github import ( GitHub, 
                                            CATEGORY_ISSUE, CATEGORY_PULL_REQUEST)
from datetime import datetime
from pprint import pprint

# Importing GitHub API Token 
from config import API_TOKEN 


REPOSITORY_NAME = "MeetInTheMiddle"

# Initializing the GitHub backend
github_backend = GitHub(owner="inishchith", api_token=API_TOKEN, repository=REPOSITORY_NAME)

print(github_backend.owner)

# Categories of information which can be retrieved
print(github_backend.categories)

print(github_backend.repository)
print(github_backend.origin)

# Analyzing Pull Request Information 

# Datetime range in which ISSUEs information is to be fetched
from_date = datetime(2019, 1, 1)
to_date = datetime(2019,2,2)

# Calling fetch method
range_issues = github_backend.fetch(category=CATEGORY_ISSUE, from_date=from_date, to_date=to_date)
range_issues_list = list(range_issues)
n_issues = len(range_issues_list)
print("NUMBER OF ISSUES: ", n_issues)

pprint(range_issues_list[n_issues-1])

for issue in range_issues_list:
    print("-"*100)
    
    # Issue Title
    print("TITLE: ",issue["data"]["title"])
    # Issue Closed at 
    print("CLOSED AT: ", issue["data"]["closed_at"])
    # Number of comments that the issue received
    print("No of comments: ", issue["data"]["comments"])
    
    # Issue creator details
    print("Issue Creator Username: ", issue["data"]["user"]["login"])
    print("\tUser Association type with repository: {association}\n\tCreated at: {created}\n\tComment: {comment}\n".format(association=issue["data"]["author_association"], comment=issue["data"]["body"],created=issue["data"]["created_at"]))
    
    # Issue comments details
    comments_data = issue["data"]["comments_data"]
    for comment in comments_data:
        print("Username: ", comment["user"]["login"])
        print("\tUser Association type with repository: {association}\n\tCreated at: {created}\n\tComment: {comment}\n".format(association=comment["author_association"], comment=comment["body"],created=comment["created_at"]))
    
    print("-"*100)

# Analyzing Pull Request Information 

# Datetime range in which PULL REQUESTs information is to be fetched
from_date = datetime(2018, 10, 1)
to_date = datetime(2019, 2, 10)

# Calling fetch method
pull_requests = github_backend.fetch(category=CATEGORY_PULL_REQUEST, from_date=from_date, to_date=to_date)
range_pull_request_list = list(pull_requests)
n_pulls = len(range_pull_request_list)
print("NUMBER OF PULL REQUESTS: ", n_pulls)

pprint(range_pull_request_list[n_pulls-1])

for pull_request in range_pull_request_list:
    print("-"*100)
    
    # Pull request Number and Title
    print("#{pull_request}: {title}".format(pull_request=pull_request["data"]["number"], title=pull_request["data"]["title"]))
    # Pull request state [ open / closed ]
    print("Pull Request State: ", pull_request["data"]["state"])
    # Merged True / False
    print("\nMerged: ", pull_request["data"]["merged"])
    
    if pull_request["data"]["merged"]:
        print("Merged at: ", pull_request["data"]["merged_at"])
    else:
        print("Closed at: ", pull_request["data"]["closed_at"])
    
    print("Number of comments: ", pull_request["data"]["comments"])
    print("\nAdditions: +{adds}\nDeletions: -{dels}".format(adds=pull_request["data"]["additions"], dels=pull_request["data"]["deletions"]))
    print("\nNumber of Commits: {commits}\nNumber of files changed: {file_changes}".format(commits=pull_request["data"]["commits"], file_changes=pull_request["data"]["changed_files"]))
    
    # Pull request creator details
    print("Username: ", pull_request["data"]["user"]["login"])
    print("\tUser Association type with repository: {association}\n\tCreated at: {created}\n\tComment: {comment}\n".format(association=pull_request["data"]["author_association"], comment=pull_request["data"]["body"], created=pull_request["data"]["created_at"]))
    
    print("-"*100)

