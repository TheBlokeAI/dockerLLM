#!/usr/bin/env python3
import datetime
import os
import subprocess
import logging
import argparse

today_tag = datetime.datetime.now().strftime("%d%m%Y")

# Creating argparse parser
parser = argparse.ArgumentParser(description="Build Dockerfile")
parser.add_argument('docker', type=str, help='Name of the Dockerfile to build - should match a folder name in this repo')
parser.add_argument('--username', type=str, default="thebloke", help=f"Tag to use. Defaults to today's date: thebloke")
parser.add_argument('--tag', type=str, default=today_tag, help=f"Tag to use. Defaults to today's date: {today_tag}")
parser.add_argument('--latest', action="store_true", help='If specified, we will also tag and push :latest')
args = parser.parse_args()

logger = logging.getLogger()
logging.basicConfig(
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
)

dockerLLM_dir = os.path.dirname(os.path.realpath(__file__))
username = args.username

def docker_command(command):
    try:
        logger.info(f"Running docker command: {command}")
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Got error while executing docker command: {e}")
        raise
    except Exception as e:
        raise e

def build(docker_repo, tag, from_docker=None):
    docker_container = f"{username}/{docker_repo}:{tag}"
    logger.info(f"Building and pushing {docker_container}")

    docker_build_arg = f"--progress=plain -t {docker_container}"
    if from_docker is not None:
        docker_build_arg += f" --build-arg DOCKER_FROM={from_docker}"

    build_command = f"docker build {docker_build_arg} {dockerLLM_dir}/{docker_repo}"
    push_command = f"docker push {docker_container}"

    docker_command(build_command)
    docker_command(push_command)

    return docker_container

def tag(source_container, target_container):
    tag_command = f"docker tag {source_container} {target_container}"
    docker_command(tag_command)
    docker_command(f"docker push {target_container}")


try:
    container = build(args.docker, args.tag)
    logger.info(f"Successfully built and pushed the container to {container}")

    if args.latest:
        latest = f"{username}/{args.docker}:latest"
        tag(container, latest)
        logger.info(f"Successfully tagged and pushed to {latest}")

except subprocess.CalledProcessError as e:
    logger.error(f"Process aborted due to error running Docker commands")
except Exception as e:
    raise e

