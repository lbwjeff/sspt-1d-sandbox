# modules/mesh.py

from dataclasses import dataclass

import numpy as np

from modules.parameters import MeshParameters
from modules.numerics import REAL_DTYPE, INT_DTYPE


@dataclass
class Mesh1D:
    nodes: np.ndarray # Finite element nodes
    elements: np.ndarray # Finite elements identified by the nodes
    centers: np.ndarray # Center of every element (for P0 value)
    dx: float # Finite element size
    length: float # Length of the domain
    nx: int # Number of elements

def build_uniform_1d_mesh(mesh_params: MeshParameters) -> Mesh1D:
    """
    Build a uniform 1D finite element mesh.

    nx is the number of elements.
    The number of nodes is therefore nx + 1
    """

    nx = int(mesh_params.nx)
    dx = REAL_DTYPE(mesh_params.dx)

    length = REAL_DTYPE(nx) * dx

    nodes = np.linspace(
            REAL_DTYPE(0.0), 
            length, 
            nx + 1,
            dtype=REAL_DTYPE
    )

    # Finite element connectivity
    # Node indeces for each element
    elements = np.column_stack(
        [
            np.arange(0, nx, dtype=INT_DTYPE),
            np.arange(1, nx + 1, dtype=INT_DTYPE),
        ]
    )

    # Element center
    centers = REAL_DTYPE(0.5) * (nodes[:-1] + nodes[1:])

    return Mesh1D(
        nodes=nodes,
        elements=elements,
        centers=centers,
        dx=dx,
        length=length,
        nx=nx,
    )


