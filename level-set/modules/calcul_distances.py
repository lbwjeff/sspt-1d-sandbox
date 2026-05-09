"""
calcul_distances.py

Description:
--- ---
This module reproduces the the following MTC modules:
    CalculDistances
    GeometreVER= Phases (Voronoi)

The purpose of this module is to:
1. Define a simple two-site Voronoi geometry
2. Compute the Voronoi interface position
3. Compute the signed distances from each mesh node to the interface
4. Determine the belonging relationship ("Appartients" in the original MTC script) for each

For the current 1D case:
    site 0 | interface | site 1

For each mesh node, the signed distances are:
    dist_0 = x_interface - x
    dist_1 = x - x_interface

And the belonging relationship for each distance is:
    App_i = 1 if dist_i > -precision else 0 Voronoi cell


Workflow:
--- ---
Inputs:
    - Voronoi sites (x_left, x_right)
    - Node coordinates (coordinates)
    - Precision tolerance (precision)
Outputs:
    - Distances to the interface (distances)
    - Belonging relationships (appartients)
"""

from dataclasses import dataclass

import numpy as np


@dataclass
class VoronoiSites1D:
    """
    Simple 1D Voronoi geometry defined by two sites.
    """

    x_left: float
    x_right: float

    @property
    def interface_position(self) -> float:
        """
        Compute the Voronoi interface position.
        """

        return 0.5 * (self.x_left + self.x_right)


@dataclass
class CalculDistancesResult:
    """
    Storage container for the CalculDistances results.

    Parameters:
    --- ---
    distances: The two signed-distance fields for every mesh node
        Shape: (number_of_nodes, 2)

    appartients: Belonging relation field for every mesh node for the two signed-distance fields
        Shape: (number_of_nodes, 2)
        Value: 1.0 -> in the cell, 0.0 -> not in the cell

    interface_position: Position of the Voronoi interface
    """

    distances: np.ndarray
    appartients: np.ndarray
    interface_position: float


def calcul_distances_1d(
        coordinates: np.ndarray,
        sites: VoronoiSites1D,
        precision: float = 1e-7,
) -> CalculDistancesResult:
    """
    Reproduce the 1D version of CalculDistances.

    Parameters:
    --- ---
    coordinates: 1D array containing node positions
    sites: Voronoi geometry definition
    precision: Belonging tolerance used in the original solver
    App[i] = (dist[i] > -lprecision )
    
    Returns:
    --- ---
    CalculDistancesResult: a structure contaning
        signed distances
        beloninging relations
        interface position

    Notes:
    --- ---
    xI = (x_left + x_right) / 2
    dist0 = xI - x
    dist1 = x - xI
    """

    # Convert coordinates into a NumPy array
    x = np.asarray(coordinates, dtype=float)

    if x.ndim != 1:
        raise ValueError(
            "Coordinates must be a one-dimensional array of x positions." 
        )

    # Voronoi interface position
    x_interface = sites.interface_position

    # Signed distance array
    distances = np.empty((x.size, 2), dtype=float)
    distances[:, 0] = x_interface - x
    distances[:, 1] = x - x_interface

    # Beloning relation
    appartients = (distances > -precision).astype(float)

    return CalculDistancesResult(
        distances=distances,
        appartients=appartients,
        interface_position=x_interface,
    )


    
