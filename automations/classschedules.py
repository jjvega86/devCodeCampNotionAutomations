from config import settings
from utilities import datetimetools

"""
Add dates to class schedule
0. Get the collection dates are being added to
1. Get the type of course (Full or Part Time) - use a dictionary or tuple to store class days (Monday-Friday, Monday-Thursday)
    1a. If course is Full Time, set global variables accordingly
    1b. If course is Part Time, set global variables accordingly
2. Get the starting date
3. Control for holidays when the school is closed
4. Iterate over each row in collection
    4a. If the Type is Assignment, call function to add start date, end date, and assignment submitted date
    4b. If the type is any other, call function to just add date assigned
"""