# GeoIndex Metadata Engine

> **Status:** Draft (v1.0)  
> **Author:** Ratan Chandra Bhowmick  
> **Project:** GeoIndex

---

# Overview

The **GeoIndex Metadata Engine** is responsible for discovering, reading, interpreting, and standardizing metadata from Earth Observation products.

Different satellite providers distribute metadata in different formats. The Metadata Engine converts these heterogeneous metadata sources into a unified internal representation that can be used consistently throughout GeoIndex.

The Metadata Engine is the first component executed during the sensor identification process.

---

# Vision

GeoIndex should never depend on a single metadata format.

Instead, it should understand metadata from multiple satellite providers and expose a common interface for all downstream components.

The Metadata Engine hides provider-specific differences from users and other GeoIndex modules.

---

# Responsibilities

The Metadata Engine is responsible for:

- Discovering metadata files
- Reading multiple metadata formats
- Validating metadata
- Extracting sensor information
- Standardizing metadata
- Providing metadata to the Knowledge Engine

---

# Supported Metadata Sources

Current and future metadata sources include:

| Source | Status |
|---------|--------|
| XML | Planned |
| JSON | Planned |
| STAC | Planned |
| GeoTIFF Metadata | Planned |
| SAFE Metadata (Sentinel-2) | Planned |
| MTL Metadata (Landsat) | Planned |
| Future EO Products | Extensible |

---

# Metadata Discovery

When a folder is scanned, GeoIndex searches recursively for supported metadata.

Example:

```
Planet Product

├── image.tif
├── metadata.xml
├── metadata.json
├── catalog.json
└── collection.json
```

The Metadata Engine automatically detects available metadata without requiring manual user input.

---

# Standardization

Different providers use different field names.

The Metadata Engine converts them into a common internal structure.

Example:

```
Internal Metadata

Sensor

Platform

Instrument

Provider

Acquisition Time

Processing Level

Band Information

Spatial Resolution

CRS

Reflectance Scale

Product Type
```

Every downstream component works with this standardized representation.

---

# Metadata Priority

GeoIndex should always prefer richer metadata when multiple sources are available.

Priority order:

1. STAC
2. XML
3. JSON
4. GeoTIFF Metadata
5. Image Characteristics

This ensures that the highest-quality information is always used.

---

# Processing Workflow

```
Earth Observation Product
            │
            ▼
Metadata Discovery
            │
            ▼
Metadata Reader
            │
            ▼
Metadata Validation
            │
            ▼
Metadata Standardization
            │
            ▼
Knowledge Engine
```

---

# Integration with the Knowledge Engine

The Metadata Engine does not identify sensors.

Instead, it provides standardized metadata to the Knowledge Engine.

```
Metadata Engine
        │
        ▼
Knowledge Engine
        │
        ▼
Sensor Registry
        │
        ▼
Sensor Identification
```

Each component has a single responsibility.

---

# Error Handling

If metadata cannot be found:

```
Metadata unavailable

↓

Read GeoTIFF metadata

↓

Read image characteristics

↓

Pass available information to the Knowledge Engine
```

GeoIndex should continue operating whenever possible.

---

# Extensibility

Adding support for a new satellite mission should only require implementing a new metadata reader.

Example:

```
metadata/

stac.py

xml.py

json.py

sentinel.py

landsat.py

planet.py

modis.py
```

The rest of GeoIndex should remain unchanged.

---

# Design Principles

The Metadata Engine follows these principles.

1. Read metadata automatically.
2. Support multiple metadata standards.
3. Convert metadata into one internal format.
4. Never expose provider-specific complexity to users.
5. Continue gracefully when metadata is incomplete.
6. Be easily extensible for future satellite missions.

---

# Future Development

Planned improvements include:

- Automatic metadata validation
- Metadata caching
- Metadata version tracking
- Support for additional providers
- Cloud-native metadata
- Metadata quality assessment

---

# Long-Term Vision

The Metadata Engine should become a universal interpreter for Earth Observation metadata.

Instead of requiring users to understand different metadata standards, GeoIndex should provide a single, consistent interface regardless of the original satellite provider.

This component forms the foundation upon which the Knowledge Engine, Sensor Registry, and all future intelligent functionality are built.