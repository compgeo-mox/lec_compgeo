# Laboratory 2: Darcy Equation with PyGeoN

This lab focuses on the numerical solution of the Darcy equation using [PyGeoN](https://github.com/compgeo-mox/pygeon) and [PorePy](https://github.com/pmgbergen/porepy). The main focus is on the sequence of exercises (`ex1.ipynb` to `ex5.ipynb`), each addressing a different scenario for Darcy flow in 2D or 3D.

---

## Files Overview

- **ex1.ipynb**:  
  *Solves the basic Darcy problem on the unit square with constant permeability and a uniform source term, using homogeneous Dirichlet boundary conditions for the pressure.*

- **ex2.ipynb**:  
  *Introduces a vector source term (e.g., buoyancy), with mixed boundary conditions.*

- **ex3.ipynb**:  
  *Considers heterogeneous permeability and computes the effective permeability, comparing numerical and analytical results.*

- **ex4.ipynb**:  
  *Models two wells (sources/sinks) in the domain, requiring a constraint to ensure uniqueness of the pressure solution.*

- **ex5.ipynb**:  
  *Extends the problem to 3D with a more complex, piecewise-constant permeability tensor and mixed boundary conditions.*

---

## Main Exercise: ex1.ipynb

### Problem Statement

Let $\Omega = (0,1)^2$ with boundary $\partial \Omega$ and outward unit normal $\nu$.  
Given $k = I$ (identity matrix, i.e., isotropic permeability) and $f = 1$ (constant source), solve for $(q, p)$:

$$
\left\{
\begin{array}{ll}
\begin{array}{l} 
q + \nabla p = 0 \\
\nabla \cdot q = f
\end{array}
& \text{in } \Omega
\end{array}
\right.
$$

with boundary condition:

$$
p = 0 \quad \text{on } \partial \Omega
$$

### Step-by-step Solution

1. **Import modules**  
   Use `numpy`, `scipy.sparse`, `porepy`, and `pygeon`.

2. **Grid creation**  
   Use a triangular (simplicial) mesh for compatibility with the Raviart-Thomas (RT0) discretization.

3. **Problem setup**  
   - Define permeability tensor ($k=I$).
   - Define the constant source term ($f=1$).
   - Set up RT0 and piecewise constant (P0) spaces.

4. **Matrix assembly**  
   - Assemble the mass and divergence matrices.
   - Build the saddle-point system for the mixed formulation.

5. **Solve the linear system**  
   - Use PyGeoN's `LinearSystem` class.
   - Extract velocity ($q$) and pressure ($p$).

6. **Post-processing**  
   - Project $q$ to cell centers for visualization.
   - Export results to VTK for visualization in ParaView.

7. **Consistency check**  
   - Assert the norms of the computed pressure and velocity fields.

---

## How to Use

- Open each notebook (`ex1.ipynb`, ..., `ex5.ipynb`) in Jupyter.
- Run the cells sequentially to reproduce the results and visualizations.
- Use ParaView to inspect the exported `.vtu` files.

---

## Requirements

- Python 3.x
- Jupyter Notebook
- numpy, scipy
- porepy
- pygeon

---

## References

- [PyGeoN documentation](https://github.com/compgeo-mox/pygeon)
- [PorePy documentation](https://github.com/pmgbergen/porepy)
- [ParaView](https://www.paraview.org/)

---

*For questions or issues, please contact the course instructor or consult the documentation linked above.*