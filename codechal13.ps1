# Script: Ops 301 Challenge 13
# Author: Cameron Berry
# Date of last revision: 
# Purpose: - Write a Powershell script that adds the below person to AD.
#                 - Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz's email is ferdi@GlobeXpower.com.
#          - Have your script also create a new group in AD.
#          - Have your script also create a new OU in AD.



# main

Import-Module activedirectory

# Put into an array for scalability
$deptlist = @("Finance", "Shipping", "TPS")

Write-Host "Set-up for new user"
$firstname = read-host "New User first name"
$lastname = read-host "New User last name"

# .substring arguments -> (starting index, length)
$samaccountname = $firstname.Substring(0,1) + $lastname

# lists departments and prompts for a choice
foreach ($deptlist in $deptlist) {
    write-host $deptlist
    }
$dept = read-host "Choose a department from the list above"
if ($deptlist -notcontains $dept) {
    Write-Host "Invalid Entry. Please restart script."
    exit
    }

$role = Read-Host "Enter new user's role"

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
    Write-Host "New User Added Successfully"
    }
else {
    Write-Host "Information not saved. Restart script to try again."
    }

# optional create new OU
$newOU = read-host "Create new OU? [Y]"
if ($newOU -eq "y") {
    $OUname = read-host "Please enter a name for the new OU"
    New-ADOrganizationalUnit -Name $OUname -ProtectedFromAccidentalDeletion $false
    write-host $OUname "OU created"
    }

# optional create new global security group
# given more time, a menu system could be added to create different types of groups
$newGroup = read-host "Create new Global Security Group? [Y]"
if ($newGroup -eq "y") {
    $Groupname = read-host "Please enter a name for the new Group"
    New-ADGroup -Name $Groupname -GroupCategory Security -GroupScope Global
    Write-Host $Groupname "group created"
    }

# end