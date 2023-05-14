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

import os

user = os.system('whoami')
ip = os.system('ip a')
hardware = os.system('lshw -short')

print(user)
print(ip)
print(hardware)

# Stretch Goals (using subprocess instead of os)

import subprocess

user = subprocess.run('whoami')
ip = subprocess.run(['ip', 'a'])
hardware = subprocess.run(['lshw', '-short'])

print(user)
print(ip)
print(hardware)

# End