#!/bin/bash

# Script: 301 Code Challenge 03
# Author: Cameron Berry
# Date of last revision:
# Purpose: Prompts user for input directory path.
#          Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
#          Navigates to the directory input by the user and changes all files inside it to the input setting.
#          Prints to the screen the directory contents and the new permissions settings of everything in the directory.
#          STRETCH GOALS
#          Design your script to output a log file of all actions that were taken by the script.
#          Design your script to output to the screen each file changed one by one, with a slight delay between each file changed.

# Declare variables

log="permissionslog.txt"

# Declare functions

userinput() {
    echo "Enter Directory Path: "
    read dir
        if [ -d "$dir" ];
        then
            cd $dir
        else
            echo "INVALID DIRECTORY"
            exit
        fi
    echo "Enter chmod Permission # (000-777): "
    read pmsn
}

chmodset() {
    date "+%m/%d/%y %H:%M:%S" >> $log
    for file in *;
        do
            if [ -d "$file" ];
            then
                echo "Changing permissions for DIR $file"
            else
                echo "Changing permissions for FILE $file"
            fi 
        echo "--------------------" >> $log
        ls -l $file >> $log
        chmod -R "$pmsn" "$file"
        echo "CHANGED TO NEW PERMISSIONS:" >> $log
        ls -l $file >> $log
        sleep 1
    done
    echo "*****COMPLETE*****" >> $log
    echo "New permissions set:"
    ls -al
}

# Main

userinput
chmodset

# End

# Questions: how to display filenames within dir with screen print
#            setting log file to a different path



# notes:

# chmod calculator

# Unix permissions:
# User/Owner -> usually the orig creator of file/folder
# Group -> owns file/folder
# Others -> public

# view file permissions:
# ls -al shows user & group that owns the file

# recursion:
# -r flag performs same task on everything in a collection
# ex chmod -r 755 ./     (<- ./ = start in pwd)