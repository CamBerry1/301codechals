#!/bin/bash

# Script: Ops 301 Code Challenge 05
# Author: Cameron Berry
# Date of last revision: 5/6/2023
# Purpose: Print to the screen the file size of the log files before compression
#          Compress the contents of the log files listed below to a backup directory
#               /var/log/syslog
#               /var/log/wtmp
#          The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
#               Example: /var/log/backups/syslog-20220928081457.zip
#          Clear the contents of the log file
#          Print to screen the file size of the compressed file
#          Compare the size of the compressed files to the size of the original log files

#!/bin/bash

# Declare variables

datetime=`date +%y%m%d%H%M%S`
backupfile="$HOME/Documents/backups/syslog_wtmp_$datetime.txt"

# Declare functions



# Main

#make the backup directory in 'Documents'
mkdir ~/Documents/backups
#create the file to copy logs into
touch $backupfile
#write syslog contents and append wtmp contents to backupfile
cat /var/log/syslog > $backupfile
cat /var/log/wtmp >> $backupfile
#read full filesize
filesize=$(wc -c $backupfile | awk '{print $1}')
echo "Syslog and Wtmp are currently $filesize bytes"
read -p "Press Enter to clear logs and compress backup "
#compress backup file
backzip="$HOME/Documents/backups/logs_$datetime.zip"
zip -r "$backzip" "$backupfile"
#clear original logs
sudo truncate -s 0 /var/log/syslog
sudo truncate -s 0 /var/log/wtmp
#read filesize of zipped logs
filesize2=$(wc -c "$backzip" | awk '{print $1}')
#display size comparision
echo "File was reduced from $filesize bytes to $filesize2 bytes"

# End


# Not super happy with how this looks. I think if I had more time I could clean it up a bit, but it works

# questions still:
#           should I have the script delete the pre-zipped backup file?
#           i couldn't get /dev/null to write into the files so i used truncate instead. it's the same effect but is it the same thing?