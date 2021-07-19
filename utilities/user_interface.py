# Generic helper functions usable in each module for getting/displaying user input

def get_course_type():
    user_input = input('What course type? 1 = Full-Time, 2 = Part-Time')
    if user_input == '1':
        course_type = ('Full-Time', 1)
        return course_type
    elif user_input == '2':
        course_type = ('Part-Time', 2)
        return course_type
    else:
        get_course_type()


def get_cohort():
    # takes user input to determine if cohort exists
    # if the cohort does not exist, creates new cohort and returns to calling function
    # helper function for adding new students to Active Students

    cohort_name = input('What is the name of the cohort?')
    return cohort_name
