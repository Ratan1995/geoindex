# GeoIndex

> A modern Python package for Earth Observation preprocessing, spectral indices, and time-series analysis.

---

## Overview

GeoIndex is an open-source Python package designed for remote sensing and GIS applications.

The goal of GeoIndex is to provide a simple and intuitive interface for working with satellite imagery from multiple sensors, including automatic sensor detection, intelligent band mapping, spectral indices, and time-series analysis.

The package is currently under active development.

---

## Features

Current features

- Open GeoTIFF images
- Read raster metadata
- Read all raster bands
- Read individual raster bands

Planned features

- Automatic sensor detection
- Automatic band mapping
- Spectral indices (NDVI, EVI, SAVI, MSAVI, NDWI, etc.)
- Time-series analysis
- Raster visualization
- Batch processing
- Cloud masking
- Vegetation phenology

---

## Installation

```bash
git clone https://github.com/Ratan1995/geoindex.git

cd geoindex

python -m pip install -e .
```

---

## Quick Start

```python
import geoindex as gi

img = gi.open(r"C:\Images\20240201.tif")

print(img)

data = img.read()

red = img.read_band(3)
```

---

## Current Output

```text
Raster(
  path='20240201.tif',
  size=5413 × 6007,
  bands=4,
  resolution=3.0 × 3.0,
  crs=EPSG:32631
)
```

---

## Project Structure

```
geoindex/
│
├── io/
├── indices/
├── sensors/
├── plotting/
└── utils/
```

---

## Roadmap

### Version 0.1

- Raster reader
- Raster metadata
- Read raster bands

### Version 0.2

- Automatic sensor detection
- Automatic band mapping

### Version 0.3

- Vegetation indices

### Version 0.4

- Time-series processing

### Version 1.0

- Complete Earth Observation toolkit

---

## Documentation

Documentation is under development.

---

## License

MIT License

---

## Author

Ratan Chandra Bhowmick
Master of Geography
Vrije Universiteit Brussel and KU Leuven
