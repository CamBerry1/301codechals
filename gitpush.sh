# !/bin/bash

git status
echo "type filename"
read filename
git add $filename
echo "add commit message"
read message
git commit -m "$message"
git push