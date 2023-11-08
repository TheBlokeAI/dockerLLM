#!/usr/bin/env python3
import datetime
import os
import subprocess
import logging

logger = logging.getLogger()
logging.basicConfig(
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
)

dockerLLM_dir = os.path.dirname(os.path.realpath(__file__))
username = "thebloke"

def build(docker_repo, tag, from_docker=None):
    docker_container = f"{username}/{docker_repo}:{tag}"
    logger.info(f"Building and pushing {docker_container}")

    docker_build_arg = f"--progress=plain -t {docker_container}"
    if from_docker is not None:
        docker_build_arg += f" --build-arg DOCKER_FROM={from_docker}"

    build_command = f"docker build {docker_build_arg} {dockerLLM_dir}/{docker_repo}"
    push_command = f"docker push {docker_container}"
    
    try:
        logger.info(f"Building {docker_repo} using command: {build_command}")
        subprocess.check_call(build_command, shell=True)

        logger.info(f"Pushing {docker_repo} using command: {push_command}")
        subprocess.check_call(push_command, shell=True)

        return docker_container
    except subprocess.CalledProcessError as e:
        logger.error(f"Got error while executing docker command: {e}")
        raise
    except Exception as e:
        raise e

today_tag = datetime.datetime.now().strftime("%d%m%Y")

try:
    pytorch_container = build("cuda12.1.1-ubuntu22.04-pytorch", "1")
    textgen_container = build("cuda12.1.1-ubuntu22.04-textgen", today_tag, pytorch_container)
    oneclick_container = build("cuda11.8.0-ubuntu22.04-oneclick", today_tag, textgen_container)

    logger.info(f"Successfully built and pushed {oneclick_container}")
except subprocess.CalledProcessError as e:
    logger.error(f"Process aborted due to error running Docker commands")
except Exception as e:
    raise e
