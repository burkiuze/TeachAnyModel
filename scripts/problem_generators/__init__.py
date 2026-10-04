"""Synthetic, verifiable science problem generators.

Importing this package registers every template in :data:`REGISTRY`.
Each template produces fresh numbers from a seeded ``random.Random`` so the
output is fully reproducible.
"""

from .common import REGISTRY, build  # noqa: F401
from . import astronomy, biology, chemistry, mathematics, physics  # noqa: F401

__all__ = ["REGISTRY", "build"]
