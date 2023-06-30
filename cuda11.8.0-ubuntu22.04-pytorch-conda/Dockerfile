ARG CUDA_VERSION="11.8.0"
ARG CUDNN_VERSION="8"
ARG UBUNTU_VERSION="22.04"

# Base NVidia CUDA Ubuntu image
FROM nvidia/cuda:$CUDA_VERSION-cudnn$CUDNN_VERSION-devel-ubuntu$UBUNTU_VERSION AS base

ENV HOME /root
WORKDIR $HOME
ENV PYTHON_VERSION=3.10
ENV PATH="/usr/local/cuda/bin:${PATH}"
#
# Install Python plus openssh, which is our minimum set of required packages.
# Install useful command line utility software
ARG APTPKGS="zsh wget tmux tldr nvtop vim neovim curl rsync net-tools less iputils-ping 7zip zip unzip"
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get install -y --no-install-recommends openssh-server openssh-client git git-lfs && \
    python3 -m pip install --upgrade pip && \
    apt-get install -y --no-install-recommends $APTPKGS && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Miniconda for Python env management
ENV PATH="${HOME}/miniconda3/bin:${PATH}"
ENV BASEPATH="${PATH}"
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir ${HOME}/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b -p ${HOME}/miniconda3 \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

# Make base conda environment
ENV CONDA=pytorch
RUN conda create -n "${CONDA}" python="${PYTHON_VERSION}"
ENV PATH="${HOME}/miniconda3/envs/${CONDA}/bin:${BASEPATH}"

# Install pytorch
ARG PYTORCH="2.0.1"
ARG CUDA="118"
RUN pip3 install --no-cache-dir -U torch==$PYTORCH torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu$CUDA

# Set up git to support LFS, and to store credentials; useful for Huggingface Hub
RUN git config --global credential.helper store && \
    git lfs install

# Install Oh My Zsh for better command line experience: https://github.com/ohmyzsh/ohmyzsh
RUN bash -c "ZSH=$HOME/ohmyzsh $(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Add some config files for a nicer command line setup
COPY conf-files/vimrc $HOME/.vimrc
COPY conf-files/zshrc $HOME/.zshrc
COPY conf-files/thebloke.zsh-theme $HOME/ohmyzsh/custom/themes/
COPY conf-files/tmux.conf $HOME/.tmux.conf
# Additional ZSH config files
COPY conf-files/.zsh $HOME/.zsh
# Set default shell to ZSH
COPY conf-files/passwd /etc/passwd

# Install Neovim 0.9 and overwrite apt nvim with it (we still installed via apt as it installs various dependencies like LuaJIT)
RUN wget https://github.com/neovim/neovim/releases/download/v0.9.1/nvim-linux64.tar.gz && \
    tar xzvf $HOME/nvim-linux64.tar.gz && \
    rm nvim-linux64.tar.gz && \
    rm /usr/bin/nvim && \
    ln -s $HOME/nvim-linux64/bin/nvim /usr/bin/nvim

# Set up neovim lazy starter pack and launch nvim once to set up the plugins
RUN git clone https://github.com/LazyVim/starter $HOME/.config/nvim && \
    /usr/bin/nvim --headless -c ':q'

COPY --chmod=755 start-ssh-only.sh /start.sh

WORKDIR /workspace

CMD [ "/start.sh" ]
