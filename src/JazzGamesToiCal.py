# pip install ics

from ics import Calendar, Event
from dateutil import tz
from datetime import timedelta
from datetime import datetime
from dateutil import tz

# Initialize an empty list to store parsed events
parsed_events = []

# Open the text file for reading
with open("HomeJazzGames2425.txt", "r") as file:
    lines = file.readlines()

event = {}  # Initialize an empty dictionary to store event details

# Loop through the lines in the text file
for line in lines:
    # Strip leading and trailing whitespace from the line
    line = line.strip()
    
    # Check if the line is empty; if yes, it's the end of an event
    if not line:
        if event:  # Check if there's an event to add
            parsed_events.append(event)  # Add the event to the list
            event = {}  # Reset the event dictionary for the next event
    else:
        # Split the line into key and value
        key, value = line.split(":", 1)
        
        # Store the key-value pair in the event dictionary
        event[key.strip()] = value.strip()

# Add the last event (if any) to the list
if event:
    parsed_events.append(event)

# Create a calendar
cal = Calendar()

# Loop through the parsed events and add them to the calendar
# Duration set to 3 hours.
date_format = '%Y-%m-%d %H:%M:%S' # Format the ics module expects the dates to be in

for event in parsed_events:
    e = Event()
    e.name = event['Event']
    # First let's convert this to a datetime object in the US/Mountain Time zone
    due_dt = datetime.strptime(event['Start'],date_format).replace(tzinfo=tz.gettz('US/Mountain'))
    # Then let's convert the date to UTC so ics can handle it correctly
    due_dt = due_dt.astimezone(tz.tzutc())
    e.begin = due_dt.strftime(date_format)
    e.duration = timedelta(hours=3)
    e.location = event['Location']
    e.description = event['Description']

    # Add the event to the calendar
    cal.events.add(e)

# Save the combined .ical file
with open("UtahJazzHomeGames24_25.ics", "w") as f:
    f.write(str(cal))
