#!/bin/sh
# script appname summary body icon urgency

if [ "$1" = "Spotify" ]; then
    exit
fi

if [ "$5" == "CRITICAL" ]; then
    mpv --no-video /usr/share/sounds/oxygen/stereo/dialog-error-veryserious.ogg &
elif [ "$5" == "NORMAL" ]; then
    mpv --no-video /usr/share/sounds/oxygen/stereo/bell.ogg &
elif [ "$5" == "LOW" ]; then
    mpv --no-video /usr/share/sounds/oxygen/stereo/message-lowpriority.ogg &
else
    mpv --no-video /usr/share/sounds/oxygen/stereo/bell.ogg &
fi
echo "$1 $2 $3 $4 $5"

