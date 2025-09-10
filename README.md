[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# NUMERICAL METHODS FOR THE GEOSCIENCES

## Course Overview

This course introduces mathematical and numerical modeling for simulating physical processes in the geosciences, with a focus on subsurface flow and deformation. It builds up numerical concepts step by step while linking them to the underlying mathematical models.

Link to the course: [link](https://www11.ceda.polimi.it/schedaincarico/schedaincarico/controller/scheda_pubblica/SchedaPublic.do?&evn_default=evento&c_classe=863565&lang=IT&__pj0=0&__pj1=fd788566d3622390ad34d698fed5e04e).

We will study flow, transport, and poroelastic deformation in porous media, alongside numerical methods such as:

- mixed formulations  
- discretization on general grids  
- hybrid-dimensional PDEs  
- conservation laws  
- advection–diffusion–reaction problems  
- techniques for nonlinear and coupled systems  

## Installation for Linux

The package requires Python >= 3.13

Many functionalities depend on [PorePy](https://github.com/pmgbergen/porepy) and [PyGeoN](https://github.com/compgeo-mox/pygeon), so these packages will be installed.
To install all the dependencies
```bash
pip install -e .
```

## Issues
Create an [issue](https://github.com/compgeo-mox/lec_compgeo/issues).

## License
See [license](./LICENSE.md).
