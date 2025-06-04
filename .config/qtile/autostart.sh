#!/usr/bin/sh


# notifications
dunst & # handled by qtile

# wallpaper
nitrogen --restore &

# init displays
#xrandr --setprovideroutputsource NVIDIA-0 &
#xrandr --output DP-1 --mode 1920x1080 --rate 143.97 &
sh /home/artur/.screenlayout/current &
#x11vnc -usepw -repeat -forever -clip 1440x810+2800+1260 &

# picom
picom -b &

#/usr/bin/sh /home/artur/.config/qtile/bluetooth.sh &
#pulseaudio --daemonoize &

# screensaver
#xscreensaver --no-splash &

# lock screen
xss-lock -- betterlockscreen -l &

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

# philips hue (huenicorn)
# huenicorn &

# start qtile // must be last
# qtile start # disabled, qtile handles autostart
