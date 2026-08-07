"""
Landsat product detector.
"""

from pathlib import Path

from .product import LandsatProduct


def detect_landsat(path: str):
    """
    Detect a Landsat Collection 2 product.
    """

    root = Path(path)

    if not root.exists():
        raise FileNotFoundError(path)

    filenames = {f.name for f in root.iterdir() if f.is_file()}

    if any(name.endswith("_MTL.txt") for name in filenames):

        return LandsatProduct(
            name="Landsat Collection 2",
            provider="USGS",
            confidence=100,
        )

    return None