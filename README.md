# TheBloke's Docker templates

### Update: 16 December 2023 - Rebuild to add Mixtral support
* Should now support Mixtral, with updated AutoGPTQ 0.6 and llama-cpp-python 0.2.23
* Updated PyTorch to 2.1.1

### Update: 11 October 2023 - Update API command line option
* Container will now launch text-generation-webui with arg `--extensions openai`
* Logs from text-generation-webui will now appear in the Runpod log viewer, as well as `/workspace/logs/text-generation-webui.log`

### Update: 8th October 2023 - CUDA 12.1.1, fixed ExLlamav2 issues
* The instances now use CUDA 12.1.1, which fixes issues with EXL2
* Note that for now the main container is still called cuda11.8.0-ubuntu22.04-oneclick
* This is because I need to get in touch with Runpod to update the name of the container used in their instances
* This is just a naming issue; the container does now use CUDA 12.1.1 and EXL2 is confirmed to work again.

### Update: 23rd July 2023 - Llama 2 support, including Llama 2 70B in ExLlama
* Llama 2 models, including Llama 2 70B, are now fully supported
* Updated to latest text-generation-webui `requirements.txt`
* Removed the exllama pip package installed by text-generation-webui
  * Therefore the ExLlama kernel will build automatically on first use
  * This ensures that ExLlama is always up-to-date with any new ExLlama commits (which are pulled automatically on each boot)
* Added simple build script for building the Docker containers

### Update: 28th June 2023 - SuperHOT fixed
* Updated to latest ExLlama code, fixing issue with SuperHOT GPTQs
* ExLlama now automaticaly updates on boot, like text-generation-webui already did
  * This should result in the template automatically supporting new ExLlama features in future
    
### Update: 19th June 2023
* Major update to the template
* text-generation-webui is now integrated with:
  * AutoGPTQ with support for all Runpod GPU types
  * ExLlama, turbo-charged Llama GPTQ engine - performs 2x faster than AutoGPTQ (Llama 4bit GPTQs only)
  * CUDA-accelerated GGML support, with support for all Runpod systems and GPUs.
* All text-generation-webui extensions are included and supported (Chat, SuperBooga, Whisper, etc).
* text-generation-webui is always up-to-date with the latest code and features.
* Automatic model download and loading via environment variable `MODEL`.
* Pass text-generation-webui parameters via environment variable `UI_ARGS`.

## Runpod: TheBloke's Local LLMs UI

[Runpod template link](https://runpod.io/gsc?template=qk29nkmbfr&ref=eexqfacd)

[Full documentation is available here](https://github.com/TheBlokeAI/dockerLLM/blob/main/README_Runpod_LocalLLMsUI.md)

## Runpod: TheBloke's Local LLMs UI & API

[Runpod template link](https://runpod.io/gsc?template=f1pf20op0z&ref=eexqfacd)

[Full documentation is available here](https://github.com/TheBlokeAI/dockerLLM/blob/main/README_Runpod_LocalLLMsUIandAPI.md)
