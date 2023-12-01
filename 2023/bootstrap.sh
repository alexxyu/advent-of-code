#!/bin/zsh
day=$(date +%d)
if [ $# -gt 1 ]; then
    echo "Expected exactly zero or one argument"
    exit 1
elif [ $# -eq 1 ]; then
    day=$1
fi

echo "Creating template for day-$day"

if [[ -d "day-$day" ]]; then
    echo "Directory for day-$day already exists"
    exit 1
fi

cp -r template day-$day
