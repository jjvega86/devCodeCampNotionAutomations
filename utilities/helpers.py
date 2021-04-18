from config import settings


# Generic helper functions usable in each module


def get_course_type():
    user_input = input('What course type? 1 = Full Time, 2 = Part Time')
    if user_input == '1':
        return 'Full Time'
    elif user_input == '2':
        return 'Part Time'
    else:
        get_course_type()
