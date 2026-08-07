"""
Landsat product detector.

Detects whether a folder contains an official
USGS Landsat Collection 2 product.
"""

from pathlib import Path


def is_landsat(path: str) -> bool:
    """
    Check whether a folder contains a Landsat product.

    Parameters
    ----------
    path : str
        Path to the folder.

    Returns
    -------
    bool
        True if the folder contains a Landsat
        Collection 2 product.
    """

    root = Path(path)

    if not root.exists():
        raise FileNotFoundError(path)

    for file in root.iterdir():

        if (
            file.is_file()
            and file.name.endswith("_MTL.txt")
        ):
            return True

    return False