#!/bin/sh
export PATH=$PATH:/home/artur/.local/bin:/home/artur/.spicetify
export EDITOR=nvim

cpc() {
  if [ $# -eq 0 ]; then
    >&2 echo "Usage: cpc <file>"
  else
    xclip -selection clipboard <"$1"
    >&2 echo "Copied contents of $1 to clipboard."
  fi
}

alias update="time yay -Syu && time flatpak update"
alias xx="exit"

colortest
fortune
