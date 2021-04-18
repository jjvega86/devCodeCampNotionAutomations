# Main entry point of application
from datetime import date
from automations import activestudents, classschedules
from utilities import datetimetools

'''
# Change standup status to Not Started
activestudents.change_standup_status_notstarted('Part-Time')
activestudents.change_standup_status_notstarted('Full-Time')
'''

classschedules.add_dates_to_schedule()
