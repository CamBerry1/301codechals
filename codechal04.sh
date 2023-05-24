#!/bin/bash

# Script: Ops 301 Code Challenge 04
# Author: Cameron Berry
# Date of last revision: 5/24/23
# Purpose: - Create a bash script that launches a menu system with the following options:
#             - Hello world (prints "Hello world!" to the screen)
#             - Ping self (pings this computer's loopback address)
#             - IP info (print the network adapter information for this computer)
#             - Exit
#          - Next, the user input should be requested.
#          - The program should next use a conditional statement to evaluate the user's input, then act according to what the user selected.
#          - Use a loop to bring up the menu again after the request has been executed.

# Declare variables

continue="Press ENTER to continue"

# Declare functions



# Main

# start menu
while true; do
    clear
    echo "Please choose an option"
    echo "1. Print 'Hello world!' to screen"
    echo "2. Ping loopback address (127.0.0.1)"
    echo "3. Print IP information"
    echo "4. Exit"
    read option
# evaulate and resolve user input with if/then statements
        if [[ $option == 1 ]]; then   
            echo "Hello world!"
            read -p "$continue" 
        elif [[ $option == 2 ]]; then
# the -c flag determines how many ping packets will be sent
            ping -c 4 127.0.0.1
            read -p "$continue"
        elif [[ $option == 3 ]]; then
            ipconfig /all
            ifconfig
            read -p "$continue"
        elif [[ $option == 4 ]]; then
            echo "Thanks for playing!"
            exit
        else
            echo "Not a valid input!"
            read -p "$continue"
        fi
    done


exit

# End
