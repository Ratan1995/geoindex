"""
Scan result object for GeoIndex.

Stores information returned by the GeoIndex Scanner.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ScanResult:
    """
    Represents the result of a GeoIndex scan.

    Parameters
    ----------
    root : str
        Root directory scanned.
    folders : int
        Number of folders discovered.
    files : int
        Number of files discovered.
    tif_files : int
        Number of GeoTIFF files.
    xml_files : int
        Number of XML metadata files.
    json_files : int
        Number of JSON metadata files.
    elapsed_time : float
        Scan time in seconds.
    """

    root: str
    folders: int
    files: int
    tif_files: int
    xml_files: int
    json_files: int
    elapsed_time: float

    def __repr__(self) -> str:
        """Return a readable scan summary."""

        return (
            "GeoIndex Scan Summary\n"
            "=====================\n"
            f"Root Folder : {self.root}\n"
            f"Folders     : {self.folders}\n"
            f"Files       : {self.files}\n"
            f"GeoTIFF     : {self.tif_files}\n"
            f"XML         : {self.xml_files}\n"
            f"JSON        : {self.json_files}\n"
            f"Elapsed     : {self.elapsed_time:.2f} s"
        )