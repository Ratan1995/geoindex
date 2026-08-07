from geoindex.providers.landsat import detect_landsat

folder = r"C:\GeoIndex_TestData\Landsat9"

product = detect_landsat(folder)

print(product)