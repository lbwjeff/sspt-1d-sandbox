from pathlib import Path
import numpy as np

from modules.parameters import load_parameters
from modules.mesh import build_uniform_1d_mesh
from modules.calcul_distances import VoronoiSites1D, calcul_distances_1d

def main() -> None:

    case_path = Path("./level-set/cases/simple_planar_interface.yaml")

    simulation_parameters = load_parameters(case_path)

    # Build mesh
    mesh = build_uniform_1d_mesh(simulation_parameters.mesh)

    print(mesh)
    print("Number of nodes:", len(mesh.nodes))
    print("Number of elements:", len(mesh.elements))
    print("Domain length:", mesh.length, "um")

    # Generate distance field and belongin field from the two voronoi sites
    site_left, site_right = simulation_parameters.interface.sites
    precision = simulation_parameters.interface.precision

    phases = VoronoiSites1D(
        x_left=site_left,
        x_right=site_right,
    )

    result = calcul_distances_1d(
        coordinates=mesh.nodes,
        sites=phases,
        precision=precision,
    )

    print("Interface position:", result.interface_position, "um")

    table = np.column_stack(
        [
            mesh.nodes,
            result.distances[:, 0],
            result.distances[:, 1],
            result.appartients[:, 0],
            result.appartients[:, 1],
        ]        
    )

    np.set_printoptions(precision=8, suppress=True)
    print("\n[x, dist0, dist1, App0, App1]")
    print(table)

if __name__ == "__main__":
    main()
