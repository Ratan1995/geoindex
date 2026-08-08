from geoindex.core.metadata import Metadata
from geoindex.core.product import Product

meta = Metadata(
    spacecraft="LANDSAT_9",
    sensor="OLI_TIRS",
    provider="USGS",
    acquisition_date="2025-02-04",
)

product = Product(
    name="Example Product",
    provider="USGS",
    metadata=meta,
)

print(product)