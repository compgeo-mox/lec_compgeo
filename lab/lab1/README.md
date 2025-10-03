# Laboratory 1: Python Programming and Grids in Geosciences

This laboratory introduces practical Python programming through geoscience-focused projects and explores the use of computational grids with PorePy and PyGeoN. The lab is organized into two main Jupyter notebooks:

---

## 1. `ex1.ipynb` — Python Programming Projects

- **Project-based learning:** Each project introduces new Python features and problem-solving strategies.
- **Topics covered:**
  - User input, type casting, variables, and functions.
  - Temperature conversion (Fahrenheit, Celsius, Kelvin).
  - The van der Waals equation for real gases, with default and keyword arguments.
  - Working with modules, tuples, and multiple return values.
  - String manipulation, slicing, and conditional logic.
  - Loops (`for`, `while`), recursion, and list comprehensions.
  - Dictionaries and data conversion (Roman numerals, binary).
  - Numerical concepts: machine epsilon, Fibonacci and Recaman sequences.
  - Monte Carlo simulation for estimating π, including visualization with Matplotlib.
- **Exercises:** Each section includes exercises to reinforce programming concepts and scientific computing skills.

---

## 2. `grid.ipynb` — Grids in PorePy and PyGeoN

- **Grid construction:** Creating Cartesian and simplex grids in 1D, 2D, and 3D using PorePy.
- **Grid properties:** Accessing cell, face, and node counts; coordinates; and grid dimensions.
- **Geometric computations:** Using `compute_geometry()` to obtain cell centers, volumes, face areas, and normals.
- **Grid perturbation:** Modifying node positions and recomputing geometry.
- **Visualization:** Plotting grids and grid properties with Matplotlib and exporting to VTK/ParaView.
- **Advanced grids:** Creating simplex and structured triangular grids, and importing from external tools (e.g., Gmsh).
- **Topological information:** Understanding cell-face and face-node relations, and working with sparse matrices.
- **PyGeoN integration:** Generating and converting grids, constructing grids from boundaries or points, and handling concave domains.
- **Practical examples:** Step-by-step code for grid creation, manipulation, and visualization.

---

## How to Use

1. **Start with `ex1.ipynb`** to practice Python programming through hands-on projects and exercises.
2. **Continue with `grid.ipynb`** to learn about computational grids and their use in geoscientific simulations.
3. **Work through the exercises** in each notebook to deepen your understanding and gain practical experience.

---

## Requirements

- Python 3.x
- Jupyter Notebook
- Numpy
- Matplotlib
- PorePy
- PyGeoN
- (Optional) Scipy

---

For further reading, see the official documentation for [Python](https://docs.python.org/3/), [Numpy](https://numpy.org/doc/), [Matplotlib](https://matplotlib.org/stable/), [PorePy](https://github.com/pmgbergen/porepy), and [PyGeoN](https://github.com/AlessioPaglialunga/pygeon).