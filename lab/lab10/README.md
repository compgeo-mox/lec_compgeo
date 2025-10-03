# Laboratory 10: Iterative Solvers for the Biot Equation

This lab explores iterative splitting methods for the (static) Biot equations in poroelasticity, using [PyGeoN](https://github.com/compgeo-mox/pygeon) and [PorePy](https://github.com/pmgbergen/porepy). The focus is on the fixed-strain and fixed-stress iterative solvers for the coupled displacement ($u$), Darcy flux ($q$), and pore pressure ($p$) system.

---

## Files Overview

- **ex1.ipynb**  
  *Fixed-strain iterative solver for the (one-step) Biot equation on a rectangular domain (footing problem). The method alternates between solving the flow and mechanics subproblems until convergence. The solution (displacement, flux, pressure, and stress tensor) is exported for visualization. The spectral radius of the iteration matrix is also computed.*

- **ex2.ipynb**  
  *Fixed-stress iterative solver for the (one-step) Biot equation on a rectangular domain (footing problem). The method introduces a stabilization parameter $\beta$ and alternates between flow and mechanics subproblems until convergence. The solution is exported, and the spectral radius of the iteration matrix is computed.*

---

## Main Features

- **Biot equations**:  
  $$
  \begin{aligned}
    &\nabla \cdot [2\mu \epsilon(u) + \lambda \nabla \cdot u\, I - \alpha p I] = -b \\\\
    &\mu q + K \nabla p = 0 \\\\
    &\partial_t (s_0 p + \alpha \nabla \cdot u) + \nabla \cdot q = \psi
  \end{aligned}
  $$
  where $\epsilon(u)$ is the symmetric gradient, $\lambda$ and $\mu$ are Lamé parameters, $K$ is permeability, $s_0$ is storativity, $\alpha$ is the Biot-Willis coefficient, $b$ is body force, and $\psi$ is a source term.

- **Iterative solvers**:  
  - **Fixed-strain splitting** (ex1): Alternates between flow and mechanics, holding strain fixed in the flow step.
  - **Fixed-stress splitting** (ex2): Alternates between flow and mechanics, holding stress fixed in the flow step and using a stabilization parameter $\beta$.
  - Both methods include convergence checks and compute the spectral radius of the iteration matrix.

- **Boundary conditions**:  
  - Dirichlet (displacement and/or pressure) and Neumann (traction and/or flux) conditions on various boundaries.
  - Footing problem: force applied on a central portion of the top boundary.

- **Numerical methods**:  
  - Mixed finite element discretization: VecLagrange1 for displacement, RT0 for flux, PwConstants for pressure.
  - Block-structured linear systems for coupled problems.

- **Post-processing**:  
  - Computation and export of stress tensor components, displacement, flux, and pressure.
  - Export of results for visualization in ParaView.

---

## How to Use

- Open each notebook (`ex1.ipynb`, `ex2.ipynb`) in Jupyter.
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
- [ParaView](https://www.paraview.org/)
- Standard texts on poroelasticity and iterative splitting methods

---

*For questions or issues, please contact the course instructor or consult the documentation linked above.*