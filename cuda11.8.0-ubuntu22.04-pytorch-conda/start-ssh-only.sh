#!/bin/bash

echo "TheBloke LLM: pod started"
echo "For more info, see: https://github.com/TheBlokeAI/dockerLLM"

if [[ $PUBLIC_KEY ]]; then
	mkdir -p ~/.ssh
	chmod 700 ~/.ssh
	cd ~/.ssh
	echo "${PUBLIC_KEY}" >>authorized_keys
	chmod 700 -R ~/.ssh
	cd /
	service ssh start
fi

sleep infinity
