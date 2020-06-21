#!/bin/bash

xhost +
docker build -t qgis-development:latest -f utils/Dockerfile .
docker run -it --rm --privileged --net=host --env="DISPLAY" -v $(pwd):/workspace \
qgis-development:latest qgis
