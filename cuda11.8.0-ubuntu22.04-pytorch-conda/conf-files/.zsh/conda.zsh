# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!

# Default conda home is in the container
CONDA="$HOME/miniconda3"

# But if there's one on the volume, use that instead
if [[ -d /workspace/miniconda3 ]]; then
  CONDA=/workspace/miniconda3
fi

__conda_setup="$('$CONDA/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "$CONDA/etc/profile.d/conda.sh" ]; then
        . "$CONDA/etc/profile.d/conda.sh"
    else
        export PATH="$CONDA/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

if [[ -d "$CONDA/envs/pytorch" ]]; then
  conda activate pytorch
fi
