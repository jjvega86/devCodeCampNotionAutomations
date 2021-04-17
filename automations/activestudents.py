from config import settings
from utilities import datetimetools

import pandas


"""
Link to Admissions => Instruction notes
https://devcodecamp-my.sharepoint.com/:x:/p/carrie/EY3vGDJt73FKsqfdc8GIqvgBJtp-DmKJPs2BpbJf2jFbcA?e=lYJA73 

"""


def get_active_students_collection():
    return settings.client.get_collection_view(
        "https://www.notion.so/44aa227ba66f4174b06c0f5a1ddbdb5e?v=26ea1860a39f4aaa9d7b35ceee7e0691")


def get_copy_active_students_collection():
    return settings.client.get_collection_view(
        "https://www.notion.so/05954b4edb354043803b8a49fabfa4f5?v=971140e72618440aa2d578c4e688b838")


def change_standup_status_notstarted(course_type):
    # course_type is a string that corresponds to either Full-Time or Part-Time
    # This allows script to run for either class at a time. Call function twice for both
    # Excluding Cohort Finished to make sure they don't show up in Notion filters

    cv = get_active_students_collection()

    for row in cv.collection.get_rows():
        if row.standup_status != "Not Started" and row.course == course_type and row.standup_status != 'Cohort Finished' and row.standup_status != 'Dropped':
            row.standup_status = "Not Started"


def add_new_class_to_activestudents():
    # need to get cohort block before adding students
    cv = get_copy_active_students_collection()
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


def get_course_type():
    user_input = input('What course type? 1 = Full Time, 2 = Part Time')
    if user_input == '1':
        return 'Full Time'
    elif user_input == '2':
        return 'Part Time'
    else:
        get_course_type()


def get_cohort():
    cohorts = settings.client.get_collection_view(
        'https://www.notion.so/fb217eba60cf4a7c9aab62f561bd5077?v=827ed92c239a4e6e9484d960b2e39a06')
    user_input = input('What is the name of the cohort?')
    cohort = cohorts.collection.get_rows(search=user_input)
    if cohort:
        return settings.client.get_block(cohort[0].id)
    else:
        new_cohort = cohorts.collection.add_row()
        new_cohort.name = user_input
        new_cohort.course_type = get_course_type()
        new_cohort.dates = datetimetools.create_date(new_cohort.course_type)
        new_cohort.status = 'In Progress'
        return new_cohort



