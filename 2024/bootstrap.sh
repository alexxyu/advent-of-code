#!/bin/zsh
real_day=$(date +%d)
aoc_day=$(( (real_day % 30) + 1 ))
if [ $# -gt 1 ]; then
    echo "Expected exactly zero or one argument"
    exit 1
elif [ $# -eq 1 ]; then
    aoc_day=$1
fi

fday=$aoc_day
if [ $aoc_day -lt 10 ]; then
    fday="0$aoc_day"
fi

echo "Creating template for day-$fday"

if [[ -d "day-$fday" ]]; then
    echo "Directory for day-$fday already exists"
    exit 1
fi

cp -r template day-$fday
grep -rl "{{aoc_day}}" day-$fday | xargs sed -i "" "s/{{aoc_day}}/$aoc_day/g"
