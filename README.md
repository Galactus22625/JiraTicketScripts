# Jira Ticket Scripts.
Generate CSV files with generated Jira Ticket information to import into Jira for volume testing using GenerateCSV.py <br />
Automatically update tickets with UpdateTickets.py using Jira api.


## Use (UpdateTickets.py)
To run update tickets, enter the following command.  
>python3 UpdateTickets.py --user [jira-username] --password [jira-api-key] --url [url-of-your-jira-site] --projkey [list of project keys]

This will take every ticket in the project and update the description and summary to something new.

To generate an api key for the passwrod field, follow the instructions here [Jira API KEY instuctions.](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)


## Use (GenerateCSV.py)
In Order to generate CSV File, run 
>python3 GenerateCSV.py {[Project Name] [Project Key] [Number of Tickets]}

If you want to import to multiple projects, just repeat{[Project Name] [Project Key] [Number of Tickets]} for each project you want.  If you want to create a new project when you import, put values for project name and project key that are different from the values of your current projects <br />

To upload generated tickets to Jira, import the generated CSV file.  
[See Instructions on the Atlassian Website.](https://support.atlassian.com/jira-cloud-administration/docs/import-data-from-a-csv-file/)
[Alternate Instructions.](https://support.atlassian.com/jira-software-cloud/docs/import-data-to-a-software-project-using-a-csv-file/) <br />

You may need to use the old Jira UI to upload to multiple projects properly.  Do not map Issue ID for the old Jira UI.   You may also run into Issues mapping Statuses into projects you already have in Jira if the mapping does not exist.  To avoid you can change the statuses fields to ones that match, or just dont map status.

If you want to upload a business project instead of a software project, change the project type category to business.  You may also need to alter the possible statuses.

## Further Updates Anyone can add
Create a createTickets.py to create tickets using the same api as updateTickets.py.  Can be used instead of GenerateCSV.py