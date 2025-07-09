#!/usr/bin/bash

# get hostname
HOSTNAME=$(cat /etc/hostname)
QTILE_CONFIG_PATH=$HOME/.config/qtile
AUTOSTART_SCRIPT=$HOME/.config/qtile/autostart/$HOSTNAME.sh


# PREREQUISITES
# init displays
bash /home/artur/.screenlayout/current &

# picom
picom -b &

# MAIN
# notifications
dunst & # handled by qtile

# wallpaper
nitrogen --restore &

# screensaver
#xscreensaver --no-splash &

# lock screen
# enable betterlockscreen@.service instead
# xss-lock -- $QTILE_CONFIG_PATH/lock-wrapper.sh &

# automount
udiskie -s -f "pcmanfm" &

# clipboard manager
copyq &

# replay manager
systemctl --user start replay-sorcery &

# kde connect tray
kdeconnect-indicator &

# flameshot screenshot tool
flameshot &

# redshift
redshift-gtk &

# hostname-specific
if [[ -x "$AUTOSTART_SCRIPT" ]]; then
    bash $AUTOSTART_SCRIPT &
else
    dunstify -u low "Autostart" "Hostname-specific autostart script not found ($AUTOSTART_SCRIPT)"
fi

