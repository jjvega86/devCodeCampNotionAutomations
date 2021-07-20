from config import settings
from utilities import datetimetools, user_interface

"""
Add dates to class schedule
DONE 0. Get the collection dates are being added to 

NOT DONE 1. Get the type of course (Full or Part Time) - use a dictionary or tuple to store class days (Monday-Friday, Monday-Thursday)
            1a. If course is Full Time, set global variables accordingly
            1b. If course is Part Time, set global variables accordingly
            
DONE 2. Get the starting date

NOT DONE 3. Control for holidays when the school is closed

NOT DONE 4. Iterate over each row in collection
            4a. If the Type is Assignment, call function to add start date, end date, and assignment submitted date
             4b. If the type is any other, call function to just add date assigned
"""


def get_schedule_to_add_dates_to():
    # this is the Class Schedule Template private page in my devCodeCamp workspace
    return settings.client.get_collection_view(
        'https://www.notion.so/29eb8cd9c412439f8adcf78aa0d24ea9?v=c3d0c786555f42a78124664e5d195cc5')


def add_dates_to_schedule():
    # get schedule collection to add dates to
    # use datetimetools function to create a Notion date for start date by passing in user interface prompt
    cv = get_schedule_to_add_dates_to()
    starting_date = datetimetools.create_date()
    course_type = user_interface.get_course_type()[1]
    active_date = starting_date
    active_day = 1
    for row in cv.collection.get_rows():
        if row.day != active_day:
            while row.day != active_day:
                active_date = datetimetools.add_class_day_to_date(
                    active_date, course_type)
                active_day += 1
            notionized_date = datetimetools.create_notion_date_start(
                active_date)
            row.date_assigned = notionized_date
            active_day = row.day
        elif row.Type == 'Assignment' and row.last_working_day is not None and active_day != row.last_working_day:
            # TODO: Test Assignment date addition logic
            # TODO: Add Assignment Submit Date to all course templates
            add_date_objects = datetimetools.create_notion_dates_start_end_submitted(active_date, active_day,
                                                                                     row.last_working_day)
            row.date_assigned = add_date_objects[0]
            row.assignment_submit_date = add_date_objects[1]
        else:
            notionized_date = datetimetools.create_notion_date_start(
                active_date)
            row.date_assigned = notionized_date


def test_function():
    pass
