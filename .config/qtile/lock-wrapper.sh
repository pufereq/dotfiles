#!/bin/bash
CURRENT=$(brightnessctl get)

brightnessctl set 0
xset dpms force off
betterlockscreen -l &
sleep 2
xset dpms force on
$HOME/.config/qtile/fade-in-screen.sh $CURRENT

