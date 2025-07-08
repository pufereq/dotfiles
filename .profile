#!/bin/sh
export PATH=$PATH:/home/artur/.local/bin:/home/artur/.spicetify
export XDG_DATA_HOME=/home/artur/.local/share
# export QT_QPA_PLATFORMTHEME="qt6ct"
export EDITOR=nvim

cpc () {  
  if [ $# -eq 0 ]; then
    >&2 echo "Usage: cpc <file>"
  else
    cat $1 | xclip -selection clipboard
    >&2 echo "Copied contents of $1 to clipboard."
  fi
}

alias update="time yay -Syu && time flatpak update"
alias xx="exit"

colortest
fortune
