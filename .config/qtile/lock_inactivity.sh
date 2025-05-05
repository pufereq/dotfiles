#!/bin/bash

xscreensaver-command -activate &
xscreensaver-command -watch | while read -r line
do
    if [[ ${line::1} == U ]]
    then
        betterlockscreen -l
        killall xscreensaver-command
    fi
done
