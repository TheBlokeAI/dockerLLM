#!/bin/bash

# Ensure we have /workspace in all scenarios
mkdir -p /workspace

if [[ ! -d /workspace/text-generation-webui ]]; then
	# If we don't already have /workspace/text-generation-webui, move it there
	mv /root/text-generation-webui /workspace
else
	# otherwise delete the default text-generation-webui folder which is always re-created on pod start from the Docker
	rm -rf /root/text-generation-webui
fi

# Then link /root/text-generation-webui folder to /workspace so it's available in that familiar location as well
ln -s /workspace/text-generation-webui /root/text-generation-webui
