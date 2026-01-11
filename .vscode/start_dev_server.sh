#!/usr/bin/env bash
set -e
# kill any process listening on port 8000
if command -v lsof >/dev/null 2>&1; then
  PID=$(lsof -t -i:8000 || true)
  if [ -n "$PID" ]; then
    echo "Killing process on port 8000: $PID"
    kill $PID || true
    sleep 0.2
  fi
fi

echo "Starting python http.server on port 8000"
nohup python3 -m http.server 8000 --directory . > ./.vscode/server.log 2>&1 &
echo $! > ./.vscode/server.pid
echo "Server started with pid $(cat ./.vscode/server.pid)"
exit 0
