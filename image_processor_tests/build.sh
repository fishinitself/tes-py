#!/bin/bash

version="1.0-amd64"
image_name="ersh/iptests_py:$version"

check_command_status() {
    if [ $? -ne 0 ]; then
        echo "Error: Command failed."
        exit 1
    fi
}

# Build the Docker image
docker build --platform linux/amd64 -t $image_name .
check_command_status

# Log in to Docker
docker login
check_command_status

# Push the Docker image
docker push $image_name
check_command_status