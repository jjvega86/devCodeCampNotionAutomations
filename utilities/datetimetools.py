from notion.collection import NotionDate
from utilities import user_interface
from datetime import datetime, timedelta
import holidays

dates_school_closed = [
    # This list is used to filter current holidays based off of the current year
    "New Year's Day",
    "Memorial Day",
    "Independence Day",
    "Labor Day",
    "Thanksgiving",
    "Christmas Day"
]


# TODO: add holiday parsing logic to change course end date based on dates the school is closed outside of weekends
# TODO: get dates the school is closed on Christmas week based on Christmas Day
# https://pypi.org/project/holidays/ -- Use this library to create custom holiday object to test date for class/no class

def get_school_closed_datetime_objects():
    current_year = datetime.now().strftime('%Y')  # Get current year
    current_holidays = holidays.UnitedStates(years=int(current_year))  # Get current year's holidays
    filtered_holidays = []
    for date in current_holidays.items():  # each item in current_holidays is a tuple, with the date at the 0 index and name at the 1 index
        if date[1] == "Christmas Day":
            filtered_holidays.append(date[0])
            filtered_holidays = add_chrismas_week_days(filtered_holidays, date[0])
        elif date[1] in dates_school_closed:
            filtered_holidays.append(date[0])
    return filtered_holidays


def add_chrismas_week_days(filtered_holidays, christmas_day):
    if christmas_day.weekday() == 0:
        dates = [christmas_day+timedelta(days=1), christmas_day+timedelta(days=2),christmas_day+timedelta(days=3), christmas_day+timedelta(days=4)]
    elif christmas_day.weekday() == 1:
        dates = [christmas_day - timedelta(days=1), christmas_day + timedelta(days=1), christmas_day + timedelta(days=2), christmas_day + timedelta(days=3)]
    elif christmas_day.weekday() == 2:
        dates = [christmas_day - timedelta(days=2), christmas_day - timedelta(days=1), christmas_day + timedelta(days=1), christmas_day + timedelta(days=2)]
    elif christmas_day.weekday() == 3:
        dates = [christmas_day - timedelta(days=3), christmas_day - timedelta(days=2), christmas_day - timedelta(days=1), christmas_day + timedelta(days=1)]
    elif christmas_day.weekday() == 4:
        dates = [christmas_day - timedelta(days=4), christmas_day - timedelta(days=3), christmas_day - timedelta(days=2), christmas_day - timedelta(days=1)]
    elif christmas_day.weekday() == 5:
        dates = [christmas_day - timedelta(days=5), christmas_day - timedelta(days=4), christmas_day - timedelta(days=3), christmas_day - timedelta(days=2), christmas_day - timedelta(days=1)]
    elif christmas_day.weekday() == 6:
        dates = [christmas_day + timedelta(days=1), christmas_day + timedelta(days=2), christmas_day + timedelta(days=3), christmas_day + timedelta(days=4), christmas_day + timedelta(days=5)]

    combined_dates = dates + filtered_holidays
    return combined_dates


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


def create_start_date(str_date):
    start = datetime.strptime(str_date, "%Y-%m-%d").date()
    notion_start_date = NotionDate(start)
    return notion_start_date
