# API source: https://archive.softwareheritage.org/api/1/
# imports

import requests
from pprint import pprint

# base requet url
base_url = "https://archive.softwareheritage.org"

# setting urls for origin and visits endpoints
origin_endpoint = "/api/1/origin/git/url/{origin_url}"
visits_endpoint = "/api/1/origin/{origin_id}/visits/"

# getting repository url from user
REPOSITORY_URL = input("ENTER REPOSITORY URL: ")

# making a GET request to the origin endpoint
origin_endpoint_url = base_url + \
    origin_endpoint.format(origin_url=REPOSITORY_URL)
request = requests.get(origin_endpoint_url)
print("Status code: ", request.status_code)

if request.status_code == 200:
    # Found the origin in archive
    print("Found origin in Software Heritage archive.")
    print()
    json_data = request.json()
    origin_id = json_data["id"]

    # making a GET requets to the visits endpoint using the origin_id of the
    # found archive
    visits_endpoint_url = base_url + \
        visits_endpoint.format(origin_id=origin_id)
    visit_request = requests.get(visits_endpoint_url)

    if visit_request.status_code == 200:
        # getting the visit history
        visits = visit_request.json()
        # picking the lates one
        print(visits)
        last_visit = visits[0]
        print("Last visits data: ")
        pprint(last_visit)
        print("\nLast visit date: ", last_visit["date"])
    else:
        print("No visits found. ")

elif request.status_code == 404:
    # Cannot find origin in archive
    print("Requested origin cannot be found in Software Heritage archive. ")
