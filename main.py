# Main entry point of application
from automations import activestudents, classschedules, activestudents
import webbrowser

"""
Daily Startup Script for devCodeCamp workflow
"""
# webbrowser.open("https://www.notion.so/Instructor-Home-Base-0692947b36fd41aaaca2a9c625dc7a78")
# webbrowser.open("https://clockify.me/tracker")
# webbrowser.open("http://onlinegradebookfinal-env.eba-9ie5afi7.us-east-2.elasticbeanstalk.com/Instructors/Dashboard")

# TODO: Refactor automations into JavaScript SDK with official Notion Client
# TODO: Convert into a CLI application
"""
Change Active Student Stand Up Status (per class)
"""
# Change standup status to Not Started
activestudents.change_standup_status_notstarted('Part-Time')
#activestudents.change_standup_status_notstarted('Full-Time')

"""
New Class Notion Admin
"""
# classschedules.add_dates_to_schedule()
# activestudents.add_new_class_to_activestudents()
