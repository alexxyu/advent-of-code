#!/bin/zsh
if [ $# -eq 0 ]; then
    echo "Please provide the day as an argument"
    exit 1
fi

cp -r template day-$1
