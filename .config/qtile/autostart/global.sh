#!/usr/bin/bash

# get hostname
HOSTNAME=$(cat /etc/hostname)
QTILE_CONFIG_PATH=$HOME/.config/qtile
AUTOSTART_SCRIPT=$HOME/.config/qtile/autostart/$HOSTNAME.sh

# PREREQUISITES
# set cursor
xsetroot -cursor_name left_ptr &

# init displays
bash /home/artur/.screenlayout/current &

# picom
picom -b &

# MAIN
# notifications
dunst & # handled by qtile

# wallpaper
nitrogen --restore &

# color scheme listener
bash $QTILE_CONFIG_PATH/wallust_on_wallpaper_change.sh &

# screensaver
#xscreensaver --no-splash &

# lock screen
# enable betterlockscreen@.service instead
# xss-lock -- $QTILE_CONFIG_PATH/lock-wrapper.sh &

# automount
udiskie -s -f "pcmanfm" &

# clipboard manager
copyq &

# kde connect tray
kdeconnect-indicator &

# flameshot screenshot tool
flameshot &

# redshift
redshift-gtk &

# discord overlay (discover-overlay)
discover-overlay &

# hostname-specific
if [[ -x "$AUTOSTART_SCRIPT" ]]; then
  bash $AUTOSTART_SCRIPT &
else
  dunstify -u low "Autostart" "Hostname-specific autostart script not found ($AUTOSTART_SCRIPT)"
fi
