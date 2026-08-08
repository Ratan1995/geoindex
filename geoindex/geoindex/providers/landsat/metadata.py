"""
Landsat metadata reader.

Reads metadata from the official USGS *_MTL.txt file.
"""

from pathlib import Path


def find_mtl_file(path: str) -> Path:
    """
    Find the Landsat MTL.txt file.
    """

    root = Path(path)

    if not root.exists():
        raise FileNotFoundError(path)

    for file in root.iterdir():
        if file.is_file() and file.name.endswith("_MTL.txt"):
            return file

    raise FileNotFoundError("MTL.txt not found.")


from geoindex.core.metadata import Metadata

def read_mtl(path: str) -> Metadata:
    """
    Read a Landsat MTL file and return a generic Metadata object.
    """

    mtl_file = find_mtl_file(path)

    values = {}

    with open(mtl_file, "r") as f:

        for line in f:

            line = line.strip()

            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            values[key.strip()] = value.strip().replace('"', "")

    return Metadata(
        spacecraft=values.get("SPACECRAFT_ID"),
        sensor=values.get("SENSOR_ID"),
        provider="USGS",
        acquisition_date=values.get("DATE_ACQUIRED"),
        processing_level=values.get("PROCESSING_LEVEL"),
        collection=values.get("COLLECTION_NUMBER"),
    )