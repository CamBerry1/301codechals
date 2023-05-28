#!/usr/bin/env python3

# Script: Ops 301 Challenge 11
# Author: Cameron Berry
# Date of last revision: 5/27/23
# Purpose: Create a Python script that fetches this information using Psutil:
#          - Time spent by normal processes executing in user mode
#          - Time spent by processes executing in kernel mode
#          - Time when system was idle
#          - Time spent by priority processes executing in user mode
#          - Time spent waiting for I/O to complete.
#          - Time spent for servicing hardware interrupts
#          - Time spent for servicing software interrupts
#          - Time spent by other operating systems running in a virtualized environment
#          - Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

# *****Psutil documentation*****
# https://psutil.readthedocs.io/en/latest/

# STRETCH GOALS:
#          - Save the information to a .txt file.
#          - Email the .txt file to yourself using Sendmail.

import psutil

# Define variables

# creates callable variable with all cpu times
times = psutil.cpu_times()
# for using 'sendmail' if I can ever figure that out
cputimestring = str(times)

# Define functions



# Main

print("System Usage Times (in seconds): " )
# user level processes
print("Normal Processes: ", times.user)
# system level processes
print("Kernal Mode Processes: ", times.system)
# idle time
print("System Idle Time: ", times.idle)
# processes with a different "niceness" value (priority value, -20 - +19, default is 0)
print("User Priority Processes: ", times.nice)
# waiting for data to be read from or written to storage devices
print("I/O Wait Time: ", times.iowait)
# hardware requests to CPU
print("Hardware Interrupt Request Servicing: ", times.irq)
# software requests to CPU
print("Software Interrupt Request Servicing: ", times.softirq)
# Guest OS wiating for CPU resoures
print("Virtualized OS Runtime: ", times.steal)
# Guest OS using CPU resources
print("Virtualized Application Processing: ", times.guest)

with open('cpu_usage.txt', 'w') as file:
# .write reads for strings. str() converts
    file.write(str(times))

# End