from qgis.core import QgsFeature, QgsGeometry, QgsVectorLayer, QgsProject


class RandomTab:
    def __init__(self, dlg):
        self.dlg = dlg
        self.dlg.doAThingButton.clicked.connect(self._add_thing_to_map)

    def _add_thing_to_map(self):
        wkt = "POLYGON((-0.2105573979070674 51.690526563312446,-0.2819685307195674 51.72796893321153,-0.4467634525945674 51.71435711183883,-0.5511335697820674 51.55411111971043,-0.5071882572820674 51.485749548234764,-0.5621198979070674 51.40015323665627,-0.3533796635320674 51.245675372871425,-0.1336531010320674 51.266302487469574,0.025648656780452583 51.262865277703824,0.3387590083429526 51.297225808893636,0.22889572709295258 51.403580169765206,0.2673478755304526 51.48917006409212,0.2838273677179526 51.567771121919726,0.19044357865545258 51.663276279969544,0.04762131303045258 51.70074119245276,-0.2105573979070674 51.690526563312446))"
        geom = QgsGeometry.fromWkt(wkt)
        feature = QgsFeature()
        feature.setGeometry(geom)
        features = []
        features.append(feature)
        layer = QgsVectorLayer("Polygon?crs=EPSG:4326", "Features", "memory")
        layer.dataProvider().addFeatures(features)
        QgsProject().instance().addMapLayer(layer, False)
        self.dlg.mapWidget.setExtent(layer.extent())
        self.dlg.mapWidget.setLayers([layer])
