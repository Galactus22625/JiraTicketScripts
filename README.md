# Jira Ticket Generator
Generate CSV files with generated Jira Ticket information to import into Jira for volume testing

## Use
In Order to generate Projects, run 
>python3 GenerateCSV.py {[Project Name] [Project Key] [Number of Tickets]}

If you want to import to multiple projects, just repeat{[Project Name] [Project Key] [Number of Tickets]} for each project you want.  If you want to create a new project when you import, put values for project name and project key that are different from the values of your current projects <br />

To upload generated tickets to Jira, import the generated CSV file.  
[See Instructions on the Atlassian Website.](https://support.atlassian.com/jira-cloud-administration/docs/import-data-from-a-csv-file/)
[Alternate Instructions.](https://support.atlassian.com/jira-software-cloud/docs/import-data-to-a-software-project-using-a-csv-file/) <br />

You may need to use the old Jira UI to upload to multiple projects properly.  Do not map Issue ID for the old Jira UI.   You may also run into Issues mapping Statuses into projects you already have in Jira if the mapping does not exist.  To avoid you can change the statuses fields to ones that match, or just dont map status.

If you want to upload a business project instead of a software project, change the project type category to business.  You may also need to alter the possible statuses.
