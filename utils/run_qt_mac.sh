#!/bin/bash

xhost +
docker run -it --rm --privileged --net=host -e DISPLAY=192.168.1.68:0 -v $(pwd):/workspace \
qgis/qgis:release-3_10_focal designer
