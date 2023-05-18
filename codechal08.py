#!/usr/bin/env python3

# Script: Ops 301 Code Challenge 08
# Author: Cameron Berry
# Date of last revision: 5/17/23
# Purpose: Assign to a variable a list of ten string elements.
#          Print the fourth element of the list.
#          Print the sixth through tenth element of the list.
#          Change the value of the seventh element to “onion”.

# Define variables

# cheese list
myfavoritecheeses = ["gouda", "mozzarella", "parmesan", "chedder", "swiss", "provalone", "pepperjack", "gruyere", "pecorino", "string"]

# Define functions



# Main

# print the 4th element at index 3
print(myfavoritecheeses[3], "is pretty good")
# each "input()" waits for user to press enter to continue
input()
# print elements 6-10 (at indices 5-10)
print(myfavoritecheeses[5:10], "...all together are better")
input()
# change "pepperjack" to "onion"
myfavoritecheeses[6] = "onion"
# print onion (7th element in list, 6th index)
print("But", myfavoritecheeses[6], "rules them all")
input()
# ask user for new element
yourfavorite = input("What is your favorite cheese? ")
# add input to list
myfavoritecheeses.append(yourfavorite)
# print input
print(myfavoritecheeses[10], "is good too!")

# End

# I want to go for more of the stretch goals tomorrow. Used the append one, researched the others
# I'm going to submit, work a little more tomorrow and ACP it