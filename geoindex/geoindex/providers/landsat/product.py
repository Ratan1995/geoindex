"""
Landsat Product object.
"""

from dataclasses import dataclass

from geoindex.core.metadata import Metadata


@dataclass
class LandsatProduct:
    """
    Represents a Landsat product.
    """

    name: str

    provider: str

    confidence: int

    metadata: Metadata | None = None

    def __repr__(self) -> str:

        text = (
            "Landsat Product\n"
            "----------------\n"
            f"Name       : {self.name}\n"
            f"Provider   : {self.provider}\n"
            f"Confidence : {self.confidence}%\n"
        )

        if self.metadata is not None:

            text += "\n"
            text += str(self.metadata)

        return text