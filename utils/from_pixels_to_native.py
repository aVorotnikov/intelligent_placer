"""Transform polygon from pixel scale to native scale
"""

import json

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from intelligent_placer_lib.utils.get_polygon_list import get_polygon_list


JSON_FILE = "transformation.json"


with open(JSON_FILE, 'r') as jsonFile:
    data = json.load(jsonFile)

for polygon in data["polygons"]:
    polygonData = get_polygon_list(polygon["input"])
    ratio = polygon["ratio"]
    with open(polygon["input"], 'w') as polygonFile:
        for vert in polygonData:
            polygonFile.write("{:.2f} {:.2f}\n".format(vert[0] / ratio, vert[1] / ratio))
