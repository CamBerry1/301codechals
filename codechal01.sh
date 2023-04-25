#!/bin/bash

# Script: 301 Ops Challenge 01
# Author: Cameron Berry
# Date of last revision: 4/24/23
# Purpose: Create a bash script that:
#           - Copies `/var/log/syslog` to the current working directory
#           - Appends the current date and time to the filename
#          Stretch goals
#           - Include in your bash script some timestamped echo statements telling the user what is happening at each stage of the script.

# Declare variables

year=`date +%y`
month=`date +%m`
day=`date +%d`
hour=`date +%H`
minute=`date +%M`
second=`date +%S`
datetime="$month$day$year|$hour$minute$second"

# Declare functions

create() {
    cat /var/log/syslog > "$datetime"_syslog.txt
}

# Main

echo "Press ENTER to create $datetime /var/log/syslog text file"
read
create
echo "$datetime syslog file created"

# End

# I tried using append to change the filename to current date/time without creating a new text file but couldn't figure it out and now I'm going to bed





# Notes:

# how to show time/date
# echo `date`
# or
# echo $(date)

# here we assign variables but you can run these commands on their own without the ` outside the command string. These are modifiers shown
# year=`date +%Y`
# echo $year
# month=`date +%m`
# echo $month
# day=`date +%a`
# echo $day
# day2=`date +%d`
# echo $day2

# # the date command displays the local system's date/time

# hour=`date +%H`
# echo $hour
# minute=`date +%M`
# echo $minute
# second=`date +%S`
# echo $second

# # put it all together
# echo "Current Date: $day-$month-$year"
# echo "Current Time: $hour:$minute:$second"


# # How to row append
# create a file testfile.txt and add lines to it
# echo "Original file before append: "
# cat testfile.txt

# # the >> double carrot will row append
# echo "My new string with the `date` " >> testfile.txt
# echo "Appended file: "
# cat testfile.txt