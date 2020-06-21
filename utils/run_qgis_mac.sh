#!/bin/bash

xhost +
docker build -t qgis-development:latest -f utils/Dockerfile .
docker run -it --rm --privileged --net=host -e DISPLAY=192.168.1.68:0 -v $(pwd):/workspace \
qgis-development:latest qgis
