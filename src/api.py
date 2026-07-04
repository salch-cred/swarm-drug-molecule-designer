from fastapi import FastAPI
from pydantic import BaseModel
from src.swarm_designer import AntMoleculeDesigner

app = FastAPI(title="Swarm Drug Molecule Designer API")
designer = AntMoleculeDesigner()

@app.post("/optimize")
def optimize():
    idx = designer.optimize_geometry()
    return {
        "optimal_atom_index": int(idx),
        "pheromones": designer.pheromones.tolist()
    }
