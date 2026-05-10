from pathlib import Path
import numpy as np

from modules.parameters import load_parameters
from modules.mesh import build_uniform_1d_mesh
from modules.calcul_distances import VoronoiSites1D, calcul_distances_1d
from modules.update_appartients import update_appartients_from_distances
from modules.numerics import PRINT_PRECISION, CIMLIB_DELIMITER, CIMLIB_OUTPUT_FORMAT, DEBUG_OUTPUT_FORMAT

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

    # Update Appartients
    updated_appartients = update_appartients_from_distances(
        result.distances
    )

    print("Interface position:", result.interface_position, "um")

    table = np.column_stack(
        [
            mesh.nodes,
            result.distances[:, 0],
            result.distances[:, 1],
            updated_appartients[:, 0],
            updated_appartients[:, 1],
        ]        
    )

    np.set_printoptions(precision=PRINT_PRECISION, suppress=False)
    print("\n[x, dist0, dist1, App0, App1]")
    print(table)

    # CimLib-line output
    np.savetxt(
        "level-set/results/distances_appartients.csv",
        table,
        delimiter=CIMLIB_DELIMITER,
        header="x\tdist0\tdist1\tapp0\tapp1",
        comments="",
        fmt=CIMLIB_OUTPUT_FORMAT,
    )

    # High precision reference output
    np.savetxt(
        "level-set/results/distances_appartients_debug.csv",
        table,
        delimiter=",",
        header="x,dist0,dist1,app0,app1",
        comments="",
        fmt=DEBUG_OUTPUT_FORMAT,
    )

if __name__ == "__main__":
    main()
