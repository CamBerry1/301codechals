#!/usr/bin/env python3

# Script: Ops 301 Challenge 09
# Author: Cameron Berry
# Date of last revision: 5/20/23
# Purpose: Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
#           - Equals: a == b
#           - Not Equals: a != b
#           - Less than: a < b
#           - Less than or equal to: a <= b
#           - Greater than: a > b
#           - Greater than or equal to: a >= b
#           Create an if statement using a logical conditional of your choice and include `elif` keyword that executes when other conditions are not met.
#           Create an if statement that includes both `elif` and `else` to execute when both `if` and `elif` are not met.
# STRETCH GOALS
#           Create an if statement with two conditions by using `and` between conditions.
#           Create an if statement with two conditions by using `or` between conditions.
#           Create a nested if statement.
#           Create an if statement that includes `pass` to avoid errors.

# let's us use the time module to time.sleep(*)
import time

# let's us use the os module to clear the screen
import os

# Define variables

favmovie = "Back to the Future"

# Define functions

# sleeps for specified time and clears the screen
def sleepclear(sleep):
    timeint = int(sleep)
    time.sleep(timeint)
    os.system('clear')

# Main

os.system('clear')

movie = input("Hey there! What's the greatest movie of all time? ")

# *.lower() converts input to lowercase, removing case sensitivity
if movie.lower() == favmovie.lower():
    print("I knew I liked you")
    time.sleep(1)
else:
    print("You're wrong")
    time.sleep(1)
    print("It's", favmovie)
    time.sleep(1)
    print("But let's move on")
    time.sleep(1)

sleepclear(1)

print("Let's try something else")

sleepclear(2)

number = input("Pick a number between 1-100: ")
# int() converts the string into an integer
number_int = int(number)

if number_int <= 1 or number_int >= 100:
    print("Did you even read the instructions?")
elif number_int == 42:
        print("That's what's up")
else:
        print(f"{number} is alright I guess")

sleepclear(2)

print("Last one")
time.sleep(1)

answer = input("What has 4 letters, never has 5 letters, sometimes has 9 letters, and occasionally has 12 letters: ")

answerlower = answer.lower()

# gives player another chance with string "i don't know"
if answerlower != "yes":
    if answerlower.lower() == "i don't know":
        print("(hint: it's not a question)")
        answer = input("Try again: ")
        answerlower = answer.lower()
    else:
        pass

# if all questions are answered correctly
if movie.lower() == favmovie.lower() and number_int == 42 and answerlower == "yes":
    pass
else:
    print("Whelp")
    time.sleep(2)
    print("Thanks for playing!")
    time.sleep(2)
    exit()

os.system('clear')

# dancing kirby + the paswwrod
print("<(^-^<)")
print("The password is 'password'")
time.sleep(0.5)
os.system('clear')
print("^(^-^)^")
print("The password is 'password'")
time.sleep(0.5)
os.system('clear')
print("(>^-^)>")
print("The password is 'password'")
time.sleep(0.5)
os.system('clear')
print("^(^-^)^")
print("The password is 'password'")
time.sleep(0.5)
os.system('clear')
print("<(^-^<)")
print("The password is 'password'")
time.sleep(0.5)
os.system('clear')
print("(>^-^)>")
print("The password is 'password'")
time.sleep(0.5)
os.system('clear')
print("<(^-^<)")
print("The password is 'password'")
time.sleep(0.5)
os.system('clear')
print("(>^-^)>")
print("The password is 'password'")
time.sleep(0.5)
os.system('clear')
print("^(^-^)^")
print("The password is 'password'")
time.sleep(1)