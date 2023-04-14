#!/bin/zsh
# lines that start like this are shell comments
# read projects current directory with $PWD
echo “running command from” $PWD
cd $PWD
git add .
read -p “Enter commit message: “ commitMessage
git commit -am “$commitMessage”
git push origin
