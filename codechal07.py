#!/usr/bin/env python3

# Script: Ops 301 Code Challenge 07
# Author: Cameron Berry
# Date of last revision: 5/13/23
# Purpose: Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

            # - Script must ask the user for a file path and read a user input string into a variable.
            # - Script must use the `os.walk()` function from the `os` library.
            # - Script must enclose the `os.walk()` function within a python function that hands it the user input file path.

import os

# Define Functions

def file_show(path):
    for (root, dirs, files) in os.walk(path):
        print(root)
        print(dirs)
        print(files)

# Main

path = input("What directory would you like information about? ")
file_show(path)

# End

# Does 'import os' need to be at the beginning of the code? or can it be called later
# Also, I'm still shaky on python. Excepted I guess because I'm a beginner, but this works