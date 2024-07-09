#!/usr/bin/python3
""" main function that will call the generate_invitations function from task_00_intro """

from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"},
    {"name": "John Doe", "event_title": "Conference"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)
