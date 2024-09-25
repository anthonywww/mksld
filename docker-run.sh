#!/bin/bash

IMAGE_NAME="mksld"
CONTAINER_NAME="mksld-downloader"

# Check if the image exists, if not, build it
if [[ "$(docker images -q ${IMAGE_NAME} 2> /dev/null)" == "" ]]; then
  echo "Image does not exist. Building..."
  docker build -t ${IMAGE_NAME} .
else
  echo "Image exists. Skipping build."
fi

# Run the container
docker run --rm -u "$(id -u):$(id -g)" -v "/$(pwd):/app" ${IMAGE_NAME}
