# TheBloke's Docker templates

### Update: 23rd July 2023 - Llama 2 support, including Llama 2 70B in ExLlama
* Llama 2 models, including Llama 2 70B, are now fully supported
* Updated to latest text-generation-webui `requirements.txt`
* Removed the exllama pip package installed by text-generation-webui
  * Therefore the ExLlama kernel will build automatically on first use
  * This ensures that ExLlama is always up-to-date with any new ExLlama commits (which are pulled automatically on each boot)

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
