ARG CUDA_VERSION="11.8.0"
ARG CUDNN_VERSION="8"
ARG UBUNTU_VERSION="22.04"

# Base pytorch image
FROM thebloke/cuda$CUDA_VERSION-ubuntu$UBUNTU_VERSION-pytorch:latest as base

WORKDIR /root

# Install text-generation-webui, including all extensions
# Also includes exllama
RUN git clone https://github.com/oobabooga/text-generation-webui && \
    cd text-generation-webui && \
    pip3 install -r requirements.txt && \
    bash -c 'for req in extensions/*/requirements.txt ; do pip3 install -r "$req" ; done' && \
    mkdir -p repositories && \
    cd repositories && \
    git clone https://github.com/turboderp/exllama

# Install AutoGPTQ, overwriting the version automatically installed by text-generation-webui
ARG AUTOGPTQ="0.2.2"
ENV CUDA_VERSION=""
ENV GITHUB_ACTIONS=true
ENV TORCH_CUDA_ARCH_LIST="8.0;8.6+PTX;8.9;9.0" 
RUN pip3 uninstall -y auto-gptq && \
    pip3 install --no-cache-dir auto-gptq==$AUTOGPTQ
