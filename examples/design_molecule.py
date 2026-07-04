from src.swarm_designer import AntMoleculeDesigner

designer = AntMoleculeDesigner()
optimal_atom_index = designer.optimize_geometry()
print("Optimized bonding atomic index identified:", optimal_atom_index)
