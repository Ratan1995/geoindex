"""
GeoIndex
========

A Python package for intelligent Earth Observation analysis.

Author
------
Ratan Chandra Bhowmick
"""

from .io import open
from .core.scanner import scan

__version__ = "0.1.0"

__all__ = [
    "open",
    "scan",
]