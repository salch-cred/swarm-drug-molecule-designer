# Swarm Drug Molecule Designer

A generative algorithm utilizing multi-agent Ant Colony Optimization (ACO) algorithms to discover viable 3D atomic structures for drug molecules.

## Usage
```bash
python examples/design_molecule.py
```


## FastAPI API Service
The project includes a FastAPI server wrapper. 

### Running the API
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000
```
- **Interactive docs**: Navigate to `/docs` for swagger documentation.
- **POST `/optimize`**: Seek configuration structures using ACO optimization.
