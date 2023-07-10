ARG CUDA_VERSION="11.8.0"
ARG CUDNN_VERSION="8"
ARG UBUNTU_VERSION="22.04"

# Base image
FROM thebloke/cuda$CUDA_VERSION-ubuntu$UBUNTU_VERSION-pytorch-conda:latest as base

ENV HOME /root
WORKDIR $HOME

# Install LmSys FastChat, plus also deepspeed which can be used with FastChat instead of torchrun
ENV CONDA=fastchat
RUN conda create -n "${CONDA}" --clone pytorch
ENV PATH="${HOME}/miniconda3/envs/${CONDA}/bin:${BASEPATH}"
RUN git clone https://github.com/lm-sys/FastChat && \
    cd FastChat && \
    pip3 install -e .  && \
    pip3 install deepspeed

# Install OpenAccess AI Collective's Axoltl
#ENV CONDA=axolotl
#RUN conda create -n "${CONDA}" --clone pytorch
#ENV PATH="${HOME}/miniconda3/envs/${CONDA}/bin:${BASEPATH}"
#RUN git clone https://github.com/OpenAccess-AI-Collective/axolotl && \
#    cd axolotl && \
#    pip3 install -e .

# Install AetherCortex's Llama-X, which is used by WizardLM for example
#ENV CONDA=llamax
#RUN conda create -n "${CONDA}" --clone pytorch
#ENV PATH="${HOME}/miniconda3/envs/${CONDA}/bin:${BASEPATH}"
#RUN git clone https://github.com/AetherCortex/Llama-X && \
#    cd Llama-X && \
#    pip3 install transformers==4.29.2 && \
#    pip3 install -r requirements.txt

# Clone the WizardLM codebase
#RUN git clone https://github.com/nlpxucan/WizardLM
