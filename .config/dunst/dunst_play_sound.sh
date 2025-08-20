#!/usr/bin/bash

exclude_apps="com.github.zh-ch.YouTubeMusic;Spotify;Volume Control;Wallpaper"

if [[ ";$exclude_apps;" == *";$DUNST_APP_NAME;"* ]]; then
  exit 0
fi

sound=""
case "$5" in
"CRITICAL") sound="/usr/share/sounds/oxygen/stereo/dialog-error-veryserious.ogg" ;;
"NORMAL") sound="/usr/share/sounds/oxygen/stereo/bell.ogg" ;;
"LOW") sound="/usr/share/sounds/oxygen/stereo/message-lowpriority.ogg" ;;
*) sound="/usr/share/sounds/oxygen/stereo/bell.ogg" ;;
esac

echo "Playing sound: $sound"
mpv --no-video "$sound" &
