# Main entry point of application
from automations import activestudents, classschedules

'''
# Change standup status to Not Started
activestudents.change_standup_status_notstarted('Part-Time')
activestudents.change_standup_status_notstarted('Full-Time')
'''

print(classschedules.get_schedule_to_add_dates_to())
