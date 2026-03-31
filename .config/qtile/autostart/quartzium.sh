# replay manager
# systemctl --user start replay-sorcery &
gpu-screen-recorder \
  -c mkv \
  -w "DisplayPort-0|DisplayPort-1;x=2560;height=1080" \
  -k av1 \
  -fm content \
  -r 120 \
  -low-power yes \
  -a "default_output|default_input" \
  -v no \
  -sc "$HOME/Scripts/gpu-screen-recorder-notify.sh" \
  -o "$HOME/Videos/Replays" &

# mic loopback
pw-loopback &
