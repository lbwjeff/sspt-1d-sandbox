from pathlib import Path

from modules.parameters import load_parameters

def main() -> None:

    case_path = Path("./level-set/cases/simple_planar_interface.yaml")

    simulation_parameters = load_parameters(case_path)

    print(simulation_parameters.mesh)

if __name__ == "__main__":
    main()
