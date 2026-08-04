"""
Raster object for GeoIndex.

This module defines the Raster class, which stores the metadata
associated with an opened raster dataset.

The Raster class is the core object in GeoIndex and provides the
foundation for future functionality such as sensor detection,
spectral indices, visualization, and time-series analysis.
"""

from __future__ import annotations

# Standard library
from pathlib import Path

# Third-party
from rasterio.io import DatasetReader


class Raster:
    """
    Represents an opened raster dataset.

    The Raster class stores the essential metadata describing a
    raster image while keeping the underlying Rasterio dataset
    internally available for future processing.

    Parameters
    ----------
    dataset : DatasetReader
        An opened Rasterio dataset.
    """

    def __init__(self, dataset: DatasetReader) -> None:
        """Initialize a Raster object."""

        # Store the original Rasterio dataset (internal use only)
        self._dataset: DatasetReader = dataset

        # File information
        self.path: Path = Path(dataset.name)

        # Raster dimensions
        self.width: int = dataset.width
        self.height: int = dataset.height
        self.count: int = dataset.count

        # Spatial metadata
        self.crs = dataset.crs
        self.transform = dataset.transform
        self.bounds = dataset.bounds
        self.resolution = dataset.res

        # Data information
        self.dtype: str = dataset.dtypes[0]

    def __repr__(self) -> str:
        """Return a readable representation of the raster."""

        return (
            "Raster(\n"
            f"  path='{self.path.name}',\n"
            f"  size={self.width} × {self.height},\n"
            f"  bands={self.count},\n"
            f"  resolution={self.resolution[0]} × {self.resolution[1]},\n"
            f"  crs={self.crs}\n"
            ")"
        )
    def info(self) -> str:
        """Return a formatted summary of the raster metadata."""

        return (
            "=========================================\n"
            "GeoIndex Raster Information\n"
            "=========================================\n\n"
            "File\n"
            "-------------------------\n"
            f"Name        : {self.path.name}\n"
            f"Path        : {self.path}\n\n"
            "Dimensions\n"
            "-------------------------\n"
            f"Width       : {self.width} pixels\n"
            f"Height      : {self.height} pixels\n"
            f"Bands       : {self.count}\n"
            f"Resolution  : {self.resolution[0]} × {self.resolution[1]} m\n\n"
            "Spatial Reference\n"
            "-------------------------\n"
            f"CRS         : {self.crs}\n"
            f"Bounds      : {self.bounds}\n\n"
            "Data\n"
            "-------------------------\n"
            f"Data Type   : {self.dtype}\n"
            "========================================="
        )
    def read(self):
        """
        Read all raster bands.

        Returns
        -------
        numpy.ndarray
            Raster values with shape (bands, rows, columns).
        """

        return self._dataset.read()