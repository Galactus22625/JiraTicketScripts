import requests
import argparse
import logging
import string
import random
import time

from GenerateCSV import validProjectKey

API_LINK = "/rest/api/2/"

logging.basicConfig(filename='UpdateTickets.log',level=logging.INFO)


def main():
    args = parseArguments()
    auth = (args.user, args.password)
    for project in args.projkey:
        if validProjectKey(project):
            updateProjectIssues(project, args.url, auth)
        else:
            logging.error(f"{project} is not a valid project key.  Projects keys must consist of only Uppercase Letters and Numbers.")
            print(f"{project} is not a valid project key.  Projects keys must consist of only Uppercase Letters and Numbers.")


def updateProjectIssues(projectKey, url, auth):
    result = getPageData(projectKey, url, auth)
    if result == None:
        return
    data, totalIssues, maxResults = result
    startAt = 0
    ticketsEdited = 0

    while startAt < totalIssues:
        apiUrl = url + API_LINK + "search?jql= project in (\"" + projectKey +"\")" + "&startAt=" + str(startAt)
        startAt += maxResults
        response = requests.get(apiUrl, auth = auth)
        if response.status_code != 200:
            logging.error(f"Expected a response code of 200.  Received a response code of {response.status_code} for page number {startAt/maxResults}")
            print(f"Unable to access project: {projectKey} page number {startAt/maxResults}, please see logs")
            return

        data = response.json()
        issues = data["issues"]
        letters = string.ascii_lowercase + " "
        batch = 0
        for issue in issues:
            key = issue["key"]
            description = issue["fields"]["description"]
            summary = issue["fields"]["summary"]

            newDescription = ''.join(random.choice(letters) for i in range(random.randint(5, 2000))) + "\n The Description has been Replaced."
            newSummary = "This is the new summary of issue " + key
            result = editIssue(key, url, auth, newSummary, newDescription)
            if result > 0:
                batch+= result
                ticketsEdited += result
                print(f"Succesfully edited {ticketsEdited} tickets in project {projectKey}", end='\r')
        logging.debug(f"Processed a batch of {batch} tickets.")
    print(f"Succesfully edited a total of {ticketsEdited} tickets in project {projectKey}")
    logging.info(f"Succesfully edited {ticketsEdited} tickets in project {projectKey}")


def editIssue(issueKey, url, auth, newSummary, newDescription):
    apiUrl = url + API_LINK + "issue/" + issueKey

    updateJson = {
        "fields": {
            "summary": newSummary,
            "description": newDescription
            }
    }
    attempt = 0
    sleepvalues = [1, 5, 10, 30, 60, 200]
    while attempt < len(sleepvalues):
        response = requests.put(apiUrl, json = updateJson, auth = auth)
        if (response.status_code == 200 or response.status_code == 204):
            logging.debug(f"edited issue {issueKey}")
            return 1
        elif response.statu_code == 429:
            x = sleepvalues[attempt]
            time.sleep(x)
        else:
            logging.error(f"Expected a response code of 200 or 204.  Received a response code of {response.status_code}")
            print("Error editing an issue, see logs")
            return 0


def getPageData(projectKey, url, auth):
    apiUrl = url + API_LINK + "search?jql= project in (\"" + projectKey +"\")"
    response = requests.get(apiUrl, auth = auth)
    if response.status_code != 200:
        logging.error(f"Expected a response code of 200.  Received a response code of {response.status_code}")
        print(f"Unable to access project: {projectKey}, please see logs")
        return None
    data = response.json()
    totalIssues = data["total"]
    maxResults = data["maxResults"]
    return data, totalIssues, maxResults


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