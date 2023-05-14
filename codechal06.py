#!/usr/bin/env python3

# Script: Ops 301 Challenge 06
# Author: Cameron Berry
# Date of last revision: 5/13/23
# Purpose: - The Python module "os" must be utilized
#          - At least three variables must be declared in Python that contain results of bash operations
#          - The Python function print() must be used at least three times

#          Include execution of the following bash commands inside your Python script:

#          - `whoami`
#          - `ip a`
#          - `lshw -short`

# Main

# load the os module
import os

# specify bash commands and input into variables
user = os.system('whoami')
ip = os.system('ip a')
hardware = os.system('lshw -short')

# print variables
print(user)
print(ip)
print(hardware)

# Stretch Goals (using subprocess instead of os)

# load the subprocess module
import subprocess

# specify bash commands and input into variables
user = subprocess.run('whoami')
ip = subprocess.run(['ip', 'a'])
hardware = subprocess.run(['lshw', '-short'])

# print variables
print(user)
print(ip)
print(hardware)

# End

# So, I know we're learning, but is using a print commands redundant?
# the os.system and subprocess.run commands already print output to the console