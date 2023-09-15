# text-2-outlook-cal-ics
Python script to take a text file list of events and create an Outlook .ics file using Python3 and ics.py

Long story short - I wanted to put all the Utah Jazz 2023 - 2024 home games on my Outlook calendar easily. After an internet search to find a calendar of home games to dump through an online utility I found nothing.. so I decided to just write some Python and do it myself. 

You can use this to create an .iCal to import into Outlook for any events using the text file. Just alter for your own events.  

You will need to adjust the time zone in the Python script for your desired time zone (since ics.py converts always to UTC).  Note there is some work the ics maintainers are doing for Daylight Savings Time issues, to your mileage may vary. Trust but Verify. :) 
