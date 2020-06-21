#!/bin/bash

xhost +
docker run -it --rm --privileged --net=host --env="DISPLAY" -v $(pwd):/workspace \
qgis/qgis:release-3_10_focal designer
