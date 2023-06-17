#!/bin/bash

echo -n "Restarting text-generation-webui: "

if pkill -f "python3 server.py"
then
    echo "DONE"
    echo "The UI will auto-restart in 2 seconds"
else
    echo "was not running"
fi
