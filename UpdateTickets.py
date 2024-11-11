import requests
import argparse

from GenerateCSV import validProjectKey

API_LINK = "/rest/api/2/"

def main():
    args = parseArguments()
    auth = (args.user, args.password)
    editIssue("ED-1", args.url, auth)
    pass

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type = str, help = "url of your jira site", required = True)
    parser.add_argument('--user', type = str, help = "your jira username", required = True)
    parser.add_argument('--password', type = str, help = "your jira api key", required = True)
    parser.add_argument('--projkey', type = str, nargs='+', help = "project keys that you want updated", required = False)
    args = parser.parse_args()
    return args
def editIssue(issueKey, url, auth):
    apiUrl = url + API_LINK + "issue/" + issueKey

    updateJson = {
        "fields": {"summary": "What fun"}
    }
    response = requests.put(apiUrl, json = updateJson, auth = auth)
    assert (response.status_code == 200 or response.status_code == 204), f"Expected a response code of 200 or 204.  Received a response code of {response.status_code}"

if __name__ == "__main__":
    main()