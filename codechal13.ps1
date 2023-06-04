# Script: Ops 301 Challenge 13
# Author: Cameron Berry
# Date of last revision: 
# Purpose: - Write a Powershell script that adds the below person to AD.
#                 - Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz's email is ferdi@GlobeXpower.com.
#          - Have your script also create a new group in AD.
#          - Have your script also create a new OU in AD.

Import-Module activedirectory

# define variables

# Put into an array for scalability
$deptlist = @("Finance", "Shipping", "TPS", "HR", "Sales", "Admin")
$newuser = "y"

# main

Write-Host "Set-up for new user"
while ($newuser -eq "y") {
    $firstname = read-host "New User first name"
    $lastname = read-host "New User last name"

# .substring arguments -> (starting index, length)
    $samaccountname = $firstname.Substring(0,1) + $lastname

# lists departments and prompts for a choice
    foreach ($dept in $deptlist) {
        write-host $dept
        }
    $dept = read-host "Choose a department from the list above"
    if ($deptlist -notcontains $dept) {
        Write-Host "Invalid Entry" 
        exit                       
        }

    $role = Read-Host "New user role"

    $mail = read-host "New user Email"

# display information and ask for confirmation
    Write-Host $firstname $lastname; write-host $dept "Department"; write-host $role; write-host $mail
    $confirm = read-host "Is this information correct? [Y]"

# create new user
    if ($confirm -eq "y") {
        New-ADUser -SamAccountName $samaccountname -Name $firstname$lastname -EmailAddress $mail -OtherAttributes @{
        'department'=$dept;
        'title'=$role
        }
        Write-Host $samaccountname "Added Successfully"
        $newuser = read-host "Add another user? [Y]"
        }
    else {
        Write-Host "Information not saved. Restart script to try again."
        exit
        }
    }

# optional create new OU
$newOU = read-host "Create new OU? [Y]"
if ($newOU -eq "y") {
    while ($newOU -eq "y") {
        $OUname = read-host "Please enter a name for the new OU"
        New-ADOrganizationalUnit -Name $OUname
        write-host $OUname "OU created"
        $newOU = Read-Host "Create another OU? [Y]"
        }
    }

# optional create new global security group
# given more time, a menu system could be added to create different types of groups
$newGroup = read-host "Create new Global Security Group? [Y]"
if ($newGroup -eq "y") {
    while ($newGroup -eq "y") {
        $Groupname = read-host "Please enter a name for the new Group"
        New-ADGroup -Name $Groupname -GroupCategory Security -GroupScope Global
        Write-Host $Groupname "group created"
        $newGroup = Read-Host "Create another group? [Y]"
        }
    }

# end