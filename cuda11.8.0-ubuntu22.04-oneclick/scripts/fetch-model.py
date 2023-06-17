#!/usr/bin/env python3
import sys
import os
import argparse
import subprocess
from urllib.parse import urlparse
from huggingface_hub import model_info

parser = argparse.ArgumentParser()
parser.add_argument('model', type=str)
parser.add_argument('output_folder', type=str)
args = parser.parse_args()

SCRIPT_DIR = "/root/scripts"

model = args.model.strip()
output_folder = args.output_folder

success=False
retry_count=0
while not success and retry_count < 10:
    os.makedirs(output_folder, exist_ok=True)
    os.chdir(output_folder)
    retry_count += 1
    print(f'Downloading {model} to {output_folder}, attempt {retry_count}')
    if 'http' in model.lower():
        # We've been passed a URL to download
        parsed = urlparse(model)
        # split the path by '/' and get the filename
        filename = parsed.path.split("/")[-1]
        print(f"Passed URL: {model}", flush=True)
        run = subprocess.run(f'/usr/bin/wget --continue --progress=dot:giga "{model}"', shell=True, check=False)
        write = filename
    elif model_info(model).id == model:
        # We've got an HF model, eg 'TheBloke/WizardLM-7B-Uncensored'
        print(f"Passed HF model: {model}", flush=True)
        model_folder = model.replace('/','_')
        run = subprocess.run(f'{SCRIPT_DIR}/download_model.py --threads 2 --output "{output_folder}/{model_folder}" "{args.model}"', shell=True, check=False)
        write = model_folder
    else:
        print(f"Error, {model} does not seem to be in a supported format.")
        success = False
        break
    if run.returncode == 0:
        # Succesful download. Write the model file or folder name to /tmp for use in --model arg
        with open('/tmp/text-gen-model', 'w') as f:
            f.write(write + '\n')
        success = True

# Exit 0 for success, 1 for failure
sys.exit(not success)
