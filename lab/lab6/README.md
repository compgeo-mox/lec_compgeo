# Laboratory 6: Darcy Equation in Fractured Domains

This lab addresses the numerical solution of the Darcy equation in fractured porous media using the mixed-dimensional approach with [PyGeoN](https://github.com/compgeo-mox/pygeon) and [PorePy](https://github.com/pmgbergen/porepy). Fractures are represented as lower-dimensional objects embedded in the matrix, and the coupling between matrix and fractures is handled automatically.

---

## Files Overview

- **ex1.ipynb**  
  *Solves the Darcy equation in a unit square domain with a single fracture. The fracture is represented as a 1D object embedded in the 2D matrix. The mixed-dimensional grid is constructed, and the problem is solved for both highly and low-permeable fractures. The solution (pressure and velocity) is exported for visualization.*

- **ex2.ipynb**  
  *Extends the previous setup to two intersecting fractures. The mixed-dimensional grid is built for the network, and the Darcy problem is solved with appropriate coupling conditions between matrix and fractures. The solution is exported for visualization.*

- **ex3.ipynb**  
  *Solves the Darcy equation for a realistic fracture network from a published benchmark (case 4). The fracture geometry is imported from file, the mixed-dimensional grid is generated, and the problem is solved with high contrast between matrix and fracture permeabilities. The results are exported for visualization.*

---

## Main Features

- **Mixed-dimensional modeling**:  
  Fractures are modeled as lower-dimensional grids (1D in 2D, 2D in 3D) coupled to the surrounding matrix.

- **Grid generation**:  
  Mixed-dimensional grids are created from fracture networks, either defined in code or imported from file.

- **Physical parameters**:  
  - Matrix and fracture permeabilities can be set independently.
  - Fracture aperture and normal permeability are specified for realistic coupling.

- **Boundary and coupling conditions**:  
  - Dirichlet and Neumann boundary conditions on the matrix and fractures.
  - Automatic coupling between matrix and fractures via interface conditions.

- **Linear system assembly**:  
  - The global saddle-point problem is assembled and solved.
  - Post-processing projects velocity and pressure to cell centers for visualization.

- **Visualization**:  
  - Results are exported in `.vtu` format for analysis in ParaView.

---

## How to Use

- Open each notebook (`ex1.ipynb`, `ex2.ipynb`, `ex3.ipynb`) in Jupyter.
- Run the cells sequentially to reproduce the results and visualizations.
- Use ParaView to inspect the exported `.vtu` files.

---

## Requirements

- Python 3.x
- Jupyter Notebook
- numpy, scipy, matplotlib
- porepy
- pygeon

---

## References

- [PyGeoN documentation](https://github.com/compgeo-mox/pygeon)
- [PorePy documentation](https://github.com/pmgbergen/porepy)
- Berre, I., et al. (2017). "Flow in fractured porous media: A review of conceptual models and discretization approaches." Advances in Water Resources, 47, 3-17. [Link](https://www.sciencedirect.com/science/article/pii/S0309170817300143)
- [ParaView](https://www.paraview.org/)

---

*For questions or issues, please contact the course instructor or consult the documentation linked above.*