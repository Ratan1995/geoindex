"""
Landsat product detector.

Detects whether a folder contains an official
USGS Landsat Collection 2 product.
"""

from pathlib import Path

from .product import LandsatProduct
from .metadata import read_mtl


def detect_landsat(path: str) -> LandsatProduct | None:
    """
    Detect a Landsat Collection 2 product.

    Parameters
    ----------
    path : str
        Path to the Landsat product folder.

    Returns
    -------
    LandsatProduct or None
        A LandsatProduct object if detected,
        otherwise None.
    """

    root = Path(path)

    if not root.exists():
        raise FileNotFoundError(path)

    filenames = {f.name for f in root.iterdir() if f.is_file()}

    if any(name.endswith("_MTL.txt") for name in filenames):

        metadata = read_mtl(path)

        return LandsatProduct(
            name="Landsat Collection 2",
            provider="USGS",
            confidence=100,
            metadata=metadata,
        )

    return None