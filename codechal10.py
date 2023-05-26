#!/usr/bin/env python3

# Script: Ops 301 Challenge 10
# Author: Cameron Berry
# Date of last revision: 5/24/23
# Purpose: Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.
# Stretch Goals:
# - Export your pfSense configuration. 
# - Have your Python script open the exported file. 
# - Code up your script to change a value inside the file. 
# - Save the changes out to a new file name.
# - Re-import the modified configuration file, to verify that your changes will be accepted by pfSense.

import os

# Define variables

file = "this_file_will_be_deleted_as_soon_as_the_script_is_done_running_so_it_doesnt_really_matter_how_long_the_file_name_is.txt"

# Define functions



# Main

with open(file, "w") as text:
    text.write("This is the first line of text in a new file\n")
    text.write("I can write anything here.\n")
    text.write("You'll never see it anyway.")

with open(file, "r") as text:
    print(text.readline())

os.remove(file)

# End

# I'm not confortable enough with pfSense to attempt the stretch goals for this one, but it's one that I will be revisiting in the future.