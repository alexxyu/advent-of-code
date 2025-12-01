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
    fday="0${aoc_day}"
fi

print -P "%F{green}Creating template for day-${fday}...%f"

for fname in template/*; do
    newpath=$(echo "$fname" | sed "s/{{aoc_day}}/${aoc_day}/g")
    newfname=$(basename $newpath)
    if [[ -e $newfname ]]; then
        print -P "%F{red}File '${newfname}' already exists!%f"
        continue
    fi
    cat "$fname" | sed "s/{{aoc_day}}/${aoc_day}/g" > "${newfname}"
done
