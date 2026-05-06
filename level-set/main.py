from pathlib import Path

from modules.parameters import load_parameters
from modules.mesh import build_uniform_1d_mesh

def main() -> None:

    case_path = Path("./level-set/cases/simple_planar_interface.yaml")

    simulation_parameters = load_parameters(case_path)

    mesh = build_uniform_1d_mesh(simulation_parameters.mesh)

    print(mesh)
    print("Number of nodes:", len(mesh.nodes))
    print("Number of elements:", len(mesh.elements))
    print("Domain length:", mesh.length, "um")

if __name__ == "__main__":
    main()
