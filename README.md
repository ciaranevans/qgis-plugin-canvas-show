# qgis-plugin-canvas-show
Reprex of an issue where QGIS Plugins QgsMapCanvas is not refreshing correctly

## Build

To prepare the plugin for installation in QGIS, ensure you're in the plugin folder and run:

```bash
$ pb_tool deploy -p ../build -y
```

## Running Plugin from a container

Ensure the plugin has been built, then in the root of the repository run one of the following:

### Mac

Follow the steps [here](https://medium.com/@mr.sahputra/running-qt-application-using-docker-on-macos-x-ad2e9d34532a), paste the IP inside DISPLAY variable of `run_qgis_mac.sh` and then:

```bash
$ ./utils/run_qgis_mac.sh
```

### Ubuntu/Linux

```bash
$ ./utils/run_qgis.sh
```

This will spin up a QGIS container with `QuickMapServices` and the plugin installed. You will have to navigate to `Plugins > Manage and Install Plugins... > Installed` and enable the plugin

## Running QT Designer from a container

In the root of the repository run one of the following:

### Mac

Follow the steps [here](https://medium.com/@mr.sahputra/running-qt-application-using-docker-on-macos-x-ad2e9d34532a), paste the IP inside DISPLAY variable of `run_qt_mac.sh` and then:

```bash
$ ./utils/run_qt_mac.sh
```

### Ubuntu/Linux

```bash
$ ./utils/run_qt.sh
```
