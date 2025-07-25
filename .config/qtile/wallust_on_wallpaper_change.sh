#!/usr/bin/bash

last_wallpaper=""

inotifywait -m -e modify ~/.config/nitrogen/bg-saved.cfg |
    while read -r file_path file_event file_name; do
        wallpaper=$(grep "file" "$file_path$file_name" | cut -d= -f2)

        if [[ "$wallpaper" == "$last_wallpaper" ]]; then
            echo "Wallpaper has not changed, skipping..."
            continue
        fi

        last_wallpaper=$wallpaper

        # set colorscheme
        wallust run "$wallpaper"

        # reload dunst
        killall dunst
        dunst &

        # reload qtile
        qtile cmd-obj -o root -f reload_config &

        # send notification
        dunstify -t 3000 -u low -a "Wallpaper" "Wallpaper changed" "Wallpaper and colorscheme have been changed."
    done
