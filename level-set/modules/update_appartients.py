"""
update_appartients.py

Description:
--- ---
This module reproduces the following MTC modules
    MAJAppartients: 
        Appartients[i] = 1 if Distances[i] >= 0 else 0
"""

from modules.numerics import REAL_DTYPE

import numpy as np


def update_appartients_from_distances(
    distances: np.ndarray
    ) -> np.ndarray:
    """
    Convert signed distances into binary belonging indicators.

    Parameters:
    --- ---
    distances: signed distance field.
        Shape: (n_nodes, n_regions)

    Returns:
    --- ---
    np.ndarray: Binary belonging field.
        Values: in the region -> 1.0, else -> 0.0
    """

    return (distances >= REAL_DTYPE(0.0)).astype(REAL_DTYPE)
