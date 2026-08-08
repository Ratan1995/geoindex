"""
Raster reader for GeoIndex.

This module provides functionality for opening raster datasets
and returning a GeoIndex Raster object.
"""

from __future__ import annotations

# Standard library
from pathlib import Path

# Third-party
import rasterio

# Local
from .raster import Raster


def open(path: str | Path) -> Raster:
    """
    Open a raster dataset.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to the raster file.

    Returns
    -------
    Raster
        A GeoIndex Raster object.
    """

    dataset = rasterio.open(path)

    return Raster(dataset)