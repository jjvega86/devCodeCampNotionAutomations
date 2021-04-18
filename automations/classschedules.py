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
    return settings.client.get_collection_view(
        'https://www.notion.so/29eb8cd9c412439f8adcf78aa0d24ea9?v=c3d0c786555f42a78124664e5d195cc5')


def add_dates_to_schedule():
    # get schedule collection to add dates to
    # use datetimetools function to create a Notion date for start date by passing in user interface prompt
    cv = get_schedule_to_add_dates_to()
    starting_date = datetimetools.create_start_date(user_interface.get_starting_date())
