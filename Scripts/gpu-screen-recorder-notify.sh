#!/usr/bin/env bash

FILEPATH=$1
# TYPE=$2

if [[ -f "$FILEPATH" ]]; then
  notify-send -u low -a "gpu-screen-recorder (script)" "GPU Screen Recorder" "Recording saved to $FILEPATH"
else
  notify-send -u normal -a "gpu-screen-recorder (script)" "GPU Screen Recorder" "Recording failed. No file found at $FILEPATH"
fi
