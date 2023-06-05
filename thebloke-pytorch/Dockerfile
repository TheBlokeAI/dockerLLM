ARG CUDA_VERSION="12.0.1"
ARG CUDNN_VERSION="8"
ARG UBUNTU_VERSION="22.04"

FROM nvidia/cuda:$CUDA_VERSION-cudnn$CUDNN_VERSION-devel-ubuntu$UBUNTU_VERSION

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-venv && \
    python3 -m pip install --upgrade pip && \
    apt-get install -y --no-install-recommends openssh-server openssh-client &&
    apt-get install -y --no-install-recommends wget tmux vim curl zsh net-tools less git-lfs && \
    apt-get install -y --no-install-recommends 7zip p7zip zip unzip rsync libopenblas-dev && \
    apt-get install -y --no-install-recommends libopenblas-base iputils-ping traceroute zlib1g zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git config --global credential.helper store &&
    git lfs install

COPY ../conf-files/bashrc /root/.bashrc
COPY ../conf-files/vimrc /root/.vimrc
COPY ../conf-files/zshrc /root/.zshrc
COPY ../conf-files/tmux.conf /root/.tmux.conf
COPY ../conf-files/iterm2_shell_integration.zsh /root/.iterm2_shell_integration.zsh
COPY ../conf-files/iterm2_shell_integration.bash /root/.iterm2_shell_integration.bash
COPY ../conf-files/passwd /etc/passwd

COPY --chmod=755 start.sh /

WORKDIR /workspace

CMD [ "/start.sh" ]
