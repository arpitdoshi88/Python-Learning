#!/bin/zsh
# lines that start like this are shell comments
# read projects current directory with $PWD
echo “running command from” $PWD
cd $PWD
echo "Enter commit message"
read message
git status
git add . && \
git add -u && \
git commit -m "$message" && \
git push origin HEAD
