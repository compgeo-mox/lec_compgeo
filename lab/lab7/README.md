# Laboratory 7: Reactive Transport

This lab explores the numerical solution of reactive transport problems, focusing on chemical kinetics, equilibrium reactions, and coupled transport-reaction systems. The exercises use Python and standard scientific libraries (NumPy, SciPy, Matplotlib, PorePy).

---

## Files Overview

- **ex1.ipynb**  
  *Solves a system of chemical kinetics ODEs for four species ($A$, $B$, $C$, $D$) with three reactions (two reversible, one irreversible). The system is advanced in time using the explicit Euler method, and the evolution of all species is plotted.*

- **ex2.ipynb**  
  *Extends the previous chemical system by treating the first two reactions as being at equilibrium, reducing the ODE system to three total concentrations. At each time step, the actual species concentrations are recovered by solving a nonlinear algebraic system (using Newton's method). The explicit Euler method is used for time integration, and results are visualized.*

- **ex3.ipynb**  
  *Solves a coupled flow and reactive transport problem in a 2D domain. First, a Darcy flow problem is solved to obtain the advective velocity field. Then, a transport-reaction system is solved for a mobile species $c$ and an immobile species $w$, including precipitation/dissolution reactions. The system is advanced in time using operator splitting, and results are exported for visualization.*

---

## Main Features

- **Chemical kinetics and equilibrium**:  
  - ODE systems for multiple species and reactions.
  - Treatment of fast equilibrium reactions via algebraic constraints and Newton's method.

- **Reactive transport**:  
  - Coupling of advection and reaction in porous media.
  - Operator splitting for time integration of transport and nonlinear reactions.
  - Precipitation/dissolution modeled via nonlinear source terms.

- **Numerical methods**:  
  - Explicit Euler for time integration.
  - Newton's method for nonlinear algebraic systems.
  - Use of PorePy for grid generation, Darcy flow, and transport discretization.

- **Visualization**:  
  - Time evolution plots for species and total concentrations.
  - Export of spatially distributed results for ParaView.

---

## How to Use

- Open each notebook (`ex1.ipynb`, `ex2.ipynb`, `ex3.ipynb`) in Jupyter.
- Run the cells sequentially to reproduce the results and visualizations.
- Use ParaView to inspect the exported `.vtu` files from ex3.

---

## Requirements

- Python 3.x
- Jupyter Notebook
- numpy, scipy, matplotlib
- porepy

---

## References

- [PorePy documentation](https://github.com/pmgbergen/porepy)
- [ParaView](https://www.paraview.org/)
- Standard texts on chemical kinetics and reactive transport

---

*For questions or issues, please contact the course instructor or consult the documentation linked above.*