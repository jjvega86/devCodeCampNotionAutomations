# NotionAutomations
2.0 version of scripting libraries to automate devCodeCamp Notion processes. 
Interfacing with Unofficial client for Notion API - https://github.com/jamalex/notion-py

# Notes

config contains initial client setup. This is ignored from GitHub for security purposes. 

automations contains a script file for each component of platform

utilities gathers commonly used functions across all components (e.g date conversions, file reading, etc)

Modified venv/lib/notion/store.py and venv/lib/notion/client.py -- set "limit" value to 100
This fixes a bug where requests for pages/collections of a certain size will return a 404 response
https://stackoverflow.com/questions/66513210/cant-get-page-title-from-notion-using-api

# TO DO
## General
    -- Error Handling
    -- Unit Tests
    -- Shell script for command line interface
    -- Documentation
    -- Refactor scripts to use user_interface functions

## Clockify API Integration
### Reporting
    -- Pull Clockify weekly time tracking report, add avg time calcs, send to Notion as entry in Instructor Time Tracking
    
### Grading
    -- Create new project in Clockify when assignment to grade is created in Notion
### Junior Developer Standups
    -- Create new project in Clockify when a new student is added to Active Students

## Notion Automations
### courses.py
    -- Take in Excel course templates -> update same course in Notion
    -- Create a duplicate of existing courses
### activestudents.py
### grading.py
    -- Add new grading templates for new classes
    -- Pre-load all assignments in Grading. Load with class templates and set to automatically appear a week before assignment submitted\
    -- Automatic reminders to system admins for pending grading

### classschedules.py
    -- Create new schedules for new classes 
    -- automatically add dates for all events, accounting for holidays and weekends, based on class start

## Wish List
    -- Scrape OneDrive account for matching lecture/user story/resource files and add to relevant courses/events
    -- Listen for In Progress status on Notion, automatically start Clockify timer