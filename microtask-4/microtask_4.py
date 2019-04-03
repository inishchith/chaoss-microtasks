# API source: https://archive.softwareheritage.org/api/1/
# imports

import requests
from pprint import pprint

# base request url
base_url = "https://archive.softwareheritage.org/api/1"

# setting urls for origin and visits endpoints
origin_endpoint = "/origin/git/url/{origin_url}"
visits_endpoint = "/origin/{origin_id}/visits/"

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

    # making a GET request to the visits endpoint using the origin_id of the
    # found archive
    visits_endpoint_url = base_url + \
        visits_endpoint.format(origin_id=origin_id)
    visit_request = requests.get(visits_endpoint_url)

    if visit_request.status_code == 200:
        # getting the visit history
        visits = visit_request.json()
        # picking the lates one
        last_visit = visits[0]
        print("Last visits data: ")
        pprint(last_visit)
        print("\nLast visit date: ", last_visit["date"])
        print()
    else:
        print("No visits found. ")
        print()

elif request.status_code == 404:
    # Cannot find origin in archive
    print("Requested origin cannot be found in Software Heritage archive. ")

# getting directory id of the repository from the user and Defining /directory endpoint
DIRECTORY_ID = input("ENTER DIRECTORY ID: ")
directory_endpoint = base_url + "/directory/" + DIRECTORY_ID

request = requests.get(directory_endpoint)

if request.status_code == 200:
    # Scaning for License Information
    print("Found directory information in Software Heritage archive.")
    
    # get the json return 
    directory_json_data = request.json()
    sha1_checksum = None
    
    # Find license metadata: sha1 checksum
    for item in directory_json_data:
        if item["name"] == "license":
            sha1_checksum = item["checksums"]["sha1"]
            break

    if sha1_checksum:
        # defining license endpoint
        license_endpoint = base_url + "/content/sha1:" + sha1_checksum + "/license/"
        
        # get request to the license endpoint
        request = requests.get(license_endpoint)
        license_json_data = request.json()
        
        print("Licenses: ",license_json_data["facts"][0]["licenses"])
        print("License Information extraction tool: ",license_json_data["facts"][0]["tool"]["name"])
    else:
        print("No license found in the directory")

elif request.status_code == 404:
    print("Directory with ID: {directory_id} cannot be found".format(directory_id=DIRECTORY_ID))
