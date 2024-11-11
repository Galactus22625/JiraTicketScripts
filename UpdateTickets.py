import requests
import argparse
import logging
import string
import random

from GenerateCSV import validProjectKey

API_LINK = "/rest/api/2/"

logging.basicConfig(filename='UpdateTickets.log',level=logging.INFO)

def main():
    args = parseArguments()
    auth = (args.user, args.password)
    for project in args.projkey:
        updateProjectIssues(project, args.url, auth)

def updateProjectIssues(projectKey, url, auth):
    apiUrl = url + API_LINK + "search?jql= project in (\"" + projectKey +"\")"
    response = requests.get(apiUrl, auth = auth)
    if response.status_code != 200:
        logging.error(f"Expected a response code of 200.  Received a response code of {response.status_code}")
        print(f"Unable to access project: {projectKey}, please see logs")
        return

    data = response.json()
    issues = data["issues"]
    letters = string.ascii_lowercase + " "
    ticketsEdited = 0
    for issue in issues:
        key = issue["key"]
        description = issue["fields"]["description"]
        summary = issue["fields"]["summary"]

        newDescription = ''.join(random.choice(letters) for i in range(random.randint(5, 2000))) + "\n The Description has been Replaced."
        newSummary = summary + ". We now have a new summary."
        ticketsEdited += editIssue(key, url, auth, newSummary, newDescription)

    print(f"Succesfully edited {ticketsEdited} tickets in project {projectKey}")
    logging.info(f"Succesfully edited {ticketsEdited} tickets in project {projectKey}")

def editIssue(issueKey, url, auth, newSummary, newDescription):
    apiUrl = url + API_LINK + "issue/" + issueKey

    updateJson = {
        "fields": {
            "summary": newSummary,
            "description": newDescription
            }
    }
    response = requests.put(apiUrl, json = updateJson, auth = auth)
    if (response.status_code == 200 or response.status_code == 204):
        logging.debug(f"edited issue {issueKey}")
        return 1
    else:
        logging.error(f"Expected a response code of 200 or 204.  Received a response code of {response.status_code}")
        print("Error editing an issue, see logs")
        return 0

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type = str, help = "url of your jira site", required = True)
    parser.add_argument('--user', type = str, help = "your jira username", required = True)
    parser.add_argument('--password', type = str, help = "your jira api key", required = True)
    parser.add_argument('--projkey', type = str, nargs='+', help = "project keys that you want updated", required = True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()