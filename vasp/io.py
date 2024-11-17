import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem


def read_molecules_from_file(filename) -> list:
    """
    Read molecules from a file (.sdf) and return a list of preprocessed molecules.
    """
    if filename.endswith(".sdf"):
        return read_molecules_from_sdf(filename)
    else:
        raise ValueError(f"Unsupported file format: {filename}")


def read_molecules_from_sdf(filename) -> list:
    """
    Read molecules from a .sdf file and return a list of preprocessed molecules.
    """
    molecules = Chem.SDMolSupplier(filename)
    return [preprocess_molecule(mol) for mol in molecules if mol is not None]


def preprocess_molecule(molecule) -> rdkit.Chem.Mol:
    """
    Preprocess a molecule and returns a molecule object.
    """
    molecule = Chem.AddHs(molecule)
    AllChem.EmbedMolecule(molecule)
    AllChem.MMFFOptimizeMolecule(molecule)
    return molecule


def write_molecule_to_sdf(molecule, filename):
    """
    Write a molecule to a .sdf file.
    """
    writer = Chem.SDWriter(filename)
    writer.write(molecule)
    writer.close()
