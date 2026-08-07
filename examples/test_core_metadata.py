from geoindex.core.metadata import Metadata

meta = Metadata(
    spacecraft="LANDSAT_9",
    sensor="OLI_TIRS",
    provider="USGS",
    acquisition_date="2025-02-04",
    processing_level="Level-2",
    collection="02",
)

print(meta)