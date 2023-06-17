#!/bin/bash

# Check if we have /workspace
if [[ -d /workspace ]]
then
    # Check that /workspace is a mounted volume
    if /usr/bin/mount | /usr/bin/grep -o '/workspace' >/dev/null 2>&1
    then
        if [[ ! -d /workspace/models ]]
        then
            # If we don't already have /workspace/models, move the text-generation-webui default model folder there
            mv /root/text-generation-webui/models /workspace/models
        else
            # otherwise delete the default text-generation-webui model folder because we already have it on the volume
            rm -rf /root/text-generation-webui/models
        fi
        # Link the text-generation-webui model folder to the model folder on /workspace
        ln -s /workspace/models /root/text-generation-webui/models
    fi
fi
