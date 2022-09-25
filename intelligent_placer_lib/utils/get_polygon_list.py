"""Getting polygon from file with get_polygon_list function
"""

import string


def get_polygon_list(path : string):
    """Get polygon vertices from file

    :param path: Path to polygon vertices file
    :type path: str
    :returns: Polygon vertices list
    :rtype: list
    """
    with open(path, 'r') as polygonFile:
        res = []
        for line in polygonFile:
            strippedLine = line.strip()
            if 0 == len(strippedLine):
                continue
            if '#' == strippedLine[0]:
                continue
            splittedLine = strippedLine.split()
            if 2 != len(splittedLine):
                raise RuntimeError(f"Incorrect line in '{path}' polygon file: {line}")
            res.append((float(splittedLine[0]), float(splittedLine[1])))
        return res
