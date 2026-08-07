"""
Landsat Product object.

Represents an official Landsat product.
"""

from dataclasses import dataclass


@dataclass
class LandsatProduct:
    """
    Landsat product information.
    """

    name: str
    provider: str
    confidence: int

    def __repr__(self) -> str:
        return (
            "Landsat Product\n"
            "----------------\n"
            f"Name       : {self.name}\n"
            f"Provider   : {self.provider}\n"
            f"Confidence : {self.confidence}%"
        )