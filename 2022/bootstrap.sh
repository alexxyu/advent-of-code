#!/bin/zsh
if [ $# -eq 0 ]; then
    echo "Please provide the day as an argument"
    exit 1
fi

day=$1
if ! [[ "$day" =~ ^(0[1-9]|1[0-9]|2[0-5])$ ]]; then
    echo "Invalid day provided"
    exit 1
fi

if [[ -d "day-$day" ]]; then
    echo "Directory for day-$day already exists"
    exit 1
fi

echo "Creating template for day-$day"
cp -r template day-$day
