#!/usr/bin/env bash

MESLO_URL=$(
  curl -s https://api.github.com/repos/ryanoasis/nerd-fonts/releases/latest |
    grep -E 'Meslo\.tar\.xz"$' |
    cut -d : -f 2,3 |
    tr -d \" | tr -d " "
)
MONASPACE_URL=$(
  curl -s https://api.github.com/repos/ryanoasis/nerd-fonts/releases/latest |
    grep -E 'Monaspace\.tar\.xz"$' |
    cut -d : -f 2,3 |
    tr -d \" | tr -d " "
)

# create a temporary directory
TEMP_DIR=$(mktemp -d)

# download
echo "Downloading fonts..."
curl -Lo "$TEMP_DIR/Meslo.tar.xz" "$MESLO_URL"
curl -Lo "$TEMP_DIR/Monaspace.tar.xz" "$MONASPACE_URL"

# extract to the fonts directory
echo "Extracting fonts..."
mkdir -p "$HOME/.local/share/fonts"

mkdir -p "$HOME/.local/share/fonts/Meslo"
mkdir -p "$HOME/.local/share/fonts/Monaspace"

tar -xf "$TEMP_DIR/Meslo.tar.xz" -C "$HOME/.local/share/fonts/Meslo"
tar -xf "$TEMP_DIR/Monaspace.tar.xz" -C "$HOME/.local/share/fonts/Monaspace"

# clean up
rm -rf "$TEMP_DIR"

fc-cache -f -v

echo "Fonts installed successfully!"
