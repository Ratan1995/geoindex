# GeoIndex Architecture

> **Status:** Draft (v1.0)  
> **Author:** Ratan Chandra Bhowmick  
> **Project:** GeoIndex

---

# Overview

GeoIndex is an intelligent Earth Observation framework designed to understand satellite imagery rather than simply process raster files.

Unlike traditional geospatial libraries that focus on raster operations, GeoIndex combines metadata, sensor knowledge, and Earth Observation expertise to provide a unified and sensor-independent interface for satellite analysis.

GeoIndex is built upon mature open-source libraries such as Rasterio instead of replacing them. Its objective is to provide higher-level intelligence while relying on proven geospatial software for low-level raster operations.

---

# Architecture

```
                    User
                      │
                      ▼
      ┌──────────────────────────────────┐
      │                                  │
      │        GeoIndex API              │
      │                                  │
      └──────────────────────────────────┘
                      │
                      ▼
            gi.open() / gi.scan()
                      │
          ┌───────────┴────────────┐
          ▼                        ▼
 Metadata Engine          Knowledge Engine
          │                        │
          ▼                        ▼
 Metadata Parser          Sensor Registry
          │                        │
          └──────────┬─────────────┘
                     ▼
            Signature Matcher
                     │
                     ▼
            Confidence Engine
                     │
                     ▼
            Explanation Engine
                     │
                     ▼
              Sensor Object
                     │
          ┌──────────┼───────────┐
          ▼          ▼           ▼
    Band Mapping   Indices   Time Series
          │          │           │
          └──────────┴───────────┘
                     ▼
               User Results
```

---

# Major Components

## GeoIndex API

The public interface used by end users.

Examples:

```python
import geoindex as gi

gi.scan("D:/SatelliteData")

img = gi.open("image.tif")
```

The API should remain simple while hiding internal complexity.

---

## Metadata Engine

Responsibilities:

- Discover metadata
- Read XML
- Read JSON
- Read STAC
- Read GeoTIFF metadata
- Standardize metadata

The Metadata Engine provides structured information to the Knowledge Engine.

---

## Knowledge Engine

The intelligence layer of GeoIndex.

Responsibilities:

- Understand Earth Observation products
- Combine metadata
- Use sensor knowledge
- Perform sensor identification
- Support future analyses

---

## Sensor Registry

Stores reusable sensor knowledge.

The registry contains:

- Sensor definitions
- Instrument information
- Band definitions
- Typical metadata
- Resolution
- Product characteristics

The registry does not store individual images.

---

## Signature Matcher

Compares available information with known sensor signatures.

Possible inputs include:

- Metadata
- GeoTIFF tags
- Band count
- Spatial resolution
- CRS
- Wavelengths
- Band descriptions

The best matching sensor is selected.

---

## Confidence Engine

Evaluates the confidence of every automatic decision.

GeoIndex should never hide uncertainty.

Every sensor identification should include a confidence estimate.

---

## Explanation Engine

Provides transparent explanations.

Example:

```
PlanetScope SuperDove

Confidence

98%

Evidence

✓ Official metadata

✓ Instrument PSB.SD

✓ Four-band configuration

✓ Sensor Registry match
```

Every automatic decision should be reproducible.

---

# Detection Strategy

GeoIndex follows a layered strategy.

Priority:

1. Metadata
2. Embedded GeoTIFF metadata
3. Official Sensor Registry
4. User Sensor Registry
5. Image characteristics
6. Intelligent inference
7. User input

---

# Development Philosophy

GeoIndex follows five architectural principles.

## 1. Build upon existing libraries

Rasterio, GDAL and similar projects already solve raster I/O extremely well.

GeoIndex should extend them instead of replacing them.

---

## 2. Metadata before inference

Whenever metadata exists, it should always be preferred over heuristic methods.

---

## 3. Explain every decision

Users should understand how GeoIndex reached every conclusion.

---

## 4. Learn reusable knowledge

GeoIndex should build reusable sensor knowledge instead of memorizing files.

---

## 5. Keep the API simple

The user experience should remain intuitive.

Example:

```python
img = gi.open("image.tif")

img.ndvi()
```

Complexity belongs inside GeoIndex, not in user code.

---

# Long-Term Vision

GeoIndex should become an intelligent Earth Observation framework capable of understanding satellite products across multiple missions.

Future modules include:

- Sensor Registry
- Knowledge Engine
- Metadata Engine
- Automatic Band Mapping
- Spectral Indices
- Time-Series Analysis
- Phenology
- Change Detection
- Machine Learning Utilities

All components should work together through a unified architecture.

---

# Philosophy Statement

GeoIndex is not designed to replace existing geospatial libraries.

Instead, GeoIndex builds upon proven open-source software and adds intelligent Earth Observation capabilities through metadata interpretation, sensor understanding, and reusable knowledge.

The ultimate objective is to create software that understands Earth Observation products rather than simply processing raster files.