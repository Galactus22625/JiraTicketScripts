import requests
import argparse

from GenerateCSV import validProjectKey

API_LINK = "/rest/api/2/"

def main():
    args = parseArguments()
    auth = (args.user, args.password)
    print(args.projkey)
    for project in args.projkey:
        updateProjectIssues(project)
    editIssue("ED-1", args.url, auth, "this is the new summary", "this is the new description")

def updateProjectIssues(projectKey):
    pass

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
        print(f"edited issue {issueKey}")
    else:
        print(f"Expected a response code of 200 or 204.  Received a response code of {response.status_code}")

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