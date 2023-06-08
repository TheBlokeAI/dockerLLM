ARG CUDA_VERSION="12.0.1"
ARG CUDNN_VERSION="8"
ARG UBUNTU_VERSION="22.04"

# Base NVidia CUDA Ubuntu image
FROM nvidia/cuda:$CUDA_VERSION-cudnn$CUDNN_VERSION-devel-ubuntu$UBUNTU_VERSION

# Install Python plus openssh, which is our minimum set of required packages.
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get install -y --no-install-recommends openssh-server openssh-client && \
    python3 -m pip install --upgrade pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install useful utility software, and libraries that may be needed by other software
RUN apt-get install -y --no-install-recommends zsh wget tmux vim curl net-tools less git-lfs && \
    apt-get install -y --no-install-recommends 7zip p7zip zip unzip rsync libopenblas-dev libopenblas-base && \
    apt-get install -y --no-install-recommends iputils-ping traceroute zlib1g zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up git to support LFS, and to store credentials; useful for Huggingface Hub
RUN git config --global credential.helper store &&
    git lfs install

# Install Oh My Zsh for better command line experience: https://github.com/ohmyzsh/ohmyzsh
RUN sh -c "ZSH=/root/ohmyzsh $(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Add config files with useful defaults and user-friendly features for users SSHing in
COPY ../conf-files/zshrc /root/.zshrc
COPY ../conf-files/bashrc /root/.bashrc
COPY ../conf-files/vimrc /root/.vimrc
COPY ../conf-files/tmux.conf /root/.tmux.conf
# For users running iTerm2 on macOS : https://iterm2.com/documentation-shell-integration.html
COPY ../conf-files/iterm2_shell_integration.zsh /root/.iterm2_shell_integration.zsh
COPY ../conf-files/iterm2_shell_integration.bash /root/.iterm2_shell_integration.bash
# Change shell of root user to zsh - is there a better way than this? chsh -s /usr/bin/zsh root did not work.
COPY ../conf-files/passwd /etc/passwd

COPY --chmod=755 start.sh /

WORKDIR /workspace

CMD [ "/start.sh" ]
