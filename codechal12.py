#!/usr/bin/env python3

# Script: Ops 301 Challenge 12
# Author: Cameron Berry
# Date of last revision: 6/1/23
# Purpose: - Prompt the user to type a string input as the variable for your destination URL.
#          - Prompt the user to select a HTTP Method of the following options:
#             - GET
#             - POST
#             - PUT
#             - DELETE
#             - HEAD
#             - PATCH
#             - OPTIONS
#          - Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
#          - Using the `requests` library, perform a `GET` request against your lab web server.
#          - For the given header, translate the codes into plain terms that print to the screen; for example, a `404` error should print `Site not found` to the terminal instead of `404`.
#          - For the given URL, print response header information to the screen.

# Define variables

request_options = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]

# Define functions

            

# Main

import os
import requests

os.system("clear")

url = input("Please type a FULL URL (ie include https://, etc): ")

# loop to enable replay on invalid input
while True:
    os.system("clear")
# create menu + exit option
    for menu_options in request_options:
        print(f"-{menu_options}")
    print("-EXIT")
# .lower to make life easier for everyone
    command = input("Please select an HTTP method from the above options: ").lower()
# get request
    if command == "get":
        get = requests.get(url)
        break
# post request
    elif command == "post":
        post = requests.post(url)
        break
# put request
    elif command == "put":
        put = requests.post(url)
        break
# delete request
    elif command == "delete":
        delete = requests.delete(url)
        break
# head request
    elif command == "head":
        head = requests.head()
        break
# patch request
    elif command == "patch":
        patch = requests.patch(url)
        break
# options request
    elif command == "options":
        options = requests.options(url)
        break
# exit path
    elif command == "exit":
        exit()
# invalid input
    else:
        print("INVALID INPUT! Press Enter to continue")
        input()
        continue

# End