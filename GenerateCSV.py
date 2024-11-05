import csv
import sys
import os
import re
import random
        
        
InputFields = ["CSV File Name", "Numbr of Issues"]

def main():
    csvFields = ["Project Name", "Project Key", "Issue Type", "Status", "Issue ID", "Summary", "Project Type"]
    issueTypes = ["Story", "Task", "Bug", "Epic"]
    statuses = ["To Do", "In Progress", "Ready For Launch"]

    csvName, projectNames, projectKeys, numIssues = processCommandLineArguments()
    csvName = csvName + ".csv"
    numIssues = [int(num) for num in numIssues]

    if os.path.exists(csvName) == True:
        while True:
            answer = input("A file named " + csvName + "already exists.  Are you sure you want to overwrite it? [y/n]").lower()
            if answer == 'y':
                break
            elif answer == 'n':
                exit()

    with open(csvName, 'w', newline = '') as file:
        writer = csv.writer(file)

        writer.writerow(csvFields)

        for projectName, projectKey, issues in zip(projectNames, projectKeys, numIssues):
            for issueNumber in range(1, issues + 1):
                writer.writerow([projectName, projectKey, random.choice(issueTypes), random.choice(statuses), str(issueNumber), "This is a well written summary of issue " + str(issueNumber), "software"])

def validProjectKey(projectKey):
    keyPattern = re.compile("[^A-Z0-9]")
    if re.search(keyPattern, projectKey):
       return False
    return True

def processCommandLineArguments():
    projectNames = []
    projectKeys = []
    numIssues = []
    
    if len(sys.argv)%3 -2 != 0 or len(sys.argv) < 5:
        fields = ""
        for field in InputFields:
            fields = fields + "[" + field + "] "
        raise ValueError("run python3 GenerateCSV.py {[Project Name] [Project Key] [Number of Tickets]}. See README.md")

    csvName = sys.argv[1]
    numberOfProjects = int((len(sys.argv) -2) /3)
    for project in range(numberOfProjects):
        if not validProjectKey(sys.argv[3*project + 3]):
            raise ValueError("Project Keys must consist of Capital Letters and Numbers Only")
        if not sys.argv[3*project + 4].isnumeric():
            raise ValueError("Number of Issues must be a number")
        projectNames.append(sys.argv[3*project + 2])
        projectKeys.append(sys.argv[3*project + 3])
        numIssues.append(sys.argv[3*project + 4])

    return csvName, projectNames, projectKeys, numIssues


if __name__ == "__main__":
    main()