"""Main library file

Contains main library functind - check_image

Need 2 arguments if script is executed:
    * path to image
    * path to polygon coordinates file

Example of script executing:
"""

import argparse
import string

from utils.get_polygon_list import get_polygon_list

def check_image(path : string, polygon : list):
    """Check if objects on image can be placed inside polygon

    :param path: Path to image with objects
    :type path: str
    :param polygon: List of polygon vertices
    :type polygon: list
    :returns: True if objects can be placed inside polygon, False - otherwise
    :rtype: bool
    """
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'img',
        type=str,
        help="Path to image"
    )
    parser.add_argument(
        'polygon',
        type=str,
        help="Path to polygon file"
    )
    args = parser.parse_args()
    check_image(args.img, get_polygon_list(args.polygon))
