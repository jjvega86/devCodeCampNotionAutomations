from notion.collection import NotionDate
from datetime import datetime, timedelta
import holidays

dates_school_closed = [
    # This list is used to filter current holidays based off of the current year
    "New Year's Day",
    "Memorial Day",
    "Independence Day",
    "Labor Day",
    "Thanksgiving",
    "Christmas Day",
    "Some Random Holiday"
]


# TODO: update holidays based on Mike's feedback. See his DM in Slack
# https://pypi.org/project/holidays/ -- Use this library to create custom holiday object to test date for class/no class

def get_school_closed_datetime_objects():
    """
    Gets current year, all US holidays based off of year.
    Removes any holidays not on list of days school is closed
    Calls function to add all days of week for Christmas Week
    :return:
    """
    current_year = datetime.now().strftime('%Y')  # Get current year
    current_holidays = holidays.UnitedStates(years=int(current_year))  # Get current year's holidays
    current_holidays[datetime(2021, 7, 2)] = "Some Random Holiday"
    filtered_holidays = []
    for date in current_holidays.items():  # each item in current_holidays is a tuple, with the date at the 0 index and name at the 1 index
        if date[1] == "Christmas Day":
            filtered_holidays.append(date[0])
            filtered_holidays = add_chrismas_week_days(filtered_holidays, date[0])
        elif date[1] in dates_school_closed:
            filtered_holidays.append(date[0])
    return filtered_holidays


def add_chrismas_week_days(filtered_holidays, christmas_day):
    """
    Takes in list of filtered holidays and the date object for Christmas Day
    Checks the day of the week Christmas Day falls on
    Populates a list of dates for all other week days that week
    Returns a combined list of the previously filtered holidays and the days of Christmas Week
    :param filtered_holidays: list of filtered holiday date objects
    :param christmas_day: date object for Christmas Day of current year
    :return: combined List of date objects
    """
    if christmas_day.weekday() == 0:
        dates = [christmas_day + timedelta(days=1), christmas_day + timedelta(days=2),
                 christmas_day + timedelta(days=3), christmas_day + timedelta(days=4)]
    elif christmas_day.weekday() == 1:
        dates = [christmas_day - timedelta(days=1), christmas_day + timedelta(days=1),
                 christmas_day + timedelta(days=2), christmas_day + timedelta(days=3)]
    elif christmas_day.weekday() == 2:
        dates = [christmas_day - timedelta(days=2), christmas_day - timedelta(days=1),
                 christmas_day + timedelta(days=1), christmas_day + timedelta(days=2)]
    elif christmas_day.weekday() == 3:
        dates = [christmas_day - timedelta(days=3), christmas_day - timedelta(days=2),
                 christmas_day - timedelta(days=1), christmas_day + timedelta(days=1)]
    elif christmas_day.weekday() == 4:
        dates = [christmas_day - timedelta(days=4), christmas_day - timedelta(days=3),
                 christmas_day - timedelta(days=2), christmas_day - timedelta(days=1)]
    elif christmas_day.weekday() == 5:
        dates = [christmas_day - timedelta(days=5), christmas_day - timedelta(days=4),
                 christmas_day - timedelta(days=3), christmas_day - timedelta(days=2),
                 christmas_day - timedelta(days=1)]
    elif christmas_day.weekday() == 6:
        dates = [christmas_day + timedelta(days=1), christmas_day + timedelta(days=2),
                 christmas_day + timedelta(days=3), christmas_day + timedelta(days=4),
                 christmas_day + timedelta(days=5)]

    combined_dates = dates + filtered_holidays
    return combined_dates


def create_cohort_date(course_type):
    # applies a start and end date to new row in Cohort database
    start = create_date()
    days = None
    if course_type == 'Full Time':
        days = 91
    elif course_type == 'Part Time':
        days = 98
    end = start + timedelta(days=days)
    date = NotionDate(start, end=end)
    return date


def create_date():
    str_date = input('Please enter starting date in format <YYYY-MM-DD>')
    date_object = datetime.strptime(str_date, "%Y-%m-%d").date()
    return date_object


def check_for_holiday(date):
    is_holiday = False
    all_holidays = get_school_closed_datetime_objects()
    for closed_day in all_holidays:
        if closed_day == date:
            is_holiday = True
    return is_holiday


def add_class_day_to_date(date, course_type):
    not_valid = True
    new_date = date
    while not_valid:
        new_date = new_date + timedelta(days=1)
        if course_type == 2 and new_date.weekday() == 4:
            new_date = new_date + timedelta(days=3)
            not_valid = check_for_holiday(new_date)
            continue
        elif new_date.weekday() == 5:
            new_date = new_date + timedelta(days=2)
            not_valid = check_for_holiday(new_date)
            continue
        elif new_date.weekday() == 6:
            new_date = new_date + timedelta(days=1)
            not_valid = check_for_holiday(new_date)
            continue
        else:
            not_valid = check_for_holiday(new_date)
            continue

    return new_date


def validate_date(date):
    not_valid = True
    new_date = date
    while not_valid:
        # new_date = new_date + timedelta(days=1)
        if new_date.weekday() == 5:
            new_date = new_date + timedelta(days=2)
            not_valid = check_for_holiday(new_date)
            continue
        elif new_date.weekday() == 6:
            new_date = new_date + timedelta(days=1)
            not_valid = check_for_holiday(new_date)
            continue
        else:
            not_valid = check_for_holiday(new_date)
            if not_valid:
                new_date = new_date + timedelta(days=1)
            continue

    return new_date


def create_notion_date_start(start):
    notion_date = NotionDate(start)
    return notion_date


def create_notion_dates_start_end_submitted(start, active_day, last_working_day):
    # TODO: Add weekend and holiday validation logic for last working day and date submitted
    end = start + timedelta(days=last_working_day - active_day)
    validated_end = validate_date(end)
    assignment_submitted_date = validated_end + timedelta(days=1)
    assignment_start_end = NotionDate(start, end=validated_end)
    assignment_submitted = NotionDate(assignment_submitted_date)
    all_date_objects = [assignment_start_end, assignment_submitted]
    return all_date_objects
