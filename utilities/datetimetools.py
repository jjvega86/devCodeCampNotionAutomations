from notion.collection import NotionDate
from datetime import datetime, timedelta

# TODO: add holiday parsing logic to change course end date based on dates the school is closed outside of weekends
# https://pypi.org/project/holidays/ -- Use this library to create custom holiday object to test date for class/no class


def create_cohort_date(course_type):
    # applies a start and end date to new row in Cohort database
    user_input = input('Enter start date in format: YYYY-MM-DD')
    start = datetime.strptime(user_input, "%Y-%m-%d").date()
    days = None
    if course_type == 'Full Time':
        days = 91
    elif course_type == 'Part Time':
        days = 98
    end = start + timedelta(days=days)
    date = NotionDate(start, end=end)
    return date
