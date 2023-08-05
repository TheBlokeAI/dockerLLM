ARG CUDA_VERSION="11.8.0"
ARG CUDNN_VERSION="8"
ARG UBUNTU_VERSION="22.04"

# Base image
FROM thebloke/cuda$CUDA_VERSION-ubuntu$UBUNTU_VERSION-oneclick:latest as base

RUN pip3 install runpod requests

COPY scripts/rp_handler.py /root/scripts

COPY --chmod=755 start-with-ui.sh /start.sh

WORKDIR /workspace

CMD [ "/start.sh" ]
