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
    
def read_mtl(path: str) -> dict:
    """
    Read the Landsat MTL.txt file.

    Parameters
    ----------
    path : str
        Landsat product folder.

    Returns
    -------
    dict
        Metadata as key-value pairs.
    """

    mtl_file = find_mtl_file(path)

    metadata = {}

    with open(mtl_file, "r") as f:

        for line in f:

            line = line.strip()

            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            metadata[key.strip()] = value.strip()

    return metadata