#!/usr/bin/env python3
import datetime
import os
import subprocess
import logging

logger = logging.getLogger()
logging.basicConfig(
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
)

dockerLLM = "/workspace/dockerLLM"
repo = "thebloke"

def build(tag, docker, from_docker=None):
    logger.info(f"Building and pushing {repo}/{docker}:{tag}")

    docker_build_arg=f"--progress=plain -t {repo}/{docker}:{tag}"

    if from_docker is not None:
        docker_build_arg += f" --build-arg DOCKER_FROM={from_docker}"

    build_command = f"docker build {docker_build_arg} {dockerLLM}/{docker}"
    push_command = f"docker push {repo}/{docker}:{tag}"
    
    try:
        subprocess.check_call(build_command, shell=True)
        subprocess.check_call(push_command, shell=True)
        return True
    except Exception as e:
        print(f"Failed to execute command: {e}")
        raise e

today_tag = datetime.datetime.now().strftime("%d%m%Y")

try:
    build("1", "cuda11.8.0-ubuntu22.04-pytorch")
    build(today_tag, "cuda11.8.0-ubuntu22.04-textgen", f"{repo}/cuda11.8.0-ubuntu22.04-pytorch:1")
    build(today_tag, "cuda11.8.0-ubuntu22.04-oneclick", f"{repo}/cuda11.8.0-ubuntu22.04-textgen:{today_tag}")
except Exception as e:
    logger.error(f"Process failed due to exception: {e}")
