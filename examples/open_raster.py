import geoindex as gi

img = gi.open(r"C:\Images\20240201.tif")

print(img)

data = img.read()

print("\nArray shape:", data.shape)
print("Data type:", data.dtype)