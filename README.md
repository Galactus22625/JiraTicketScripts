# Jira Ticket Generator
Generate CSV files with generated Jira Ticket information to import into Jira

## Use
In Order to generate Projects, run 
>python3 GenerateCSV.py {[Project Name] [Project Key] [Number of Tickets]}

If you want to import to multiple projects, just repeat{[Project Name] [Project Key] [Number of Tickets]} for each project you want.  If you want to create a new project when you import, put values for project name and project key that are different from the values of your current projects <br />

To upload generated tickets to Jira, import the generated CSV file.  
[See Instructions on the Atlassian Website.](https://support.atlassian.com/jira-cloud-administration/docs/import-data-from-a-csv-file/)
[Alternate Instructions.](https://support.atlassian.com/jira-software-cloud/docs/import-data-to-a-software-project-using-a-csv-file/) <br />

You may need to use the old Jira UI to upload to multiple projects properly.  Do not map Issue ID for the old Jira UI. 
