"""
Generic Earth Observation Product.

Base class for all satellite products
supported by GeoIndex.
"""

from dataclasses import dataclass

from geoindex.core.metadata import Metadata


@dataclass
class Product:
    """
    Generic Earth Observation product.
    """

    name: str

    provider: str

    metadata: Metadata | None = None

    def __repr__(self) -> str:

        text = (
            "Product\n"
            "-------\n"
            f"Name     : {self.name}\n"
            f"Provider : {self.provider}\n"
        )

        if self.metadata is not None:

            text += "\n"
            text += str(self.metadata)

        return text