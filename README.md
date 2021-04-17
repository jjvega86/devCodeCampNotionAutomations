# NotionAutomation
2.0 version of scripting libraries to automate devCodeCamp Notion processes

# Notes

See examples.py for snippets of functionality.

config contains initial client setup. This is ignored from GitHub for security purposes. For more information, see documentation
for notion.py: https://github.com/jamalex/notion-py

automations contains a script file for each component of platform

utilities gathers commonly used functions across all components (e.g date conversions, file reading, etc)

Modified venv/lib/notion/store.py and venv/lib/notion/client.py -- set "limit" value to 100
This fixes a bug where requests for pages/collections of a certain size will return a 404 response
https://stackoverflow.com/questions/66513210/cant-get-page-title-from-notion-using-api

# TO DO
## grading.py
    -- Add new grading templates for new classes
    -- Pre-load all assignments in Grading. Load with class templates and set to automatically appear a week before assignment submitted\
    -- Automatic reminders to system admins for pending grading

##class_schedules.py
    -- Create new schedules for new classes; automatically add dates for all events, accounting for holidays and weekends

##onedrive
    -- Scrape OneDrive account for matching lecture/user story/resource files and add to relevant courses/events