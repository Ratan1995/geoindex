"""
GeoIndex Scanner.

This module provides the scan() function, which searches
Earth Observation archives and summarizes their contents.

Author
------
Ratan Chandra Bhowmick

Project
-------
GeoIndex
"""

from __future__ import annotations

from pathlib import Path
from time import perf_counter

from .result import ScanResult


def scan(path: str) -> ScanResult:
    """
    Scan an Earth Observation archive.

    Parameters
    ----------
    path : str
        Path to the root directory.

    Returns
    -------
    ScanResult
        Summary of the scan.
    """

    root = Path(path)

    if not root.exists():
        raise FileNotFoundError(f"Folder not found: {path}")

    start = perf_counter()

    folders = 0
    files = 0

    tif_files = 0
    xml_files = 0
    json_files = 0

    for item in root.rglob("*"):

        if item.is_dir():
            folders += 1

        elif item.is_file():

            files += 1

            suffix = item.suffix.lower()

            if suffix in (".tif", ".tiff"):
                tif_files += 1

            elif suffix == ".xml":
                xml_files += 1

            elif suffix == ".json":
                json_files += 1

    elapsed = perf_counter() - start

    return ScanResult(
        root=str(root),
        folders=folders,
        files=files,
        tif_files=tif_files,
        xml_files=xml_files,
        json_files=json_files,
        elapsed_time=elapsed,
    )