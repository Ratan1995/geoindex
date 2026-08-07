from geoindex.providers.landsat.metadata import read_mtl

folder = r"C:\GeoIndex_TestData\Landsat9"

metadata = read_mtl(folder)

print(metadata["SPACECRAFT_ID"])
print(metadata["SENSOR_ID"])
print(metadata["DATE_ACQUIRED"])
print(metadata["COLLECTION_NUMBER"])