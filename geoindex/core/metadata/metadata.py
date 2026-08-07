"""
Generic Earth Observation metadata.

This class represents metadata that is common
across all supported satellite products.
"""

from dataclasses import dataclass


@dataclass
class Metadata:
    """
    Generic metadata object.
    """

    spacecraft: str | None = None
    sensor: str | None = None
    provider: str | None = None
    acquisition_date: str | None = None
    processing_level: str | None = None
    collection: str | None = None
    crs: str | None = None
    resolution: float | None = None

    def __repr__(self) -> str:
        return (
            "Metadata\n"
            "--------\n"
            f"Spacecraft       : {self.spacecraft}\n"
            f"Sensor           : {self.sensor}\n"
            f"Provider         : {self.provider}\n"
            f"Acquisition Date : {self.acquisition_date}\n"
            f"Processing Level : {self.processing_level}\n"
            f"Collection       : {self.collection}\n"
            f"CRS              : {self.crs}\n"
            f"Resolution       : {self.resolution}"
        )