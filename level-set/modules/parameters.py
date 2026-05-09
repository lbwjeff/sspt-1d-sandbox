from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class MeshParameters:
    nx: int # Number of finite element
    dx: float # Size of finite element


@dataclass
class InterfaceParameters:
    sites: list[float] # Voronoi site positions to generate the interface
    precision: float # Beloning precision for distance calculation
    eta: float # Diffuse interface width


@dataclass
class SimulationParameters:
    mesh: MeshParameters
    interface: InterfaceParameters


def load_parameters(yaml_path: str | Path)-> SimulationParameters:
    """
    Load simulation parameters from a yaml file.
    """

    yaml_path = Path(yaml_path)

    with open(yaml_path, "r", encoding="utf-8") as file:
        raw_parameters = yaml.safe_load(file)

    mesh = MeshParameters(**raw_parameters["mesh"])
    interface = InterfaceParameters(**raw_parameters["interface"])

    simulation_parameters = SimulationParameters(
            mesh=mesh,
            interface=interface,
            )

    return simulation_parameters 
