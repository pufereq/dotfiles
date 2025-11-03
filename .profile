#!/bin/zsh
export PATH=$PATH:/home/artur/.local/bin:/home/artur/.spicetify
export EDITOR=nvim
export TERMINAL=alacritty
export QT_STYLE_OVERRIDE=kvantum
export QT_QPA_PLATFORMTHEME=qt6ct

cpc() {
  if [ $# -eq 0 ]; then
    >&2 echo "Usage: cpc <file>"
  else
    xclip -selection clipboard <"$1"
    >&2 echo "Copied contents of $1 to clipboard."
  fi
}

source <(fzf --zsh)

alias update="time yay -Syu && time flatpak update"
alias xx="exit"

colortest
fortune
