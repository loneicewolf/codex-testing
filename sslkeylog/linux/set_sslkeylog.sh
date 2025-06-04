#!/bin/sh
# Simple script to set SSLKEYLOGFILE for the current shell
# Usage: source ./set_sslkeylog.sh [log_file]

LOG_FILE="$1"
if [ -z "$LOG_FILE" ]; then
  LOG_FILE="$HOME/sslkeylog.log"
fi
export SSLKEYLOGFILE="$LOG_FILE"
echo "SSLKEYLOGFILE set to $SSLKEYLOGFILE"
