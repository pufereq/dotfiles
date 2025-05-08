#!/usr/bin/env sh

# This script ensures that a given process is running.
# It starts the process and restarts if it stops.
# Sends a notification if the process is not running.

# Usage: ./ensure-running.sh <process_name>
# Example: ./ensure-running.sh my_process


process_name="$1"

if [ -z "$process_name" ]; then
  echo "Usage: $0 <process_name>"
  exit 1
fi

function process_running() {
  # check if the process is running
  if pgrep -x "$process_name" > /dev/null; then
    return 0
  else
    return 1
  fi
}

function start_process() {
  # start the process
  echo "Starting $process_name..."
  "$process_name" &
}

function notify() {
  echo "$process_name is not running"
  dunstify -u critical -a ensure-running.sh "$process_name is not running" "Starting $process_name..."
}

while true; do
  if ! process_running; then
    notify
    start_process
  fi

  sleep 5
done
