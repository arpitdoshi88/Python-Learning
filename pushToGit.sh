#!/bin/zsh
# lines that start like this are shell comments
# read projects current directory with $PWD
cd /Users/arpit/Python-Learning 
echo "Enter commit message"
read message
git status
git add . && \
git add -u && \
git commit -m "$message" && \
git push origin HEAD
