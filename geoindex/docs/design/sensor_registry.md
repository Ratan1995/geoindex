> ⚠️ This document defines the architectural vision of the GeoIndex Sensor Registry. Code implementations should follow the principles described here unless there is a strong technical reason to revise them.
# GeoIndex Sensor Registry

> **Status:** Draft (v1.0)  
> **Author:** Ratan Chandra Bhowmick  
> **Project:** GeoIndex

---

# Overview

The **GeoIndex Sensor Registry** is the core intelligence system of GeoIndex.

Unlike traditional remote sensing libraries that only process raster files, GeoIndex is designed to **understand Earth Observation datasets**.

The Sensor Registry builds a persistent knowledge base by scanning Earth Observation archives and learning the characteristics of different satellite sensors.

Once a sensor has been identified from complete metadata, GeoIndex can use this knowledge to help identify future images, even when only a GeoTIFF is available.

---

# Motivation

In a typical remote sensing workflow, researchers download complete satellite products containing:

- GeoTIFF images
- XML metadata
- JSON metadata
- STAC metadata
- Quality masks
- Other auxiliary files

However, after preprocessing, users often keep **only the GeoTIFF**, while deleting the metadata files.

For example:

```
Download Product
        │
        ▼
Preprocess
        │
        ▼
Clip
Reproject
Mask
Stack
Rename
        │
        ▼
20240201.tif
```

At this stage, valuable metadata describing the satellite sensor has been lost.

GeoIndex solves this problem by allowing users to scan their satellite archive **before preprocessing**, creating a reusable Sensor Registry that can later assist with sensor identification.

---

# Design Philosophy

GeoIndex should **understand satellite imagery**, not simply process raster files.

The package should use every available source of information before asking the user.

---

# Sensor Detection Workflow

```
               First Time
                     │
                     ▼
      gi.scan("D:/SatelliteData")
                     │
                     ▼
      Scan all Earth Observation products
                     │
                     ▼
      Read metadata (XML / JSON / STAC)
                     │
                     ▼
      Build Sensor Registry
                     │
                     ▼
      Save Local Knowledge Base

──────────────────────────────────────────────

             Future Sessions
                     │
                     ▼
         gi.open("unknown.tif")
                     │
                     ▼
      Search Sensor Registry
                     │
                     ▼
      Match Sensor Signature
                     │
                     ▼
      Confidence Evaluation
                     │
                     ▼
      Return Sensor Information
```

---

# Example Workflow

```python
import geoindex as gi

# One-time setup (recommended)
gi.scan("D:/SatelliteData")

# Everyday use
img = gi.open("20240201.tif")

print(img.sensor)
```

Expected output:

```
PlanetScope SuperDove

Confidence : 98%

Source : Sensor Registry
```

---

# GeoIndex Scan

Example output:

```
Scanning D:/SatelliteData...

------------------------------------------------
PlanetScope SuperDove
------------------------------------------------
✓ Products discovered      : 325
✓ Metadata files           : XML + STAC
✓ Sensor identified        : PSB.SD
✓ Registry updated

------------------------------------------------
Sentinel-2 MSI
------------------------------------------------
✓ Products discovered      : 182
✓ Metadata files           : SAFE
✓ Registry updated

------------------------------------------------
Landsat 9 OLI-2
------------------------------------------------
✓ Products discovered      : 54
✓ Metadata files           : MTL
✓ Registry updated

------------------------------------------------
Summary
------------------------------------------------
Sensors learned : 3
Products scanned: 561

Sensor Registry successfully updated.
```

---

# Detection Priority

GeoIndex should identify sensors using the following order of confidence.

| Priority | Source | Confidence |
|----------|---------|------------|
| 1 | XML / STAC / JSON Metadata | ⭐⭐⭐⭐⭐ |
| 2 | Embedded GeoTIFF Metadata | ⭐⭐⭐⭐☆ |
| 3 | Official Sensor Registry | ⭐⭐⭐⭐☆ |
| 4 | User Sensor Registry | ⭐⭐⭐⭐☆ |
| 5 | Image Characteristics | ⭐⭐⭐☆☆ |
| 6 | Filename Pattern | ⭐⭐☆☆☆ |
| 7 | User Input | Manual |

---

# Sensor Registry

The registry should store reusable sensor knowledge rather than information about individual images.

Example:

```
PlanetScope SuperDove

Instrument
PSB.SD

Bands
Blue
Green
Red
Near Infrared

Spatial Resolution
3 m

Reflectance Scaling

Provider
Planet Labs

Typical Metadata Signatures

Supported Products
```

---

# Design Principles

GeoIndex follows six fundamental principles.

1. Metadata first.
2. GeoTIFF metadata second.
3. Registry-based identification.
4. Intelligent inference.
5. User input when necessary.
6. Never fabricate information.

---

# Long-Term Vision

GeoIndex should become an intelligent Earth Observation framework.

Instead of asking users to provide sensor information repeatedly, GeoIndex should build knowledge from previous datasets and reuse that knowledge throughout future analyses.

The objective is to create software that understands Earth Observation products rather than simply reading raster files.

---

# Future Development

- Metadata Engine
- Sensor Registry
- Knowledge Engine
- Confidence Engine
- Automatic Band Mapping
- Sensor-independent Vegetation Indices
- Multi-sensor Earth Observation Workflows

---

# Notes

This document describes the architectural vision for the GeoIndex Sensor Registry.

Implementation details may evolve, but the overall philosophy should remain consistent throughout the development of GeoIndex.