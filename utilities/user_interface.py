from config import settings


# Generic helper functions usable in each module for getting/displaying user input


def get_course_type():
    user_input = input('What course type? 1 = Full Time, 2 = Part Time')
    if user_input == '1':
        return 'Full Time'
    elif user_input == '2':
        return 'Part Time'
    else:
        get_course_type()


def get_string_input(prompt):
    user_input = prompt(prompt)
    return user_input


def get_starting_date():
    str_date = get_string_input('What date will the class start? FORMAT: <YYYY-mm-dd')