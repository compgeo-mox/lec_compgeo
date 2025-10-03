# Laboratory 3: Finite Volume Methods for the Darcy Equation

This lab explores the solution of the Darcy equation using finite volume methods with [PorePy](https://github.com/pmgbergen/porepy) and [PyGeoN](https://github.com/compgeo-mox/pygeon). The focus is on comparing the two-point flux approximation (TPFA) and multi-point flux approximation (MPFA) schemes on various grids and permeability fields.

---

## Files Overview

- **ex1.ipynb**  
  *Compares TPFA and MPFA for the Darcy problem on different grid types (Cartesian, simplex, Voronoi, octagonal) with constant permeability and a uniform source term on the unit square. Computes and compares the $L^2$-difference between the two solutions and exports results for visualization.*

- **ex2.ipynb**  
  *Studies the effect of grid distortion (shear transformation) on the difference between TPFA and MPFA. The domain is a sheared unit square, and the discrepancy between the two methods is analyzed as the shear angle increases. Both pressure and fluxes are exported for visualization.*

- **ex3.ipynb**  
  *Solves the Darcy problem on a realistic heterogeneous permeability field from the SPE10 benchmark. The domain and permeability are imported from the benchmark, and Dirichlet/Neumann boundary conditions are imposed. The TPFA scheme is used, and both pressure and fluxes are exported for visualization.*

---

## Main Exercise: ex1.ipynb

### Problem Statement

Let $\Omega = [0,1]^2$ with boundary $\partial \Omega$ and outward unit normal $\nu$.  
Given $k = I$ (isotropic permeability) and $f = 1$ (constant source), solve for $p$:

$$
\nabla \cdot (-\nabla p) = f \quad \text{in } \Omega
$$

with boundary condition:

$$
p = 0 \quad \text{on } \partial \Omega
$$

### Step-by-step Solution

1. **Import modules**  
   Use `numpy`, `porepy`, and `pygeon`.

2. **Grid creation**  
   Try different grid types: Cartesian, simplex, Voronoi, octagonal.

3. **Problem setup**  
   - Define permeability tensor ($k=I$).
   - Set Dirichlet boundary conditions.
   - Set up the scalar source term ($f=1$).

4. **Matrix assembly**  
   - Assemble the system matrix and right-hand side for both TPFA and MPFA schemes.

5. **Solve the linear systems**  
   - Compute the pressure field with both TPFA and MPFA.

6. **Comparison**  
   - Compute the $L^2$-norm of the difference between the two solutions.

7. **Post-processing**  
   - Export the solutions for visualization in ParaView.

---

## How to Use

- Open each notebook (`ex1.ipynb`, `ex2.ipynb`, `ex3.ipynb`) in Jupyter.
- Run the cells sequentially to reproduce the results and visualizations.
- Use ParaView to inspect the exported `.vtu` files.

---

## Requirements

- Python 3.x
- Jupyter Notebook
- numpy
- porepy
- pygeon

---

## References

- [PorePy documentation](https://github.com/pmgbergen/porepy)
- [PyGeoN documentation](https://github.com/compgeo-mox/pygeon)
- [SPE10 Benchmark](http://dx.doi.org/10.2118/66599-MS)
- [ParaView](https://www.paraview.org/)

---

*For questions or issues, please contact the course instructor or consult the documentation linked above.*