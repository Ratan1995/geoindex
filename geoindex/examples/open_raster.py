import geoindex as gi

img = gi.open(r"C:\Images\20240201.tif")

print(img)

red = img.read_band(3)

print("\nBand shape:", red.shape)
print("Data type :", red.dtype)
print("Minimum   :", red.min())
print("Maximum   :", red.max())