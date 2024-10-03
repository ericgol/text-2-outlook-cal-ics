# text-2-outlook-cal-ics
Python script to take a text file list of events and create an Outlook .ics file using Python3 and ics.py

Long story short - I wanted to put all the Utah Jazz 2023 - 2024 home games on my Outlook calendar easily. After an internet search to find a calendar of home games to dump through an online utility I found nothing.. so I decided to just write some Python and do it myself. 

You can use this to create an .iCal to import into Outlook for any events using the text file. Just alter for your own events.  

You will need to adjust the time zone in the Python script for your desired time zone (since ics.py converts always to UTC).  Note there is some work the ics maintainers are doing for Daylight Savings Time issues, to your mileage may vary. Trust but Verify. :) 


**New to coding? Here's a primer to get you started:**

Ensure Python is installed on your machine. 
  If not, head on over to [Python.org ](https://www.python.org/downloads/)

Ensure you have the Package Installer for Python installed on your machine. 
  In not, head on over to https://pip.pypa.io/en/stable/installation/

Ensure VS Code is installed on your machine. 
  If not, head on over to https://code.visualstudio.com/

Install the VS Code Python Extensions from within VS Code's Extension browser.

Install https://pypi.org/project/ics/
This is easy with the latest Python3 and PIP:
python 3 -m install pip

1) Clone this repo to your local machine with Git.
2) Use your terminal to cd into the \src directory. 
3) Start VS Code "code ."

You can now debug and run the script in VS code easily.

10/1/2024 - Updated with 24-25 Jazz Home Games
