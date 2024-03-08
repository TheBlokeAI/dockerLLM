ARG CUDA_VERSION="12.1.1"
ARG CUDNN_VERSION="8"
ARG UBUNTU_VERSION="22.04"
ARG DOCKER_FROM=thebloke/cuda$CUDA_VERSION-ubuntu$UBUNTU_VERSION-pytorch:latest 

# Base pytorch image
FROM $DOCKER_FROM as base

WORKDIR /root

# Install text-generation-webui, including all extensions
# Also includes exllama
# We remove any installed exllamav2 and use the same version used on text-generation-webui
# We remove the ExLlama automatically installed by text-generation-webui
# so we're always up-to-date with any ExLlama changes, which will auto compile its own extension
RUN git clone https://github.com/oobabooga/text-generation-webui && \
    cd text-generation-webui && \
    pip3 uninstall exllamav2 && \
    pip3 install -r requirements.txt && \
    bash -c 'for req in extensions/*/requirements.txt ; do pip3 install -r "$req" ; done' && \
    #pip3 uninstall -y exllama && \
    mkdir -p repositories && \
    cd repositories && \
    git clone https://github.com/turboderp/exllama && \
    pip3 install -r exllama/requirements.txt

# Install AutoGPTQ, overwriting the version automatically installed by text-generation-webui
# May not be needed any more? But just in case
#RUN pip3 uninstall -y auto-gptq && \
#    pip3 install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/
