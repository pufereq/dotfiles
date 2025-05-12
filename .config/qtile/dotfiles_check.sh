#!/bin/sh

UPSTREAM=${1:-'@{u}'}
LOCAL=$(yadm rev-parse @)
REMOTE=$(yadm rev-parse "$UPSTREAM")
BASE=$(yadm merge-base @ "$UPSTREAM")

STATE=""

if [ $LOCAL = $REMOTE ]; then
    STATE="up-to-date"
elif [ $LOCAL = $BASE ]; then
    STATE="pull"
elif [ $REMOTE = $BASE ]; then
    STATE="push"
else
    STATE="diverged"
fi


if [ "$STATE" = "up-to-date" ]; then
    MESSAGE=""
elif [ "$STATE" = "pull" ]; then
    MESSAGE="There are new changes on the remote branch."
elif [ "$STATE" = "push" ]; then
    MESSAGE="There are local changes that need to be pushed."
else
    MESSAGE="The branches have diverged. Please resolve the conflicts."
fi

if [ "$MESSAGE" != "" ]; then
    dunstify -a "yadm" -u normal -i "$HOME/.local/share/icons/Adwaita/32x32/status/changes-preference-symbolic.svg" \
	"Dotfiles Status" "$MESSAGE"
fi

