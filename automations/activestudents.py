from config import settings
from utilities import datetimetools, helpers

import pandas

"""
Link to Admissions => Instruction notes
https://devcodecamp-my.sharepoint.com/:x:/p/carrie/EY3vGDJt73FKsqfdc8GIqvgBJtp-DmKJPs2BpbJf2jFbcA?e=lYJA73 

"""


def get_active_students_collection():
    return settings.client.get_collection_view(
        "https://www.notion.so/44aa227ba66f4174b06c0f5a1ddbdb5e?v=26ea1860a39f4aaa9d7b35ceee7e0691")


def change_standup_status_notstarted(course_type):
    # course_type is a string that corresponds to either Full-Time or Part-Time
    # This allows script to run for either class at a time. Call function twice for both
    # Excluding Cohort Finished to make sure they don't show up in Notion filters

    cv = get_active_students_collection()

    for row in cv.collection.get_rows():
        if row.standup_status != "Not Started" and row.course == course_type and row.standup_status != 'Cohort Finished' and row.standup_status != 'Dropped':
            row.standup_status = "Not Started"


def add_new_class_to_activestudents():
    # Uses pandas to parse CSV from Admissions into Python data structure
    # Gets the cohort information for students' class
    # Adds new row for each student and assigns properties based on parsed CSV data

    cv = get_active_students_collection()
    students = pandas.read_csv(r'/Users/jjvega/Desktop/Admissions to Instruction - April 26 - FT.csv')
    students_list = students.to_dict(
        'records')  # creates a List of dictionary items containing key-value pairs representing column -> value
    cohort = get_cohort()
    for student in students_list:
        row = cv.collection.add_row()
        row.name = student["Student Name"]
        row.contact_number = student["Contact Number"]
        row.emergency_contact_number = student["Emergency Contact Number"]
        row.emergency_contact_name = student["Emergency Contact Name"]
        row.admissions_notes = student["Admissions Notes"]
        row.cohort = cohort
        row.course = cohort.course_type


def get_cohort():
    # takes user input to determine if cohort exists
    # if the cohort does not exist, creates new cohort and returns to calling function
    # helper function for adding new students to Active Students
    cohorts = settings.client.get_collection_view(
        'https://www.notion.so/fb217eba60cf4a7c9aab62f561bd5077?v=827ed92c239a4e6e9484d960b2e39a06')
    user_input = input('What is the name of the cohort?')
    cohort = cohorts.collection.get_rows(search=user_input)
    if cohort:
        return settings.client.get_block(cohort[0].id)
    else:
        new_cohort = cohorts.collection.add_row()
        new_cohort.name = user_input
        new_cohort.course_type = helpers.get_course_type()
        new_cohort.dates = datetimetools.create_cohort_date(new_cohort.course_type)
        new_cohort.status = 'In Progress'
        return new_cohort
